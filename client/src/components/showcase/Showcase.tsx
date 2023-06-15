import Image from '../../assets/ShowcaseImg.jpg'
import './Showcase.css'

const Showcase = () => {
  return (
    <section className="showcase bg-dark">
        <div className="container">
          <div className="showcase-container">
          <div className="showcase-text">
            <h1>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ipsam, corporis voluptatem ullam quaerat esse debitis.</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem, rem.</p>
          </div>
          <div className="showcase-image">
              <img src={Image} alt="" />
          </div>
          <div className='showcase-text'>
            <p className='side-text'>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Fuga numquam fugiat molestiae, suscipit sequi unde odio quibusdam excepturi. Ullam fugiat nesciunt voluptate ipsa cumque minima iure aspernatur autem modi mollitia.</p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Showcase
