import { useState } from 'react'
import './App.css'
import Dartboard from './Dartboard'
import Game301 from './Game301'

function App() {
  const [game, setGame] = useState(null)
  const [players, setPlayers] = useState(['Anaïs', 'Guillaume'])

  return (
    <>
      <h1>Darts</h1>
      {game !== null && <h2>Jeu en cours : {game}</h2>}
      {game === null && <button onClick={() => setGame('301')}>Commencer la partie</button>}
      {game === '301' && <Game301 players={players} />}
    </>
  )
}

export default App
