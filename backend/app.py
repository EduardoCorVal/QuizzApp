from flask import Flask, request
import controller as dynamodb

app = Flask(__name__)


@app.route('/test')
def test():
    print("TEST SUCCESS")
    return 'TEST SUCCESS'


@app.route('/create')
def root_route():
    dynamodb.create_table_user()
    return 'Table created'


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


@app.route('/user/<string:name>', methods=['GET'])
def get_user(name):
    response = dynamodb.read_from_user(name)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        if ('Item' in response):
            return {'Item': response['Item']}
        return {'msg': 'Item not found!'}
    return {
        'msg': 'Some error occured',
        'response': response
    }


@app.route('/user/<string:name>', methods=['PUT'])
def update_user(name):

    data = request.get_json()
    response = dynamodb.update_in_user(name, data)
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
