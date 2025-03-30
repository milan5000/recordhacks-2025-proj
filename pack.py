from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enables CORS for all routes and origins. Should NOT be used in production

PACKING_LIST = {
    "essential": [
        {
            "id": "1",
            "name": 'Canned Food',
            "available": "true"
        },
        {
            "id": "2",
            "name": 'Bottled Water',
            "available": "true"
        },
        {
            "id": "3",
            "name": '$25-100 or more',
            "available": "true"
        }
    ]
}

@app.route('/')
def home():
    return "PackAdvisor is live! Go to /packing-list to view essentials."

@app.route('/packing-list')
def get_packing_list():
    return jsonify(PACKING_LIST)

if __name__ == '__main__':
    app.run(debug=True)
