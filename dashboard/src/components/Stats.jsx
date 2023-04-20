import { useEffect, useState } from 'react'

const Stats = () => {
    const [event, setEvent] = useState([])

    useEffect(() => {
        fetch('http://localhost/processing/stats')
        .then(res => res.json())
        .then(res => { 
            setEvent(res) 
        })
    }, [])

    return (
        <div className="stats">
            <h2>Latest Statistics</h2>
            <div>
                <p className="single-stat">Max Buy Price: {event.max_buy_price}$</p>
	    	    <p className="single-stat">Max Sell Price: {event.max_sell_price}$</p>
                <p className="single-stat">Number of Buys: {event.num_buys}</p>
                <p className="single-stat">Number of Sells: {event.num_sells}</p>
            </div>
        </div>
    )   
}

export default Stats
