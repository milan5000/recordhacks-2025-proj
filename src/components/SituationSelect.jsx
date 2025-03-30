const SituationSelect = ({ mode, situParams, editParam }) => {
    if (mode === null) {
        return null
    } else if (mode === "disaster") {
        return (
            <div>
                <p>The impostor is {situParams.amogus}!</p>
                <button onClick={() => editParam("amogus", "not sus")}>click to make the impostor not sus</button>
                <button onClick={() => editParam("amogus", "sus")}>click to make the impostor sus</button>
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
