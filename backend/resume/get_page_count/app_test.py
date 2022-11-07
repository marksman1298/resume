# import json
# import unittest
# import boto3
# import os
# import mock
# from moto import mock_dynamodb2

# from app import lambda_handler

# DEFAULT_REGION = 'ca-central-1'
# DYNAMODB_TABLE_NAME = 'test_table'

# @mock_dynamodb2
# @mock.patch.dict(os.environ, {'DB_TABLE_NAME': DYNAMODB_TABLE_NAME})
# class TestLambdaFunction(unittest.TestCase):
#     def createDB(self):
#         self.dynamodb = boto3.client('dynamodb', region_name=DEFAULT_REGION)
#         try:
#             self.table = self.dynamodb.create_table(
#                 TableName=DYNAMODB_TABLE_NAME,
#                 KeySchema=[
#                     {
#                         'AttributeName': 'id',
#                         'KeyType': 'HASH'
#                     }
#                 ],
#                 AttributeDefinitions=[
#                     {
#                         'AttributeName': 'id',
#                         'AttributeType': 'S'
#                     }
#                 ],
#             )
#             self.dynamodb.put_item(Item={"id": "0", "page_views": 7})
#         except self.dynamodb.exceptions.ResourceInUseException:
#             self.table = boto3.resource('dynamodb').Table(DYNAMODB_TABLE_NAME)

#     def test_get_count(self):
#         count = lambda_handler() 
#         self.assertEqual(7, count["Item"]["page_counter"])
