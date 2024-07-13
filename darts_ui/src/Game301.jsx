import React, { useEffect, useState } from 'react';
import { getDart } from './mock';

function Game301(props) {
    const { players } = props

    const [currentPlayer, setCurrentPlayer] = useState(0);
    const [remianingDarts, setRemainingDarts] = useState(3);
    const [score, setScore] = useState([301, 301]);
    const [openDetails, setOpenDetails] = useState(false);
    const [darts, setDarts] = useState([]);
    const [openCorrectScore, setOpenCorrectScore] = useState(false);

    const nextPlayer = () => {
        setCurrentPlayer((currentPlayer + 1) % players.length)
        setRemainingDarts(3)

    }

    const getDartPoints = (dart) => {
        let points = dart.section
        if (dart.double) {
            points *= 2
        } else if (dart.triple) {
            points *= 3
        }
        return points
    }

    const onDart = (value) => {
        setDarts([...darts, { player: players[currentPlayer], value: value }])
        const newRemainingDarts = remianingDarts - 1
        setRemainingDarts(newRemainingDarts)
        if (newRemainingDarts === 0) {
            nextPlayer()
            setRemainingDarts(3)
        }
        setScore(score => {
            const newScore = [...score]
            newScore[currentPlayer] -= getDartPoints(value)
            return newScore
        }
        )
        
    }        


    
    return (
        <div className="two-columns">
            <div>
                <h2>Tableau des scores</h2>
                
                <table className='scoreboard'>
                    <thead>
                        <tr>
                            {players.map((player, index) => {
                                return <th key={index}>{player}</th>
                            })}
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            {score.map((playerScore, index) => {
                                return <td key={index}>{playerScore}</td>
                            })}
                        </tr>
                    </tbody>
                </table>

                <button className="button--sm" onClick={() => setOpenDetails(d => !d)}>Détail</button>
                {openDetails && <div className="popup--background">
                    <div className="popup--content">
                    <h3>Détail des scores</h3>
                    <h4>Historique des lancers</h4>
                    <p>Nombre de lancers : {darts.length}</p>
                    <p>10 dermiers lancers:</p>
                    <div className="dartsDetails">
                        {darts.map((dart, index) => {
                            if(index > darts.length - 10) {
                            return <div key={index}>{dart.player} : {dart.value.double ? 'double' : ''} {dart.value.triple ? 'triple' : ''} {dart.value.section}</div>
                            }

                        })}
                    </div>
                    <button className="button--sm" onClick={() => setOpenDetails(false)}>Fermer</button>
                    </div>
                    
                </div>}
            </div>
            <div>
                <h2>{players[currentPlayer]} joue</h2>
                <h3>Reste {remianingDarts} {remianingDarts > 1 ? 'fléchettes' : 'fléchette'}</h3>
                <button onClick={() => {
                    const dart = getDart()
                    onDart(dart)
                }}>Lancer</button>
                <button style={{marginLeft: '0.5rem'}} onClick={() => nextPlayer()}>Passer</button>
                <button style={{marginLeft: '0.5rem'}} onClick={() => setOpenCorrectScore(true)}>Corriger</button>
            </div>

            {openCorrectScore && <div className="popup--background">
                    <div className="popup--content">
                    <h3>Corriger le dernier lancer</h3>

                    <h4>Flèche détectée : {darts[darts.length - 1].value.double ? 'double' : ''} {darts[darts.length - 1].value.triple ? 'triple' : ''} {darts[darts.length - 1].value.section}</h4>
                    
                    <p>Lancée par : {darts[darts.length - 1].player}</p>

                    
                    <button className="button--sm" onClick={() => setOpenCorrectScore(false)}>Fermer</button>
                    </div>
                    
                </div>}

        </div>
    );
}

export default Game301;