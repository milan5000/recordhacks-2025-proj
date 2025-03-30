const FilteredSupplyList = ({ stage, mode, situParams, supplies, toggleSupplyAvail }) => {
    if (stage !== "checklist") return null;

    if (mode === null) {
        return null
    } else if (mode !== "disaster") {
        return <div></div> // currently unimplemented
    } else if (mode === "disaster") {
        let suppliesToReturn = structuredClone(supplies).filter((supply) => supply.list === 'essential')
        //console.log(suppliesToReturn)
        switch (situParams.disaster_type) {
            case "hurricane":
            case "flood":
                suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'hurricane_flood'))
                break;
            case "wildfire":
                suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'wildfire'))
                break;
            case "earthquake":
                suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'earthquake'))
                break;
            case "winter_storm":
                suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'winterstorm_blizzard'))
                break;
            case "tornado":
                suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'tornado'))
                break;
            default:
                break;
        }
        if (situParams.medical_needs) {
            suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'medical_needs'))
        }
        if (situParams.has_pets) {
            suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'pets'))
        }
        switch (situParams.time) {
            case "<1 day":
            case "<1 week":
            case "More than 1 week":
                suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'important_not_urgent'))
                break;
            default:
                break;
        }
        if (situParams.under5 > 0) {
            suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'infant'))
        }

        return (
            <div>
                {suppliesToReturn.map(supply =>
                <div key={supply.id}>
                    {supply.name} {supply.available ? "Available" : "Unavailable"}
                    <button onClick={() => toggleSupplyAvail(supply.id)}>Change availability (TODO)</button>
                </div>
                )}
                <p>{situParams.disaster_type}</p>
            </div>
        )
    }
}

export default FilteredSupplyList
