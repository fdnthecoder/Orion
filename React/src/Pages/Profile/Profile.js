import React from 'react'
import './Profile.css'
import logoURL from '../../Assets/defaultProfilePic.png'

class Profile extends React.Component{
    render(){
        return(
            <div className=".profile-body">
                <div className=".profile-photo">
                    <img src={logoURL} alt = "logo"/>
                </div>
                <h1>Hello world!</h1>
            </div>
        );
    }
}

export default Profile;