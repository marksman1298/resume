import boto3
# import os

# AWS_REGION = os.environ.get('AWS_REGION', 'ca-central-1')
# DB_TABLE_NAME = os.environ.get('DB_TABLE_NAME', 'test_table')
# DYNAMODB_CLIENT = boto3.resource("dynamodb", region_name=AWS_REGION)
# DYNAMODB_TABLE = DYNAMODB_CLIENT.Table(DB_TABLE_NAME)
def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    
    table = dynamodb.Table("visitor-counter")
    
    response = table.get_item(
        Key={
            "id":"0"
        }
    )

    if response != 200:
        return response

    return {
        'headers' : {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*'
        },
        'statusCode': response,
        'body': response["Item"]["page_counter"]
    }

