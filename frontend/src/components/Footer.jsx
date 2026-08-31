import React from 'react';

export default function Footer() {
  return (
    <footer>
      <div className="wrap">
        <div className="footer-top">
          <div>
            <a href="#home" className="logo">
              CORE<span>SA</span>
            </a>
            <p>
              A performance gym in Chinchwad, Pune built on real coaching, honest programming, and community over ego.
            </p>
            <div className="footer-social">
              <a href="#" aria-label="Instagram">
                IG
              </a>
              <a href="#" aria-label="Facebook">
                FB
              </a>
              <a href="#" aria-label="YouTube">
                YT
              </a>
            </div>
          </div>
          <div className="footer-col">
            <h4>Navigate</h4>
            <ul>
              <li>
                <a href="#home">Home</a>
              </li>
              <li>
                <a href="#about">About</a>
              </li>
              <li>
                <a href="#program">Program</a>
              </li>
              <li>
                <a href="#trainer">Trainer</a>
              </li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>Programs</h4>
            <ul>
              <li>
                <a href="#program">Strength Training</a>
              </li>
              <li>
                <a href="#program">HIIT &amp; Metcon</a>
              </li>
              <li>
                <a href="#program">Boxing</a>
              </li>
              <li>
                <a href="#program">Yoga &amp; Mobility</a>
              </li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>Studio</h4>
            <ul>
              <li>Chinchwad, Pune, MH 411033</li>
              <li>+91 98765 43210</li>
              <li>hello@coresa.fit</li>
            </ul>
          </div>
        </div>
        <div className="footer-bottom">
          <span>© 2026 CORESA Fitness. All rights reserved.</span>
          <span>Design &amp; Build — Sanket Jadhav</span>
        </div>
      </div>
    </footer>
  );
}
