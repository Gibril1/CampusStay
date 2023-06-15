import './Navbar.css'
import { useNavigate } from 'react-router-dom'
const Navbar = () => {
  const navigate = useNavigate()

  const handleSignUpClick = ():void => {
    navigate('/register')
  }

  return (
    <div>
          <nav className="navbar bg-dark">
              <div className="container">
                  <div className="nav-items flexBetween">
                    <div className="logo">
                        <h1>RelState</h1>
                    </div>
                    <div className="flexBetween list">
                        <li>Home</li>
                        <li>About</li>
                        <li>Portfolio</li>
                    </div>
                    <div className='signUp'>
                        <button className="btn bg-primary" onClick={handleSignUpClick}>Sign Up</button>
                    </div>
                  </div>
              </div>
              
        </nav>
    </div>
  )
}

export default Navbar
