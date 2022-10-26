import boto3

def create_dynamodb(table_name: str):
    dynamodb = boto3.resource("dynamodb")
    all_tables = [table.name for table in dynamodb.tables.all()] 

    if table_name not in all_tables:
        resume_table = dynamodb.create_table(
            TableName=table_name,
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
        resume_table.put_item(
            Item={
                "id": "0",
                "page_views": 0
            }
        )
        return 0
    return "table already exists"




