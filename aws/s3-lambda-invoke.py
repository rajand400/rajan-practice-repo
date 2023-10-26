import boto3

def lambda_handler(event, context):
    # Get the S3 bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Create a Lambda client
    lambda_client = boto3.client('lambda')
    
    # Invoke the Lambda function
    response = lambda_client.invoke(
        FunctionName='your-lambda-function-name',
        InvocationType='Event',
        Payload='{"bucket": "' + bucket + '", "key": "' + key + '"}'
    )
    
    # Print the response
    print(response)
In this code, you need to replace 'your-lambda-function-name' with the actual name of your Lambda function. The Payload parameter is used to pass the S3 bucket and key information to the Lambda function.

Please note that you'll need to have the Boto3 library installed and configured with your AWS credentials for this code to work.

