import { useState, useEffect } from 'react';

const BackgroundButton = (props) => {
    const [bg, setBg] = useState([props.initial_mode]);

    const changeBg = () => {
        if (bg === 'bg-dark') {
            setBg('bg-light');
        } else {
            setBg('bg-dark');
        }
    };

    useEffect(() => {
        document.getElementById("root").className = bg;
    }, [bg]);

    return (
        <div className='background-button-wrapper'>
            <h3>Current background mode: {bg}</h3>
            <div className="background-button">
                <button onClick={changeBg}>Change Background</button>
            </div>
        </div>
    );
};

export default BackgroundButton;