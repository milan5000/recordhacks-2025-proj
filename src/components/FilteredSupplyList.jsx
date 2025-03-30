const FilteredSupplyList = ({ mode, situParams, supplies, toggleSupplyAvail }) => {
    if (mode === null) {
        return null
    } else if (mode !== "disaster") {
        return <div></div> // currently unimplemented
    } else if (mode === "disaster") {
        let suppliesToReturn = structuredClone(supplies).filter((supply) => supply.list === 'essential')
        //console.log(suppliesToReturn)
        if (situParams.disaster_type === "hurricane" || situParams.disaster_type === "flood") {
            //console.log("changed to hurrflood")
            suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'hurricane_flood'))
            //console.log(supplies.filter((supply) => supply.list === 'hurricane_flood'))
            //console.log(suppliesToReturn)
        } else if (situParams.disaster_type === "wildfire") {
            //console.log("changed to fire")
            suppliesToReturn.push(... supplies.filter((supply) => supply.list === 'wildfire'))
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
