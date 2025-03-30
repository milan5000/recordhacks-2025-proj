const StagingButton = ({ stage, setStage, mode }) => {
    if (mode === null) return null;
    if (stage === "user_setup") {
        return <button onClick={() => setStage("checklist")}>Generate Personalized Supply List</button>
    } else {
        return null
    }
}

export default StagingButton;
