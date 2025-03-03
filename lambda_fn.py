import boto3
import csv
import uuid

# Initialize AWS clients
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CSVDataTable')  # Updated DynamoDB table name

def lambda_handler(event, context):
    # Get bucket and object key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Ensure the event is from the correct bucket
    if bucket_name != 'csv-upload-bucket':
        return {
            'statusCode': 400,
            'body': f'Unexpected bucket: {bucket_name}'
        }

    try:
        # Get the CSV file from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        content = response['Body'].read().decode('utf-8').splitlines()

        # Read the CSV content
        csv_reader = csv.reader(content)
        headers = next(csv_reader)  # Skip the header row if needed

        # Insert each row into DynamoDB
        for row in csv_reader:
            item = {
                'id': str(uuid.uuid4()),  # Generate a unique ID for each row
                'name': row[0],           # Assuming 'name' is the first column
                'email': row[1],          # Assuming 'email' is the second column
                'city': row[2]            # Assuming 'city' is the third column
            }
            table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': f'Successfully inserted data from {object_key} into DynamoDB!'
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error processing file {object_key}: {str(e)}'
        }
