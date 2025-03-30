const SituationSelect = ({ stage, mode, situParams, editParam }) => {
    if (stage !== "user_setup") return null;

    const handleAgeGroupChange = (field, value) => {
        const num = parseInt(value) || 0;
        editParam(field, num);
    };

    if (mode !== "disaster") return null;

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
                </div>
                
                <br />
                <label>
                    Time Frame:
                    <select value={situParams.time} onChange={(e) => editParam("time", e.target.value)}>
                        <option value="">Select</option>
                        <option value="<10 min">10 min</option>
                        <option value="<30 min">30 min</option>
                        <option value="<1 hour">1 hour</option>
                        <option value="<1 day">1 day</option>
                        <option value="<1 week">1 day</option>
                        <option value="More than 1 week">More than 1 week</option>
                    </select>
                </label>
            </div>
            <br />

            <h3 class="immediate_subheader">👪 Household Members by Age Group</h3>
            <div class="immediate_dropdowns">
                <label>
                    Under 5 years old:
                    <input
                        type="number"
                        min="0"
                        value={situParams.under5 || 0}
                        onChange={(e) => handleAgeGroupChange("under5", e.target.value)}
                    />
                </label>
                <br />

                <label>
                    Under 18 years old:
                    <input
                        type="number"
                        min="0"
                        value={situParams.under18 || 0}
                        onChange={(e) => handleAgeGroupChange("under18", e.target.value)}
                    />
                </label>
                <br />

                <label>
                    Over 18 years old:
                    <input
                        type="number"
                        min="0"
                        value={situParams.over18 || 0}
                        onChange={(e) => handleAgeGroupChange("over18", e.target.value)}
                    />
                </label>
                <br />
            </div>

            <h3 class="immediate_subheader">⚠️ Additional Considerations</h3>
            <div class="immediate_dropdowns">
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

                {/* <hr />
                <p>Current Input State:</p>
                <pre>{JSON.stringify(situParams, null, 2)}</pre> */}
            </div>
        </div>
    );
};

export default SituationSelect;
