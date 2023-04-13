import './App.css'
import Stats from './components/Stats'
import Health from './components/Health'

const App = () => {
  return (
    <div className="App">
      <h1>Dashboard</h1>
      <Stats />
      <Health />
    </div>
  );
}

export default App
