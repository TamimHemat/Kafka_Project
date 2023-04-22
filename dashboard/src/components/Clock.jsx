import { useState, useEffect, useRef } from 'react';

const Clock = () => {
    const [time, setTime] = useState(new Date().toLocaleTimeString());
    const [dayDate, setDayDate] = useState(new Date().toString().split(' ').slice(0, 4).join(' '));
    const [display, setDisplay] = useState({
        display: 'none',
        text: 'Show Time'
    });

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

    const showTime = () => {
        if (display.display === 'none') {
            setDisplay({
                display: 'block',
                text: 'Hide Time'
            });
        } else {
            setDisplay({
                display: 'none',
                text: 'Show Time'
            });
        }
    }

    return (
        <div className='clock'>
            <div className='clock-button'>
                <button onClick={showTime}>{display.text}</button>
            </div>
            <h3 style={{ display : display.display}}>{dayDate} {time}</h3>
            <h3>Time passed since opening the page: </h3> 
            <div className='time-passed-wrapper'>
                <table className="time-passed-table">
                    <thead>
                        <tr>
                            <th className='time-passed-label'>Hours</th>
                            <th className='time-passed-label'>Minutes</th>
                            <th className='time-passed-label'>Seconds</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td className='time-passed'>{timePassed.current.hours}</td>
                            <td className='time-passed'>{timePassed.current.minutes}</td>
                            <td className='time-passed'>{timePassed.current.seconds}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Clock;