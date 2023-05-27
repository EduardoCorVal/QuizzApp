# Final Project: Quiz Application with Microservices
# Date: 29-May-2023
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
#          A01751587 Paulo Ogando Gulias 
#          A01745865 José Ángel García Gómez 
#          A01745419 José Luis Madrigal Sánchez

'''
This file consists of the definition of the QuestionModel class that has all the functions that are used to interact with the Questions database.
It also consists of the code needed to connect to the dynamoDB database using the
configurations set in config.py file.
'''

from boto3 import resource
import config as config
import random

AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN = config.AWS_SESSION_TOKEN
REGION_NAME = config.REGION_NAME

class QuestionModel ():
    __tablename__ = 'QuestionsQuizzApp'
    dynamodb_client = resource(
        service_name='dynamodb',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        aws_session_token=AWS_SESSION_TOKEN,
        region_name=REGION_NAME
    )

    def __init__(self):
        self.QuestionTable = self.create_table_question()
    
    def create_table_question(self):
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

    # This function already sort the items in the response ramdomly.
    # So, when calling it, the response (the questions needed) is already sorted by random.
    def read_questions(self):
        response = self.QuestionTable.scan()
        all_questions = response['Items']
        random.shuffle(all_questions)
        return response
