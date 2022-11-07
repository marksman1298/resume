import boto3
import os
from matplotlib import test
import pytest 
from moto import mock_dynamodb
from test import *
@mock_dynamodb
def test_update_count():
    dynamodb = boto3.resource("dynamodb")
    tableName = "test2"
    table = dynamodb.create_table(
        TableName=tableName,
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
    table.put_item(Item={"id": "0", "page_views": 7})
    result = update_views(tableName)
    assert 8 == int(result)

test_update_count()