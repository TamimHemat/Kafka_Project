import { useEffect, useState } from 'react'

// const Stats = () => {
//     const [event, setEvent] = useState([])

//     useEffect(() => {
//         fetch('http://localhost/processing/stats')
//         .then(res => res.json())
//         .then(res => { 
//             setEvent(res) 
//         })
//     }, [])

//     return (
//         <div className="stats">
//             <h2>Latest Statistics</h2>
//             <div className='events-stats-wrapper'>
//                 <div className='events-stats'>
//                     <div className='stats-params'>
//                         <p className='stats-param'>Number of Buys:</p>
//                         <p className='stats-param'>Number of Sells:</p>
//                         <p className='stats-param'>Max Buy Price:</p>
//                         <p className='stats-param'>Max Sell Price:</p>
//                         <p className='stats-param'>Last Updated:</p>
//                     </div>
//                     <div className='stats-values'>
//                         <p className='stats-value'>{event.num_buys}</p>
//                         <p className='stats-value'>{event.num_sells}</p>
//                         <p className='stats-value'>{event.max_buy_price}$</p>
//                         <p className='stats-value'>{event.max_sell_price}$</p>
//                         <p className='stats-value'>{event.last_updated}</p>
//                     </div>
//                 </div>
//             </div>    
//         </div>
//     )   
// }

const Stat = (props) => {
    const [event, setEvent] = useState([])
    const wanted_stat = props.stat_var

    useEffect(() => {
        fetch('http://localhost/processing/stats')
        .then(res => res.json())
        .then(res => { 
            setEvent(res) 
        })
    }, [])

    return (
        <div className="individual-stat">
            <div className='events-stats-wrapper'>
                <div className='events-stats'>
                    <div className='stats-params'>
                        <p className='stats-param'>{props.stat_name}:</p>
                    </div>
                    <div className='stats-values'>
                        <p className='stats-value'>{event[wanted_stat]}{props.dollar}</p>
                    </div>
                </div>
            </div>    
        </div>
    )   
}

export default Stat
