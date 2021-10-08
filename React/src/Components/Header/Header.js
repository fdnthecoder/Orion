import React from 'react'
import './Header.css'
import { NavLink} from 'react-router-dom'
import logoURL from '../../Assets/logo.png'

const Header = () => {
    return(
        <nav>
            <div className="header">
                <div>
                    <NavLink to='/' className="navLink"> <img src={logoURL} alt = "logo"/></NavLink>
                </div>
                <div>
                    <NavLink to='' className='navLink'>Companies</NavLink>
                </div>
                <div>
                    <NavLink to='' className='navLink'>Internships</NavLink>
                </div>
                <div>
                    <NavLink to='/login' className='navLink'>Login</NavLink>
                </div>
                <div>
                    <NavLink to='/profile' className='navLink'>Profile</NavLink>
                </div>
            </div>
        </nav>
    );
}

export default Header