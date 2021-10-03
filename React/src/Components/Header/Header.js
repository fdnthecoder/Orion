import React from 'react'
import './Header.css'
import { NavLink, Link } from 'react-router-dom'
import logoURL from '../../Assets/logo.png'

const Header = () => {
    return(
        <nav>
            <div className="header">
                <div>
                    <NavLink to='/' className="navLink"><img src={logoURL}/></NavLink>
                </div>
                <div>
                    <NavLink to='' className='navLink'>Companies</NavLink>
                </div>
                <div>
                    <NavLink to='' className='navLink'>Interships</NavLink>
                </div>
                <div>
                    <NavLink to='/login' className='navLink'>Login</NavLink>
                </div>
            </div>
        </nav>
    );
}

export default Header