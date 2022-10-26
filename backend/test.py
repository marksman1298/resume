import boto3
def update_views(table: str):
    dynamodb = boto3.resource("dynamodb")
        
    table = dynamodb.Table(table)

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
    return get_counter["Item"]["page_views"]
    # print(get_counter["Item"]["page_views"])

print(update_views("test"))