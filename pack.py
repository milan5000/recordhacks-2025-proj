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

INFANT = {
    "infant": [
        {
            "id": "Baby formula (3-day supply)",
            "name": "Baby formula (3-day supply)",
            "available": "true",
            "list": "infant"
        },
        {
            "id": "Bottles",
            "name": "Bottles",
            "available": "true",
            "list": "infant"
        },
        {
            "id": "Baby food",
            "name": "Baby food",
            "available": "true",
            "list": "infant"
        },
        {
            "id": "Diapers and wipes (3-day supply)",
            "name": "Diapers and wipes (3-day supply)",
            "available": "true",
            "list": "infant"
        },
        {
            "id": "Baby carrier or stroller",
            "name": "Baby carrier or stroller",
            "available": "true",
            "list": "infant"
        },
        {
            "id": "Comfort item (toy, blanket)",
            "name": "Comfort item (toy, blanket)",
            "available": "true",
            "list": "infant"
        }
    ]
}

MEDICAL_NEEDS = {
    "medical_needs": [
        {
            "id": "Extra prescription medications (7-day supply)",
            "name": "Extra prescription medications (7-day supply)",
            "available": "true",
            "list": "medical_needs"
        },
        {
            "id": "Backup medical devices (hearing aid batteries, extra glasses)",
            "name": "Backup medical devices (hearing aid batteries, extra glasses)",
            "available": "true",
            "list": "medical_needs"
        },
        {
            "id": "Epinephrine auto-injector (if needed)",
            "name": "Epinephrine auto-injector (if needed)",
            "available": "true",
            "list": "medical_needs"
        }
    ]
}

PETS = {
    "pets": [
        {
            "id": "Pet food",
            "name": "Pet food",
            "available": "true",
            "list": "pets"
        },
        {
            "id": "Collapsible bowls",
            "name": "Collapsible bowls",
            "available": "true",
            "list": "pets"
        },
        {
            "id": "Collar + Leash",
            "name": "Collar + Leash",
            "available": "true",
            "list": "pets"
        },
        {
            "id": "Pet carrier",
            "name": "Pet carrier",
            "available": "true",
            "list": "pets"
        },
        {
            "id": "Vaccination records & ID tag",
            "name": "Vaccination records & ID tag",
            "available": "true",
            "list": "pets"
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

TORNADO = {
    "tornado": [
        {
            "id": "Bike helmet (to protect head from flying objects)",
            "name": "Bike helmet (to protect head from flying objects)",
            "available": "true",
            "list": "tornado"
        },
        {
            "id": "N95 masks (in-case poor air quality)",
            "name": "N95 masks (in-case poor air quality)",
            "available": "true",
            "list": "tornado"
        },
        {
            "id": "Bike helmet (to protect head from flying objects)",
            "name": "Bike helmet (to protect head from flying objects)",
            "available": "true",
            "list": "tornado"
        },
        {
            "id": "Safety goggles (to protect head from flying objects)",
            "name": "Bike helmet (to protect head from flying objects)",
            "available": "true",
            "list": "tornado"
        },
        {
            "id": "Paper maps (if evacuating)",
            "name": "Paper maps (if evacuating)",
            "available": "true",
            "list": "tornado"
        }
    ]
}

EARTHQUAKE = {
    "earthquake": [
        {
            "id": "Bike helmet (to protect head from falling objects)",
            "name": "Bike helmet (to protect head from falling objects)",
            "available": "true",
            "list": "earthquake"
        },
        {
            "id": "Crowbar (to move debris/obstacle)",
            "name": "Crowbar (to move debris/obstacle)",
            "available": "true",
            "list": "earthquake"
        },
        {
            "id": "N95 masks (in-case trapped under debris)",
            "name": "N95 masks (in-case trapped under debris)",
            "available": "true",
            "list": "earthquake"
        }
    ]
}

WILDFIRE = {
    "wildfire": [
        {
            "id": "N95 masks (in-case poor air quality)",
            "name": "N95 masks (in-case poor air quality)",
            "available": "true",
            "list": "wildfire"
        },
        {
            "id": "Fire-resistant gloves",
            "name": "Fire-resistant gloves",
            "available": "true",
            "list": "wildfire"
        },
        {
            "id": "Fire-resistant clothing (cotton or wool, long sleeves & pants)",
            "name": "Fire-resistant clothing (cotton or wool, long sleeves & pants)",
            "available": "true",
            "list": "wildfire"
        },
        {
            "id": "Paper maps",
            "name": "Paper maps",
            "available": "true",
            "list": "wildfire"
        }
    ]
}

WINTERSTORM_BLIZZARD = {
    "winterstorm_blizzard": [
        {
            "id": "Extra blankets and sleeping bags",
            "name": "Extra blankets and sleeping bags",
            "available": "true",
            "list": "winterstorm_blizzard"
        },
        {
            "id": "Gas powered heat source",
            "name": "Gas powered heat source",
            "available": "true",
            "list": "winterstorm_blizzard"
        },
        {
            "id": "Hand warmers and thermal clothing",
            "name": "Hand warmers and thermal clothing",
            "available": "true",
            "list": "winterstorm_blizzard"
        },
        {
            "id": "Snow shovel and ice scraper (to move snow/obstacle)",
            "name": "Snow shovel and ice scraper (to move snow/obstacle)",
            "available": "true",
            "list": "winterstorm_blizzard"
        },
        {
            "id": "Jumper cables (for car)",
            "name": "Jumper cables (for car)",
            "available": "true",
            "list": "winterstorm_blizzard"
        },
        {
            "id": "Snow chains for tires (for car)",
            "name": "Snow chains for tires (for car)",
            "available": "true",
            "list": "winterstorm_blizzard"
        },
        {
            "id": "Tow rope (for car)",
            "name": "Tow rope (for car)",
            "available": "true",
            "list": "winterstorm_blizzard"
        }
    ]
}

IMPORTANT_NOT_URGENT = {
    "important_not_urgent": [
        {
            "id": "Can opener",
            "name": "Can opener",
            "available": "true",
            "list": "important_not_urgent"
        },
        {
            "id": "NOAA radio (for real-time weather updates)",
            "name": "NOAA radio (for real-time weather updates)",
            "available": "true",
            "list": "important_not_urgent"
        },
        {
            "id": "Whistle to signal for help",
            "name": "Whistle to signal for help",
            "available": "true",
            "list": "important_not_urgent"
        },
        {
            "id": "Personal sanitation",
            "name": "Personal sanitation",
            "available": "true",
            "list": "important_not_urgent"
        },
        {
            "id": "Non-sparking wrench or pliers to turn off utilities",
            "name": "Non-sparking wrench or pliers to turn off utilities",
            "available": "true",
            "list": "important_not_urgent"
        },
        {
            "id": "Local maps",
            "name": "Local maps",
            "available": "true",
            "list": "important_not_urgent"
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
