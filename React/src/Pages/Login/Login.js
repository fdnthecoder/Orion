import React from 'react'
import logoURL from '../../Assets/logo.png'
import './Login.css'

class Login extends React.Component{
    render(){
        return(
            <div className="login-body">
                <div className="login-div">
                    <div>
                        <img src={logoURL} alt = "logo"/>
                    </div>
                    <div>
                        <form>
                            <input type='username' name='user' placeholder='username' required />
                            <input type='password' name='pwd' placeholder='password' required />
                            <button>
                                Login
                            </button>
                        </form>
                    </div>

                </div>
            </div>
        );
    }
}

export default Login;