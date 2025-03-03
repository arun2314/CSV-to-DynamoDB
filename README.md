## AWS S3 to DynamoDB Integration

This guide outlines the step-by-step process to set up an S3 bucket, DynamoDB table, and a Lambda function for processing CSV files.

### Step 1: Create the S3 bucket
1. Go to the AWS S3 Console.
2. Click "Create bucket".
3. Name it `csv-upload-bucket`.
4. Leave other settings as default and click "Create bucket".

### Step 2: Create the DynamoDB table
1. Go to the AWS DynamoDB Console.
2. Click "Create table".
3. Table name: `CSVDataTable`.
4. Partition key: `id` → Type: `String` (Unique IDs for each row).
5. Click "Create table".

### Step 3: Create an IAM role for the Lambda function
1. Go to the AWS IAM Console.
2. Click "Roles" → "Create role".
3. Choose "Lambda" as the trusted entity.
4. Attach the following policies:
   - `AmazonS3ReadOnlyAccess` (to read the CSV from S3).
   - `AmazonDynamoDBFullAccess` (to write data to DynamoDB).
5. Click "Next" → "Create role".
6. Name it `LambdaS3DynamoDBRole`.

### Step 4: Create the Lambda function
1. Go to the AWS Lambda Console.
2. Click "Create function" → "Author from scratch".
3. Function name: `S3ToDynamoDBFunction`.
4. Runtime: Python 3.x (latest version preferred).
5. Execution role: Use existing role → Select `LambdaS3DynamoDBRole`.
6. Click "Create function".

### Step 5: Write the Lambda function (lambdaFunc.py)
Add your Python script to process CSV files from S3 and insert data into DynamoDB.

### Step 6: Add an S3 trigger to the Lambda function
1. Open your `S3ToDynamoDBFunction` in the Lambda Console.
2. Click "Add trigger".
3. Select `S3` as the source.
4. Choose `csv-upload-bucket`.
5. Event type: `PUT` (For new file uploads).
6. Click "Add".

### Step 7: Upload a CSV file to S3
1. Go to the S3 Console.
2. Open `csv-upload-bucket`.
3. Upload a sample CSV file (`sample.csv`).

### Step 8: Check DynamoDB
1. Go to `CSVDataTable` in the DynamoDB Console.
2. Click "Explore table items".
3. Verify that each row from the CSV has been inserted as an item.

