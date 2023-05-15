'''
This file consists of all the functions that are used to interact with the database.
It also consists of the code needed to connect to the dynamoDB database using the
configurations set in config.py file.
'''

from boto3 import resource
import config as config
import time
from decimal import Decimal
from operator import itemgetter
from poolQuestions import items
import random

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

## Methods related to 'UserQuizzApp' table

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
            # id generet is a timestamp kind of id. 
            # So, numbers with higher values are newer
            'id': id, 
            'name': name,
            'points': points,
        }
    )
    return response


def read_from_user(id):
    response = UserTable.get_item(
        Key={
            'id': id,
        },
        ProjectionExpression='points'
    )
    return response

def read_users():
    response = UserTable.response = UserTable.scan()
    return response


def get_top_10_users():
    response = UserTable.scan()
    items = response['Items']
    # Sort the items in the list descending by id. (The id itself is a timestamp)
    items.sort(key=itemgetter('id'), reverse=True)
    # Sort the items in the list descending by points
    items.sort(key=itemgetter('points'), reverse=True)
    # Get the top 10 items
    top_10_items = items[:10]
    response['Items'] = top_10_items
    return response


def update_in_user(id, data):
    response = UserTable.update_item(
        Key={
            'id': id
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


## Methods related to 'QuestionsQuizzApp' table

def create_table_questions():
    table = dynamodb_client.create_table(
        TableName='QuestionsQuizzApp',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH' 
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

QuestionsTable = dynamodb_client.Table('QuestionsQuizzApp')


# Elements divided in lotes of 25 or less
batch_size = 10
batch_items = [items[i:i+batch_size] for i in range(0, len(items), batch_size)]

# Insert each batch in the table using batch_write_item
def insert_questions_table():
    for batch in batch_items:
        response = dynamodb_client.batch_write_item(
            RequestItems={
                'QuestionsQuizzApp': [
                    {'PutRequest': {'Item': item}} for item in batch
                ]
            }
        )
    return response
    
def read_questions():
    response = QuestionsTable.scan()
    all_questions = response['Items']
    random.shuffle(all_questions)
    return response