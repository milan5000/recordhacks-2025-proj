from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes and origins. Should NOT be used in production

PACKING_LIST = {
    "packing_list": [
        { # essential
            "id": 'Canned Food',
            "name": 'Canned Food',
            "available": "true",
            "list": 'essential',
            "priority_level": 'very high'
        },
        {
            "id": 'Bottled Water',
            "name": 'Bottled Water',
            "available": "true",
            "list": 'essential',
            "priority_level": 'very high'
        },
        {
            "id": '$25-100 or more',
            "name": '$25-100 or more',
            "available": "true",
            "list": 'essential',
            "priority_level": 'very high'
        },
        { # infant
            "id": "Baby formula (3-day supply)",
            "name": "Baby formula (3-day supply)",
            "available": "true",
            "list": "infant"
            "priority_level": 'very high'
        },
        {
            "id": "Bottles",
            "name": "Bottles",
            "available": "true",
            "list": "infant"
            "priority_level": 'very high'
        },
        {
            "id": "Baby food",
            "name": "Baby food",
            "available": "true",
            "list": "infant"
            "priority_level": 'very high'
        },
        {
            "id": "Diapers and wipes (3-day supply)",
            "name": "Diapers and wipes (3-day supply)",
            "available": "true",
            "list": "infant"
            "priority_level": 'very high'
        },
        {
            "id": "Baby carrier or stroller",
            "name": "Baby carrier or stroller",
            "available": "true",
            "list": "infant"
            "priority_level": 'high'
        },
        {
            "id": "Comfort item (toy, blanket)",
            "name": "Comfort item (toy, blanket)",
            "available": "true",
            "list": "infant"
            "priority_level": 'low'
        },
        { # medical needs
            "id": "Extra prescription medications (7-day supply)",
            "name": "Extra prescription medications (7-day supply)",
            "available": "true",
            "list": "medical_needs"
            "priority_level": 'very high'
        },
        {
            "id": "Backup medical devices (hearing aid batteries, extra glasses)",
            "name": "Backup medical devices (hearing aid batteries, extra glasses)",
            "available": "true",
            "list": "medical_needs"
            "priority_level": 'high'
        },
        {
            "id": "Epinephrine auto-injector (if needed)",
            "name": "Epinephrine auto-injector (if needed)",
            "available": "true",
            "list": "medical_needs"
            "priority_level": 'high'
        },
        { # pets
            "id": "Pet food",
            "name": "Pet food",
            "available": "true",
            "list": "pets"
            "priority_level": 'very high'
        },
        {
            "id": "Collapsible bowls",
            "name": "Collapsible bowls",
            "available": "true",
            "list": "pets"
            "priority_level": 'high'
        },
        {
            "id": "Collar + Leash",
            "name": "Collar + Leash",
            "available": "true",
            "list": "pets"
            "priority_level": 'high'
        },
        {
            "id": "Pet carrier",
            "name": "Pet carrier",
            "available": "true",
            "list": "pets"
            "priority_level": 'low'
        },
        {
            "id": "Vaccination records & ID tag",
            "name": "Vaccination records & ID tag",
            "available": "true",
            "list": "pets"
            "priority_level": 'low'
        },
        { # hurricane_flood
            "id": "Waterproof container for documents",
            "name": "Waterproof container for documents",
            "available": "true",
            "list": "hurricane_flood"
            "priority_level": 'very high'
        },
        {
            "id": "Life jackets (for children & non-swimmers)",
            "name": "Life jackets (for children & non-swimmers)",
            "available": "true",
            "list": "hurricane_flood"
            "priority_level": 'very high'
        },
        {
            "id": "Plastic bags to keep clothes & supplies dry",
            "name": "Plastic bags to keep clothes & supplies dry",
            "available": "true",
            "list": "hurricane_flood"
            "priority_level": 'high'
        },
        {
            "id": "Paper maps",
            "name": "Paper maps",
            "available": "true",
            "list": "hurricane_flood"
            "priority_level": 'medium'
        },
        {
            "id": "Rope (for securing items or rescue situations)",
            "name": "Rope (for securing items or rescue situations)",
            "available": "true",
            "list": "hurricane_flood"
            "priority_level": 'medium'
        },
        {
            "id": "Gasoline (fuel car if gas stations closed)",
            "name": "Gasoline (fuel car if gas stations closed)",
            "available": "true",
            "list": "hurricane_flood"
            "priority_level": 'medium'
        },
        {
            "id": "Tarps (keeps things dry)",
            "name": "Tarps (keeps things dry)",
            "available": "true",
            "list": "hurricane_flood"
        },
        { # tornado
            "id": "Bike helmet (to protect head from flying objects)",
            "name": "Bike helmet (to protect head from flying objects)",
            "available": "true",
            "list": "tornado"
            "priority_level": 'very high'
        },
        {
            "id": "N95 masks (in-case poor air quality)",
            "name": "N95 masks (in-case poor air quality)",
            "available": "true",
            "list": "tornado"
            "priority_level": 'high'
        },
        {
            "id": "Paper maps (if evacuating)",
            "name": "Paper maps (if evacuating)",
            "available": "true",
            "list": "tornado"
            "priority_level": 'medium'
        },
        { # earthquake
            "id": "Bike helmet (to protect head from falling objects)",
            "name": "Bike helmet (to protect head from falling objects)",
            "available": "true",
            "list": "earthquake"
            "priority_level": 'very high'
        },
        {
            "id": "Crowbar (to move debris/obstacle)",
            "name": "Crowbar (to move debris/obstacle)",
            "available": "true",
            "list": "earthquake"
            "priority_level": 'medium'
        },
        {
            "id": "N95 masks (in-case trapped under debris)",
            "name": "N95 masks (in-case trapped under debris)",
            "available": "true",
            "list": "earthquake"
            "priority_level": 'medium'
        },
        { # wildfire
            "id": "N95 masks (in-case poor air quality)",
            "name": "N95 masks (in-case poor air quality)",
            "available": "true",
            "list": "wildfire"
            "priority_level": 'very high'
        },
        {
            "id": "Fire-resistant gloves",
            "name": "Fire-resistant gloves",
            "available": "true",
            "list": "wildfire"
            "priority_level": 'high'
        },
        {
            "id": "Paper maps",
            "name": "Paper maps",
            "available": "true",
            "list": "wildfire"
            "priority_level": 'medium'
        },
        {
            "id": "Fire-resistant clothing (cotton or wool, long sleeves & pants)",
            "name": "Fire-resistant clothing (cotton or wool, long sleeves & pants)",
            "available": "true",
            "list": "wildfire"
            "priority_level": 'low'
        }
        { # winterstorm_blizzard
            "id": "Extra blankets and sleeping bags",
            "name": "Extra blankets and sleeping bags",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'very high'
        },
        {
            "id": "Gas powered heat source",
            "name": "Gas powered heat source",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'high'
        },
        {
            "id": "Hand warmers and thermal clothing",
            "name": "Hand warmers and thermal clothing",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'high'
        },
        {
            "id": "Snow shovel and ice scraper (to move snow/obstacle)",
            "name": "Snow shovel and ice scraper (to move snow/obstacle)",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'medium'
        },
        {
            "id": "Jumper cables (for car)",
            "name": "Jumper cables (for car)",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'high'
        },
        {
            "id": "Snow chains for tires (for car)",
            "name": "Snow chains for tires (for car)",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'medium'
        },
        {
            "id": "Tow rope (for car)",
            "name": "Tow rope (for car)",
            "available": "true",
            "list": "winterstorm_blizzard"
            "priority_level": 'medium'
        },
        { # important_not_urgent
            "id": "Can opener",
            "name": "Can opener",
            "available": "true",
            "list": "important_not_urgent"
            "priority_level": 'medium'
        },
        {
            "id": "NOAA radio (for real-time weather updates)",
            "name": "NOAA radio (for real-time weather updates)",
            "available": "true",
            "list": "important_not_urgent"
            "priority_level": 'medium'
        },
        {
            "id": "Whistle to signal for help",
            "name": "Whistle to signal for help",
            "available": "true",
            "list": "important_not_urgent"
            "priority_level": 'medium'
        },
        {
            "id": "Personal sanitation",
            "name": "Personal sanitation",
            "available": "true",
            "list": "important_not_urgent"
            "priority_level": 'medium'
        },
        {
            "id": "Non-sparking wrench or pliers to turn off utilities",
            "name": "Non-sparking wrench or pliers to turn off utilities",
            "available": "true",
            "list": "important_not_urgent"
            "priority_level": 'medium'
        },
        {
            "id": "Local maps",
            "name": "Local maps",
            "available": "true",
            "list": "important_not_urgent"
            "priority_level": 'medium'
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
