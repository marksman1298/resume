import boto3

dynamodb = boto3.resource("dynamodb")
    
table = dynamodb.Table("resume_counter")

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

print(get_counter["Item"]["page_views"])