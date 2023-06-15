import "./Footer.css";
const Footer = () => {
  return (
    <div className="footer bg-dark">
      <div className="container">
        <div className="footer-container">
          <div className="footer-text">
            <p>
              Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sed,
              laudantium. Perferendis eos quae laborum ex.
            </p>
          </div>
          <div className="footer-contact">
            <label htmlFor="#">Contact Us</label>
            <div className="footer-contact-form">
              <input type="text" placeholder="Message..." />
              <button className="btn bg-primary">Send</button>
            </div>
          </div>
          <div className="footer-links">
            <li>Home</li>
            <li>About</li>
            <li>Contact</li>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
