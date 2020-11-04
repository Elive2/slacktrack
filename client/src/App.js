/*
  File: client/src/App.js

  Desctiprion:
  This component is the first component rendered when react attaches to index.html
*/

import logo from './logo.svg';
import GitLogo from './GitHub_Logo_White.png'
import './App.css';
import UserTable from './components/UserTable.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        SlackTrack
        <div id="GitLogo" >
          <a href="https://github.com/Elive2/slacktrack/" target="_blank">
            <img id="GitLogoImg" src={GitLogo}/>
          </a>
        </div>
      </header>
      <div id="centered-container">
        <UserTable/>
      </div>
    </div>
  );
}

export default App;
