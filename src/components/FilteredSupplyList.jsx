const FilteredSupplyList = ({ mode, situParams, supplies, toggleSupplyAvail }) => {
    if (mode === null) {
        return null
    } else if (mode !== "disaster") {
        return <div></div> // currently unimplemented
    } else if (mode === "disaster") {
        return (
            <div>
                {supplies.map(supply =>
                <div key={supply.id}>
                    {supply.name} {supply.available ? "Available" : "Unavailable"}
                    <button onClick={() => toggleSupplyAvail(supply.id)}>Change availability (TODO)</button>
                </div>
                )}
            </div>
        )
    }
}

export default FilteredSupplyList
