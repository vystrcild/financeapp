from flask import Flask, jsonify, request
from flask_cors import CORS
from calc import final


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS - In a production environment, you should only allow cross-origin requests from the domain
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong kundafdsfds!')

@app.route('/expenses', methods=['GET'])
def get_data():
    return jsonify({
        'status': 'success',
        'expenses': final
    })

@app.route('/send', methods=['GET', 'POST'])
def post_data():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data)
    response_object['message'] = "Veryy succeeesss!"
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()