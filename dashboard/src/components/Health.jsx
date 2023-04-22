import { useState } from 'react'

const Health = () => {
    const [event, setEvent] = useState([])
    const [isFetching, setIsFetching] = useState('')

    const getHealth = async () => {
        setIsFetching('fetching');
        await fetch('http://localhost/health/check')
        .then(res => res.json())
        .then(res => {
            setEvent(res)
            setIsFetching('fetched');
        })
    }

    return (
        <div className='health'>
            <h2>Click the button below to check the health status of the servers</h2>
	        <button className='health-button' onClick={getHealth}>CHECK HEALTH</button>
            {isFetching === 'fetching' && <h4 className='fetching' style={{ textDecoration : 'underline' }}>
                Fetching health statuses - Please wait...
            </h4>}
            {isFetching === 'fetched' &&
            <div className='app-statuses'>
                <table className="app-statuses-table">
                    <thead>
                        <tr>
                            <th className='app-status-label'>Receiver Status</th>
                            <th className='app-status-label'>Storage Status</th>
                            <th className='app-status-label'>Processing Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td className='app-status'>{event.receiver}</td>
                            <td className='app-status'>{event.storage}</td>
                            <td className='app-status'>{event.processing}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            }
	    </div>
    )
}

export default Health
