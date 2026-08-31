import React from 'react';
import { useScrollReveal } from '../hooks/useScrollReveal';

export default function About() {
  const aboutRef = useScrollReveal();

  const stats = [
    { value: '12+', label: 'Years Running' },
    { value: '1,400+', label: 'Members' },
    { value: '18', label: 'Coaches' },
  ];

  return (
    <section id="about" ref={aboutRef}>
      <div className="wrap about-grid">
        <div className="about-imgs reveal">
          <img
            className="about-img-main"
            src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=900&q=80"
            alt="Inside the CORESA training floor"
          />
          <img
            className="about-img-float"
            src="https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5?auto=format&fit=crop&w=500&q=80"
            alt="Free weights rack at CORESA"
          />
          <div className="about-badge">
            <span className="num">98%</span>
            <span className="lbl">
              Goal<br />Success
            </span>
          </div>
        </div>

        <div className="about-text reveal">
          <div className="eyebrow">Who We Are</div>
          <h2 style={{ fontSize: 'clamp(32px, 4.5vw, 48px)', margin: '18px 0 24px' }}>
            A Gym Built On<br />Coaching, Not Machines
          </h2>
          <p>
            CORESA started in 2013 as a single-room barbell club in Pune. Today it's a 12,000 sq. ft. facility, but the philosophy hasn't moved an inch: every member gets a real program, real feedback, and a coach who knows their name.
          </p>
          <p>
            We combine strength training, conditioning, and recovery science under one roof — so progress isn't guesswork, it's tracked, tested, and adjusted every four weeks.
          </p>
          <div className="about-stats">
            {stats.map((stat, idx) => (
              <div key={idx}>
                <strong>{stat.value}</strong>
                <span>{stat.label}</span>
              </div>
            ))}
          </div>
          <a href="#program" className="btn btn-primary">
            Explore Programs
          </a>
        </div>
      </div>
    </section>
  );
}
