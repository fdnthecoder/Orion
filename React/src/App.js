import React, {Component} from 'react';
import './App.css';
import {Switch, Route} from 'react-router-dom';
import Header from './Components/Header/Header';
import Login from './Pages/Login/Login';
//import React, { useEffect, useState } from 'react';
//import axios from 'axios'

class App extends Component{
	render(){
		return (
			<div className="App">
				<Header />
				<Switch>
					<Route path='/login' render={() =><h1>Hello Gang</h1>}/>
					<Route path='/' component={Login}/>
				</Switch>
			</div>
		);
	}
}

export default App;
