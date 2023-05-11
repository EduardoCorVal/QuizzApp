from flask import Flask, request
import controller as dynamodb
from flask_cors import CORS as CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/test')
def test():
    print("TEST SUCCESS")
    return 'TEST SUCCESS'


@app.route('/create')
def root_route():
    dynamodb.create_table_user()
    return 'Table created'


# Routes for Questions Table

@app.route('/getAllQuestions', methods=['GET'])
def get_all_questions():
    response = dynamodb.read_questions()
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if ('Items' in response):
            return {'Items': response['Items']}
        return {'msg': 'Item not found!'}
    return {
        'msg': 'Some error occured',
        'response': response
    }

# Routes for User Table


@app.route('/getAllUsers', methods=['GET'])
def get_all_users():
    response = dynamodb.read_users()
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if ('Items' in response):
            return {'Items': response['Items']}
        return {'msg': 'Item not found!'}
    return {
        'msg': 'Some error occured',
        'response': response
    }


@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    response = dynamodb.write_to_user(
        data['name'], data['points'])
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }
    return {
        'msg': 'Some error occcured',
        'response': response
    }


@app.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    response = dynamodb.read_from_user(id)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if ('Item' in response):
            return {'Item': response['Item']}
        return {'msg': 'Item not found!'}
    return {
        'msg': 'Some error occured',
        'response': response
    }


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):

    data = request.get_json()
    response = dynamodb.update_in_user(id, data)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Updated successfully',
            'ModifiedAttributes': response['Attributes'],
            'response': response['ResponseMetadata']
        }
    return {
        'msg': 'Some error occured',
        'response': response
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
