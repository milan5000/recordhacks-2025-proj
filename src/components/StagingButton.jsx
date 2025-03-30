const StagingButton = ({ stage, setStage, mode }) => {
    if (mode === null) {
        return null
    } else if (mode === "disaster") {
        if (stage === "user_setup") {
            return <button class="generate_button" onClick={() => setStage("checklist")}>Generate Personalized Supply List</button>
        } else if (stage === "checklist") {
            return <button class="generate_button" onClick={() => setStage("user_setup")}>Go Back to Setup</button>
        }
    } else {
        return null
    }
}

export default StagingButton;
