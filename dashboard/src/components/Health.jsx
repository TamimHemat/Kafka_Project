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
            <h2>Click to check servers Health Status</h2>
	        <button onClick={getHealth}>CHECK HEALTH</button>
            <div className="statuses">
                <p className='app-status'>Receiver Status: {event.receiver}</p>
	            <p className='app-status'>Storage Status: {event.storage}</p>
	            <p className='app-status'>Processing Status: {event.processing}</p>
	        </div>
	    </div>
    )
}

export default Health
