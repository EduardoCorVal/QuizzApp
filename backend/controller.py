'''
This file consists of all the functions that are used to interact with the database.
It also consists of the code needed to connect to the dynamoDB database using the
configurations set in config.py file.
'''

from boto3 import resource
import config as config
import time
from decimal import Decimal

AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN = config.AWS_SESSION_TOKEN
REGION_NAME = config.REGION_NAME

dynamodb_client = resource(
    service_name='dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=REGION_NAME
)


def create_table_user():
    table = dynamodb_client.create_table(
        TableName='UserQuizzApp',  # Name of the table
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # HASH = partition key, RANGE = sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',  # Name of the attribute
                'AttributeType': 'N'   # N = Number (S = String, B = Binary)
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


UserTable = dynamodb_client.Table('UserQuizzApp')


def write_to_user(name, points):
    id = Decimal(str(time.time()).replace('.', ''))
    response = UserTable.put_item(
        Item={
            'id': id,
            'name': name,
            'points': points,
        }
    )
    return response


def read_from_user(name):
    response = UserTable.get_item(
        Key={
            'name': name,
        },
        ProjectionExpression='points'
    )
    return response


def update_in_user(name, data):
    response = UserTable.update_item(
        Key={
            'name': name
        },
        AttributeUpdates={
            'points': {
                'Value': data['points'],
                # available options = DELETE(delete), PUT(set/update), ADD(increment)
                'Action': 'PUT'
            }
        },
        ReturnValues="UPDATED_NEW"  # returns the new updated values
    )
    return response
