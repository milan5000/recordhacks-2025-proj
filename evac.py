from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_shelters', methods=['POST'])
def get_shelters():
    data = request.get_json()
    lat, lng = data['latitude'], data['longitude']

    # Simulated shelter data (can be fetched from DB or API)
    shelters = [
        {"name": "Shelter A", "lat": lat + 0.01, "lng": lng + 0.01},
        {"name": "Shelter B", "lat": lat - 0.01, "lng": lng - 0.01},
    ]
    return jsonify(shelters)

if __name__ == '__main__':
    app.run(debug=True)
