from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes and origins. Should NOT be used in production

PACKING_LIST = {
    "essential": [
        {
            "id": 'Canned Food',
            "name": 'Canned Food',
            "available": "true",
            "list": 'essential',
        },
        {
            "id": 'Bottled Water',
            "name": 'Bottled Water',
            "available": "true",
            "list": 'essential',
        },
        {
            "id": '$25-100 or more',
            "name": '$25-100 or more',
            "available": "true",
            "list": 'essential',
        }
    ]
}

HURRICANE_FLOOD = {
    "hurricane_flood": [
        {
            "id": "Waterproof container for documents",
            "name": "Waterproof container for documents",
            "available": "true",
            "list": "hurricane_flood"
        },
        {
            "id": "Life jackets (for children & non-swimmers)",
            "name": "Life jackets (for children & non-swimmers)",
            "available": "true",
            "list": "hurricane_flood"
        },
        {
            "id": "Plastic bags to keep clothes & supplies dry",
            "name": "Plastic bags to keep clothes & supplies dry",
            "available": "true",
            "list": "hurricane_flood"
        },
        {
            "id": "Paper maps",
            "name": "Paper maps",
            "available": "true",
            "list": "hurricane_flood"
        },
        {
            "id": "Rope (for securing items or rescue situations)",
            "name": "Rope (for securing items or rescue situations)",
            "available": "true",
            "list": "hurricane_flood"
        },
        {
            "id": "Gasoline (fuel car if gas stations closed)",
            "name": "Gasoline (fuel car if gas stations closed)",
            "available": "true",
            "list": "hurricane_flood"
        },
        {
            "id": "Tarps (keeps things dry)",
            "name": "Tarps (keeps things dry)",
            "available": "true",
            "list": "hurricane_flood"
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
