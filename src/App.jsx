import { useState, useEffect } from 'react'
import packingListService from './services/packinglist'
import SituationSelect from './components/SituationSelect'
import FilteredSupplyList from './components/FilteredSupplyList'

const App = () => {
  const [supplies, setSupplies] = useState([])
  const [avail, setAvail] = useState({
    water: true,
    food: true,
    first_aid_kit: true
  })
  const [situParams, setSituParams] = useState({
    disaster_type: null,
    amogus: "sus"
  })
  const [mode, setMode] = useState(null)

  useEffect(() => {
    packingListService
      .getAll()
      .then(initialSupplies => {
        console.log(initialSupplies['essential'])
        setSupplies(initialSupplies['essential'])
      })
  }, [])

  const editParam = (arg, val) => {
    console.log(`Setting ${arg} to ${val}`)
    const situClone = { ...situParams };
    situClone[arg] = val;
    setSituParams(situClone)
  }

  return (
    <div>
      <h1>PackAdvisor</h1>
      <div>
        <button onClick={() => {console.log("disaster"); setMode("disaster")}}>Immediate Disaster</button>
        <button onClick={() => {console.log("prepare"); setMode("prepare")}}>Non-Urgent Preparation</button>
        <button onClick={() => {console.log("education"); setMode("education")}}>Educational</button>
      </div>
      <SituationSelect mode={mode} situParams={situParams} editParam={editParam} />
      <FilteredSupplyList mode={mode} situParams={situParams} />
    </div>
  )
}

export default App
