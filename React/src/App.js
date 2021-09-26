import logo from './logo.png';
import './App.css';
//import React, { useEffect, useState } from 'react';
//import axios from 'axios'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h2>
          Orion
        </h2>
		<form className="App-login">
		  <div>
		  Username: 
		  <input type="text" defaultValue="Username" name="uname"/>
		  </div>
		  <div>
		  Password: 
		  <input type="text" name="pword"/>
		  </div>
		  <input type="submit" value="Submit"/>
		</form>
		<p id="test-div">
			This is where we will test our connection to the API
		</p>
		<button onclick="">
		  Change text!
		</button>
      </header>
    </div>
  );
}

export default App;
