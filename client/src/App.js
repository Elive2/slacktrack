import logo from './logo.svg';
import './App.css';
import UserTable from './components/UserTable.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        SlackTrack
      </header>
      <div id="centered-container">
        <UserTable/>
      </div>
    </div>
  );
}

export default App;
