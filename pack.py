from flask import Flask, jsonify

app = Flask(__name__)


PACKING_LIST = {
    "essential": [
        "Water (1 gallon per person per day, 3-day supply)",
        "Non-perishable food (3-day supply)",
        "Flashlight with extra batteries",
        "Battery-powered or hand crank radio (NOAA weather alerts)",
        "First aid kit (bandages, antiseptic, gloves, etc.)",
        "Prescription medications and medical supplies",
        "Whistle to signal for help",
        "Multi-tool or Swiss Army knife",
        "ID and important documents",
        "Phone charger & power bank",
        "Emergency blanket or sleeping bag",
        "Toothbrush, toothpaste, soap, and hygiene supplies"
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
