import { useState } from 'react'

const Health = () => {
    const [event, setEvent] = useState([])

    const getHealth = async () => {
        await fetch('http://localhost/health/check')
        .then(res => res.json())
        .then(res => {
            setEvent(res)
        })
    }

    return (
        <div className="health">
            <h2>Click the button below to check the health status of the servers</h2>
	        <button onClick={getHealth}>CHECK HEALTH</button>
            <div className='app-statuses'>
                <table className="app-statuses-table">
                    <tr>
                        <th className='app-status-label'>Receiver Status</th>
                        <th className='app-status-label'>Storage Status</th>
                        <th className='app-status-label'>Processing Status</th>
                    </tr>
                    <tr>
                        <td className='app-status'>{event.receiver}</td>
                        <td className='app-status'>{event.storage}</td>
                        <td className='app-status'>{event.processing}</td>
                    </tr>
                </table>
            </div>
	    </div>
    )
}

export default Health
