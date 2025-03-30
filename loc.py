@app.route('/location-hazards')
def get_hazards_by_location():
    from flask import request, jsonify
    import requests

    lat = request.args.get("lat")
    lon = request.args.get("lon")

    geo_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}"
    geo_res = requests.get(geo_url).json()
    state = geo_res.get("address", {}).get("state", "Unknown")

    if state == "Unknown":
        return jsonify({"state": state, "disasters": ["Unable to detect state"]}), 400

    fema_url = f"https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries?$filter=state eq '{state}'"
    fema_res = requests.get(fema_url).json()

    type_count = {}
    for record in fema_res.get("DisasterDeclarationsSummaries", []):
        dtype = record.get("incidentType")
        if dtype:
            type_count[dtype] = type_count.get(dtype, 0) + 1

    sorted_disasters = sorted(type_count.items(), key=lambda x: x[1], reverse=True)
    top_disasters = [item[0] for item in sorted_disasters[:3]]

    return jsonify({"state": state, "disasters": top_disasters})
