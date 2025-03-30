const SituationSelect = ({ mode, situParams, editParam }) => {
    const handleAgeGroupChange = (field, value) => {
        const num = parseInt(value) || 0;
        editParam(field, num);
    };

    if (mode !== "disaster") return null;

    console.log("Current input state:")
    console.log(JSON.stringify(situParams, null, 2))

    return (
        <div>
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
                    <option value="<1 week">1 day</option>
                    <option value="More than 1 week">More than 1 week</option>
                </select>
            </label>
            <br />

            <h4>Household Members by Age Group</h4>

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
                Under 13 years old:
                <input
                    type="number"
                    min="0"
                    value={situParams.under13 || 0}
                    onChange={(e) => handleAgeGroupChange("under13", e.target.value)}
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
    );
};

export default SituationSelect;
