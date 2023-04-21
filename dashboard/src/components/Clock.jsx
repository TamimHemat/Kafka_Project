import { useState, useEffect, useRef } from 'react';

const Clock = () => {
    const [time, setTime] = useState(new Date().toLocaleTimeString());
    const [dayDate, setDayDate] = useState(new Date().toString().split(' ').slice(0, 4).join(' '));
    const timePassed = useRef({
        seconds: 0,
        minutes: 0,
        hours: 0,
    });

    useEffect(() => {
        const interval = setInterval(() => {
            setTime(new Date().toLocaleTimeString())
            setDayDate(new Date().toString().split(' ').slice(0, 4).join(' '));
            timePassed.current.seconds++;
            if (timePassed.current.seconds === 60) {
                timePassed.current.minutes++;
                timePassed.current.seconds = 0;
            }
            if (timePassed.current.minutes === 60) {
                timePassed.current.hours++;
                timePassed.current.minutes = 0;
            }
        }, 1000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className='clock'>
            <h2>Current time: {dayDate} {time}</h2>
            <h3>Time passed since opening the page: </h3> 
            {/* <span>
                {timePassed.current.hours} hours,{' '}
            </span>
            <span>
                {timePassed.current.minutes} minutes,{' '}
            </span>
            <span>
                {timePassed.current.seconds} seconds
            </span> */}
            <div className='time-passed-wrapper'>
                <table className="time-passed-table">
                    <tr>
                        <th className='time-passed-label'>Hours</th>
                        <th className='time-passed-label'>Minutes</th>
                        <th className='time-passed-label'>Seconds</th>
                    </tr>
                    <tr>
                        <td className='time-passed'>{timePassed.current.hours}</td>
                        <td className='time-passed'>{timePassed.current.minutes}</td>
                        <td className='time-passed'>{timePassed.current.seconds}</td>
                    </tr>
                </table>
            </div>
        </div>
    );
}

export default Clock;