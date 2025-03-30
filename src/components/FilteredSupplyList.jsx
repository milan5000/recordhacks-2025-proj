const FilteredSupplyList = ({ mode, situParams }) => {
    if (mode === null) {
        return null
    } else if (mode !== disaster) {
        return <div></div> // currently unimplemented
    } else if (mode === disaster) {
        return (
            <div>
                
            </div>
        )
    }
}

export default FilteredSupplyList
