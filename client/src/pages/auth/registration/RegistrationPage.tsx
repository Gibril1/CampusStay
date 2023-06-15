import Footer from "../../../components/footer/Footer";
import Navbar from "../../../components/navbar/Navbar";
import RestrationImg from "../../../assets/RegistrationImg.jpg";
import "./Registration.css";

const RegistrationPage = () => {
  return (
    <>
      <Navbar />
      <div className="auth-page">
        <div className="container">
          <div className="registration-container">
            <div className="auth-image">
              <img src={RestrationImg} alt="Registration Image" />
            </div>
            <div className="auth-form">
              <form action="">
                <div className="form-controller">
                  <label htmlFor="username">Username</label>
                  <input type="text" name="username" />
                </div>
                <div className="form-controller">
                  <label htmlFor="email">Email</label>
                  <input type="email" name="email" />
                </div>
                <div className="form-controller">
                  <label htmlFor="password">Password</label>
                  <input type="password" name="password" />
                </div>
                <div className="form-controller">
                  <label htmlFor="password2">Confirm Password</label>
                  <input type="password" name="password2" />
                </div>
                <div className="form-controller">
                  <label htmlFor="role">Role</label>
                  <select name="role" id="role">
                    <option value="Student">Student</option>
                    <option value="Manager">Manager</option>
                  </select>
                </div>
                <div className="form-controller">
                  <label htmlFor="firstName">First Name</label>
                  <input type="text" name="firstName" />
                </div>
                <div className="form-controller">
                  <label htmlFor="lastName">Last Name</label>
                  <input type="text" name="lastName" />
                </div>
                <div className="form-controller">
                  <label htmlFor="phone">Phone Number</label>
                  <input type="number" name="phone" />
                </div>
                <div className="form-controller">
                  <label htmlFor="gender">Gender</label>
                  <input type="text" name="gender" />
                </div>
              </form>
              <button className="btn bg-primary">Register</button>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default RegistrationPage;
