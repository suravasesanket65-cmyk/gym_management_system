import React from 'react';
import { useScrollReveal } from '../hooks/useScrollReveal';

export default function Hero() {
  const heroRef = useScrollReveal();

  const tickerItems = [
    '12+ Years Coaching',
    '1,400+ Active Members',
    '18 Certified Trainers',
    '24/7 Access',
    '6 Signature Programs',
    '4.9★ Member Rating',
  ];

  return (
    <section id="home" ref={heroRef}>
      <div className="wrap hero-inner">
        <div className="eyebrow">Pune's Strength &amp; Conditioning Studio</div>
        <h1>
          Train Hard.<br />
          Recover <em>Smart.</em><br />
          Repeat.
        </h1>
        <p className="hero-sub">
          CORESA is a performance gym built around real coaching, honest programming, and a floor that pushes you one rep past comfortable — every single day.
        </p>
        <div className="hero-cta">
          <a href="#contact-section" className="btn btn-primary">
            Start Free Trial
          </a>
          <a href="#program" className="btn btn-outline">
            View Programs
          </a>
        </div>
      </div>

      {/* Marquee Ticker */}
      <div className="ticker">
        <div className="ticker-track">
          <span>
            {tickerItems.map((item, idx) => (
              <span key={`t1-${idx}`}>{item}</span>
            ))}
          </span>
          <span>
            {tickerItems.map((item, idx) => (
              <span key={`t2-${idx}`}>{item}</span>
            ))}
          </span>
        </div>
      </div>
    </section>
  );
}
