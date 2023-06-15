import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/landingPage/LandingPage";
import RegistrationPage from './pages/auth/registration/RegistrationPage'
import Login from './pages/auth/login/Login'
import "./App.css";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="" element={<LandingPage />}></Route>
          <Route path="/register" element={<RegistrationPage />}></Route>
          <Route path="/login" element={<Login />}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
