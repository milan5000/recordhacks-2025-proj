const SituationSelect = ({ mode }) => {
    if (mode === null) {
        return null
    } else if (mode === "disaster") {
        return (
            <div>
                <p>Checkboxes here please</p>
            </div>
        )
    } else if (mode === "prepare") {
        return (
            <div>
                <p>Welcome to prep mode!</p>
            </div>
        )
    } else if (mode === "education") {
        return (
            <div>
                <p>Welcome to education mode!</p>
            </div>
        )
    } else { // unknown mode
        return null
    }
}

export default SituationSelect
