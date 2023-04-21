import { useState } from 'react';

const BackgroundButton = (props) => {
    const [bg, setBg] = useState([props.initial_mode]);

    const changeBg = () => {
        if (bg === 'bg-dark') {
            setBg('bg-light');
        } else {
            setBg('bg-dark');
        }
    };

    return (
        <div className='background-button-wrapper'>
            <h2>Current background mode: {bg}</h2>
            <div className="background-button">
                <button onClick={changeBg}>Change Background</button>
            </div>
        </div>
    );
};

export default BackgroundButton;