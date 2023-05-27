# Final Project: Quiz Application with Microservices
# Date: 29-May-2023
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
#          A01751587 Paulo Ogando Gulias 
#          A01745865 José Ángel García Gómez 
#          A01745419 José Luis Madrigal Sánchez


'''
This file consists of the definition of the UserModel class that has all the functions that are used to interact with the User database.
It also consists of the code needed to connect to the dynamoDB database using the
configurations set in config.py file.
'''


# Importing libraries
from boto3 import resource
import config as config
import time
from decimal import Decimal
from operator import itemgetter


AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN = config.AWS_SESSION_TOKEN
REGION_NAME = config.REGION_NAME


class UserModel ():
    __tablename__ = 'UserQuizzApp'
    dynamodb_client = resource(
        service_name='dynamodb',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=REGION_NAME
    )


    def __init__(self):
        self.UserTable = self.create_table_user()


    def create_table_user(self):
        if (not self.dynamodb_client.Table(self.__tablename__)):
            self.dynamodb_client.create_table(
                TableName=self.__tablename__,  
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
        return self.dynamodb_client.Table(self.__tablename__)


    def read_users(self):
        response = self.UserTable.response = self.UserTable.scan()
        return response


    def write_to_user(self, name, points):
        id = Decimal(str(time.time()).replace('.', ''))
        response = self.UserTable.put_item(
            Item={
                # id generated is a timestamp kind of id. 
                # So, numbers with higher values are newer
                'id': id, 
                'name': name,
                'points': points,
            }
        )
        return response


    def get_top_10_users(self):
        response = self.UserTable.scan()
        items = response['Items']
        # Sort the items in the list descending by id. (The id itself is a timestamp)
        items.sort(key=itemgetter('id'), reverse=True)
        # Sort the items in the list descending by points
        items.sort(key=itemgetter('points'), reverse=True)
        # Get the top 10 items
        top_10_items = items[:10]
        response['Items'] = top_10_items
        return response
