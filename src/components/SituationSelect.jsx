const SituationSelect = ({ stage, mode, situParams, editParam }) => {
    const handleAgeGroupChange = (field, value) => {
        const num = parseInt(value) || 0;
        editParam(field, num);
    };

    if (mode === "disaster") {
        if (stage !== "user_setup") return null;

        console.log("Current input state:")
        console.log(JSON.stringify(situParams, null, 2));

        console.log("Current input state:")
        console.log(JSON.stringify(situParams, null, 2))

        return (
            <div class="immediate_div">
                <h3 class="immediate_subheader">🌪️ Emergency Situation</h3>
                <div class="immediate_dropdowns">
                    <div class="custom-select">
                        <label>
                            Type of Natural Disaster:
                            <select value={situParams.disaster_type} onChange={(e) => editParam("disaster_type", e.target.value)}>
                                <option value="">Select</option>
                                <option value="earthquake">Earthquake</option>
                                <option value="hurricane">Hurricane</option>
                                <option value="wildfire">Wildfire</option>
                                <option value="flood">Flood</option>
                                <option value="tornado">Tornado</option>
                                <option value="winter_storm">Winter Storm</option>
                            </select>
                        </label>
                        <br />
                        <label>
                            Time Frame:
                            <select value={situParams.time} onChange={(e) => editParam("time", e.target.value)}>
                                <option value="">Select</option>
                                <option value="<10 min">10 min</option>
                                <option value="<30 min">30 min</option>
                                <option value="<1 hour">1 hour</option>
                                <option value="<1 day">1 day</option>
                                <option value="<1 week">1 week</option>
                                <option value="More than 1 week">More than 1 week</option>
                            </select>
                        </label>
                    </div>
                    <br />

                    <h3 className="immediate_subheader">👪 Household Members by Age Group</h3>
                    <div className="immediate_dropdowns">
                        <label>
                            Under 5 years old:
                            <input class="number_input"
                                type="number"
                                min="0"
                                value={situParams.under5 || 0}
                                onChange={(e) => handleAgeGroupChange("under5", e.target.value)}
                            />
                        </label>
                        <br />

                        <label>
                            Under 13 years old:
                            <input class="number_input"
                                type="number"
                                min="0"
                                value={situParams.under13 || 0}
                                onChange={(e) => handleAgeGroupChange("under13", e.target.value)}
                            />
                        </label>
                        <br />

                        <label>
                            Under 18 years old:
                            <input class="number_input"
                                type="number"
                                min="0"
                                value={situParams.under18 || 0}
                                onChange={(e) => handleAgeGroupChange("under18", e.target.value)}
                            />
                        </label>
                        <br />

                        <label>
                            Over 18 years old:
                            <input class="number_input"
                                type="number"
                                min="0"
                                value={situParams.over18 || 0}
                                onChange={(e) => handleAgeGroupChange("over18", e.target.value)}
                            />
                        </label>
                        <br />
                    </div>

                    <h3 className="immediate_subheader">⚠️ Additional Considerations</h3>
                    <div className="immediate_dropdowns">
                        <label>
                            Medical Needs / Disabilities:
                            <select
                                value={situParams.medical_needs ? "yes" : "no"}
                                onChange={(e) => editParam("medical_needs", e.target.value === "yes")}
                            >
                                <option value="">Select</option>
                                <option value="yes">Yes</option>
                                <option value="no">No</option>
                            </select>
                        </label>
                        <br />

                        <label>
                            Pets:
                            <select
                                value={situParams.has_pets ? "yes" : "no"}
                                onChange={(e) => editParam("has_pets", e.target.value === "yes")}
                            >
                                <option value="">Select</option>
                                <option value="yes">Yes</option>
                                <option value="no">No</option>
                            </select>
                        </label>
                    </div>
                </div>
            </div>
        );
    } else if (mode === "education") {
        return (
            <div className="education_div section">
                <h3>🌀 Hurricanes – The Big Blow!</h3>
                <p>Hurricanes form over warm ocean waters and bring strong winds, rain, and flooding.</p>
                <ul>
                    <li>✅ Stock up on supplies early</li>
                    <li>🧳 Pack a hurricane kit</li>
                    <li>🏠 Know your safe space or evacuation route</li>
                    <li>💧 Keep important things dry</li>
                </ul>
                <p><em>💡 Did You Know?</em> The “eye” of a hurricane is calm — but only briefly!</p>

                <h3>🌪️ Tornadoes – The Spinning Trouble!</h3>
                <p>Tornadoes are fast columns of swirling wind that can destroy anything in their path.</p>
                <ul>
                    <li>🛑 Go to a basement or small interior room</li>
                    <li>👟 Wear sturdy shoes to avoid injury</li>
                    <li>📯 Keep a whistle in your kit</li>
                    <li>👨‍👩‍👧 Practice tornado drills</li>
                </ul>
                <p><em>💡 Did You Know?</em> Some tornadoes reach 200+ mph!</p>

                <h3>🌍 Earthquakes – The Ground Shaker!</h3>
                <p>Caused by tectonic shifts, earthquakes shake the ground and can damage buildings.</p>
                <ul>
                    <li>🙇‍♂️ Learn “Drop, Cover, and Hold On”</li>
                    <li>🪛 Secure heavy furniture</li>
                    <li>🎒 Keep an emergency kit ready</li>
                    <li>📍 Plan a family meeting spot</li>
                </ul>
                <p><em>💡 Did You Know?</em> Over 500,000 earthquakes happen globally each year!</p>

                <h3>🔥 Wildfires – Fire on the Move!</h3>
                <p>Wildfires spread rapidly through dry areas and can force evacuations.</p>
                <ul>
                    <li>🎒 Have a “go bag” near the door</li>
                    <li>🛣️ Plan two ways out</li>
                    <li>😷 Use a mask during smoke exposure</li>
                    <li>🍂 Clear dry brush around your home</li>
                </ul>
                <p><em>💡 Did You Know?</em> Some trees only release seeds after a fire!</p>

                <h3>❄️ Winter Storms – The Snowy Surprise!</h3>
                <p>These bring snow, ice, and freezing temps, often causing power outages.</p>
                <ul>
                    <li>🧥 Dress in warm layers</li>
                    <li>🔦 Keep flashlights and blankets ready</li>
                    <li>🚰 Fill water bottles early</li>
                    <li>🏠 Stay inside when conditions are dangerous</li>
                </ul>
                <p><em>💡 Did You Know?</em> The biggest snowflake ever was 15 inches wide!</p>
            </div>
        );
    }

    return null;
};

export default SituationSelect;
