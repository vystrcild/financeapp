from flask import Flask, jsonify, request
from flask_cors import CORS
from models import post_data, get_bilance, get_monthly_change, get_overview, get_investments

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS - In a production environment, you should only allow cross-origin requests from the domain
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def test():
    return "AHOJ"

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify({
        'status': 'success',
        'bilance': get_bilance(),
        'assets_change': get_monthly_change()
    })

@app.route('/overview', methods=['GET'])
def get_overview_endpoint():
    return jsonify({
        'status': 'success',
        'overview': get_overview(),
    })

@app.route('/investments', methods=['GET'])
def get_investments_endpoint():
    return jsonify({
        'status': 'success',
        'investments': get_investments(),
    })

@app.route('/send', methods=['GET', 'POST'])
def postdata():
    response_object = {'status': 'success'}
    data = request.get_json()
    post_data(data)
    response_object['message'] = "Veryy succeeesss!"
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()