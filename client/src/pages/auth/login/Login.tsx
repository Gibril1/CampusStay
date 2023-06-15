import Footer from "../../../components/footer/Footer";
import Navbar from "../../../components/navbar/Navbar";
import LoginImg from "../../../assets/Login.jpg";
import './Login.css'

const Login = () => {
  return (
    <>
      <Navbar />
      <div className="auth-page">
        <div className="container">
          <div className="login-container">
            <div className="login-image">
              <img src={LoginImg} alt="" />
            </div>
            <div className="login-form">
              <form action="">
                <div className="form-controller">
                  <label htmlFor="username">Username</label>
                  <input type="text" name="username" />
                </div>
                <div className="form-controller">
                  <label htmlFor="password">Password</label>
                  <input type="password" name="password" />
                </div>
              </form>
              <button className="btn bg-primary">Login</button>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default Login;
