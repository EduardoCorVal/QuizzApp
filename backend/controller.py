# Final Project: Quiz Application with Microservices
# Date: 28-Nov-2022
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
#          A01751587 Paulo Ogando Gulias 
#          A01745865 José Ángel García Gómez 
#          A01745419 José Luis Madrigal Sánchez

'''
This file consists of the definition of the Controller class wich is in charge of handling the requests and responses of the API.
'''


# Importing libraries and dependencies 
import config as config
from flask import Flask, request
from flask_cors import CORS as CORS
from QuestionModel import QuestionModel
from UserModel import UserModel


class Controller ():
    UserModel = UserModel()
    QuestionModel = QuestionModel()

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/*": {"origins": "*"}})
        self.app.route('/')(self.test)
        # Routes for Question Table
        self.app.route('/getAllQuestions')(self.get_all_questions)
        # Routes for User Table
        self.app.route('/getAllUsers')(self.get_all_users)
        self.app.route('/getTop10Users')(self.get_top_10_users)
        self.app.route('/user', methods=['POST'])(self.add_user)
        self.app.route('/user/<id>', methods=['GET'])(self.get_user)


    def test(self):
        print("TEST SUCCESS")
        return 'TEST SUCCESS'
    
    def get_all_questions(self):
        response = self.QuestionModel.read_questions()
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            if ('Items' in response):
                return {'Items': response['Items']}
            return {'msg': 'Item not found!'}
        return {
            'msg': 'Some error occured',
            'response': response
        }
    

    def get_all_users(self):
        response = self.UserModel.read_users()
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            if ('Items' in response):
                return {'Items': response['Items']}
            return {'msg': 'Item not found!'}
        return {
            'msg': 'Some error occured',
            'response': response
        }


    def get_top_10_users(self):
        response = self.UserModel.get_top_10_users()
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            if ('Items' in response):
                return {'Items': response['Items']}
            return {'msg': 'Item not found!'}
        return {
            'msg': 'Some error occured',
            'response': response
        }


    def add_user(self):
            data = request.get_json()
            response = self.UserModel.write_to_user(
                data['name'], data['points'])
            if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
                return {
                    'msg': 'Added successfully',
                }
            return {
                'msg': 'Some error occcured',
                'response': response
            }
    

    def get_user(self, id):
        response = self.UserModel.read_from_user(id)
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            if ('Item' in response):
                return {'Item': response['Item']}
            return {'msg': 'Item not found!'}
        return {
            'msg': 'Some error occured',
            'response': response
        }



    def run(self):
        self.app.run(host='127.0.0.1', port=5000, debug=True)
