import './App.css'
import React from 'react'
import Stats from './components/Stats'
import Health from './components/Health'
import BackgroundButton from './components/BackgroungButton'
import Clock from './components/Clock'

const App = () => {
  return (
    <div className='App'>
      <div className='bg-light' id='bg'>
        <h1>Kafka Project Dashboard</h1>
        <Stats />
        <Health />
        <div className='extra-features-wrapper'>
          <h2>EXTRA FEATURES</h2>
          <div className='extra-features'>
            <BackgroundButton initial_mode="bg-light"/>
            <Clock />
          </div>
        </div>
      </div>
      <footer className='app-bottom'></footer>
    </div>
  );
}

export default App
