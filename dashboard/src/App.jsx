import './App.css'
import React from 'react'
import Stats from './components/Stats'
import Health from './components/Health'
import BackgroundButton from './components/BackgroungButton'

const App = () => {
  return (
    <div className='App'>
      <div className='bg-light' id='bg'>
        <h1>Kafka Project Dashboard</h1>
        <Stats />
        <Health />
        <BackgroundButton initial_mode="bg-light"/>
      </div>
    </div>
  );
}

export default App
