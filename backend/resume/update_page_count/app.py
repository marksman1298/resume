import boto3

def lambda_handler(event, context):    
    dynamodb = boto3.resource("dynamodb")
    
    table = dynamodb.Table("visitor-counter")

    get_counter = table.get_item(
        Key={
            "id":"0"
        }
    )
    
    value = get_counter["Item"]["page_views"]
    
    response = table.update_item(
        Key={
            "id":"0"
        },
        UpdateExpression="SET page_views = :val1",
        ExpressionAttributeValues={
            ":val1": int(value) + 1
        },
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
        'body': get_counter["Item"]["page_views"] # remove? call get instead?
    }