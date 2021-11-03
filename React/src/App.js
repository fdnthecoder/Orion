import React from 'react';
import './App.css';
import {Switch, Route} from 'react-router-dom';
import Header from './Components/Header/Header';
import Login from './Pages/Login/Login';
import Profile from './Pages/Profile/Profile';
import {Test} from "./Components/Test/Test"
import { useEffect, useState } from 'react';
//import axios from 'axios'

function App() {
	const [state, setState] = useState({})

	useEffect(() => {
		fetch("/hello").then(response => {
			if (response.status == 200){
				return response.json()
			}
		}).then(data => setState(data))
		.then(error => console.log(error))
	},[])

	return (
		<div className="App">

			<Test prop={state}/>
			<Header />
			<Switch>
				<Route path='/login' component={Login}/>
				<Route path='/profile' component={Profile}/>
				<Route exact path='/' render={() => <h1><Test prop={state}/></h1>}/>
			</Switch>
		</div>
	);
}

//<Route path='/login' render={() =><h1>Hello Gang</h1>}/>
export default App;