import React from 'react';
import './App.css';
import {Switch, Route} from 'react-router-dom';
//import Header from './Components/Header/Header';
import Login from './Pages/Login/Login';
import Profile from './Pages/Profile/Profile';
import { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
	const [getMessage, setGetMessage] = useState({})
  
	useEffect(()=>{
	  axios.get('https://react-flask-tutorial.herokuapp.com/flask/hello').then(response => {
		console.log("SUCCESS", response)
		setGetMessage(response)
	  }).catch(error => {
		console.log(error)
	  })
	}, [])
	return (
		<div className="App">
			<header className="App-header">
				<p>React + Flask Tutorial</p>
				<div>{getMessage.status === 200 ? 
				<h3>{getMessage.data.message}</h3>
				:
  				<h3>LOADING</h3>}</div>
			</header>

			<Switch>
				<Route path='/login' component={Login}/>
				<Route path='/profile' component={Profile}/>
				<Route exact path='/' render={() => <h1>Hello Gang!</h1>}/>
			</Switch>
		</div>
	);
}

//<Route path='/login' render={() =><h1>Hello Gang</h1>}/>
export default App;