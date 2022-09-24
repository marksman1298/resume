import boto3

dynamodb = boto3.resource("dynamodb")
all_tables = [table.name for table in dynamodb.tables.all()] 

if "resume_counter" not in all_tables:
    resume_table = dynamodb.create_table(
        TableName="resume_counter",
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )

    resume_table.wait_until_exists()

else:
    table = dynamodb.Table("resume_counter")
    table.put_item(
        Item={
            "id": "0"
        }
    )


