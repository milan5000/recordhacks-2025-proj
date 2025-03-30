import { useState, useEffect } from 'react'

const App = () => {
  const [supplies, setSupplies] = useState([
    {
      id: 1,
      name: 'Canned Food',
      available: true
    },
    {
      id: 2,
      name: 'Bottled Water',
      available: true
    },
    {
      id: 3,
      name: '$25-100 or more',
      available: true
    }
  ])
  const [avail, setAvail] = useState({
    water: true,
    food: true,
    first_aid_kit: true
  })

  return (
    <div>
      <h1>PackAdvisor</h1>
      <div>
        {supplies.map(supply =>
          <div key={supply.id}>
            {supply.name} {supply.available ? "Available" : "Unavailable"}
            <button>Change availability (TODO)</button>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
