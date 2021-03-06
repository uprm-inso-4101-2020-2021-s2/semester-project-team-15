import { useState } from 'react'
import { useForm } from 'react-hook-form'

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEye } from "@fortawesome/free-solid-svg-icons";

const Login = () => {

    const [s_email, setEmail]= useState('')
    const [s_password, setPassword]= useState('')

    const [hiddenPassword, setHiddenPassword] = useState(true)
    const toggleHiddenPassword = () => {
        setHiddenPassword(!hiddenPassword)
    }
    const eye = <FontAwesomeIcon icon = {faEye} />;

    const onSubmit = (e) => {
        e.preventDefault()
        if(!s_email) {
            alert('Please add your email')
            return
        }

        //onAdd({ name, email, password, passwordConfirmation })

        setEmail('')
        setPassword('')
    }

    return (
        <form className='add-form'>

            <div className='form-control'>
                <label>Email</label>
                <input type='text' 
                       placeholder='email'
                       name="email"
                       value={s_email}
                       onChange={(e) => setEmail(e.target.value)}/>
            </div>

            <div className='form-control'>
                <label>Password</label>
                <input 
                    type={hiddenPassword ? "password" : "text"} 
                    placeholder='password' 
                    name="password"
                    value={s_password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <i onClick={toggleHiddenPassword}> {eye} </i>{" "}
            </div>

            <input type='submit' value='Login'
            className='btn btn-block'/>
            
        </form>
    )
}

export default Login
