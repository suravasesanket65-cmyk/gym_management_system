import React, { useState } from 'react';
import { useScrollReveal } from '../hooks/useScrollReveal';

export default function Contact() {
  const contactRef = useScrollReveal();

  const [formData, setFormData] = useState({
    fname: '',
    lname: '',
    email: '',
    phone: '',
    program: 'Strength Training',
    message: '',
  });

  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { id, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [id]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      setFormData({
        fname: '',
        lname: '',
        email: '',
        phone: '',
        program: 'Strength Training',
        message: '',
      });
    }, 4000);
  };

  return (
    <section id="contact-section" ref={contactRef}>
      <div className="wrap">
        <div className="section-head reveal">
          <div>
            <div className="eyebrow">Get Started</div>
            <h2 style={{ marginTop: '18px' }}>
              Walk In. Lift Once.<br />Decide For Yourself.
            </h2>
          </div>
          <p>
            First session is on us — bring shoes, water, and questions. We'll handle the rest.
          </p>
        </div>

        <div className="contact-grid reveal">
          <div className="contact-info">
            <div className="contact-info-item">
              <div className="ci-icon">📍</div>
              <div>
                <h4>Studio Address</h4>
                <p>Chinchwad, Pune, Maharashtra 411033</p>
              </div>
            </div>
            <div className="contact-info-item">
              <div className="ci-icon">📞</div>
              <div>
                <h4>Phone</h4>
                <p>+91 98765 43210</p>
              </div>
            </div>
            <div className="contact-info-item">
              <div className="ci-icon">✉️</div>
              <div>
                <h4>Email</h4>
                <p>hello@coresa.fit</p>
              </div>
            </div>
            <div style={{ marginTop: '32px' }}>
              <div className="hours-row">
                <span>Monday – Friday</span>
                <span>5:00 AM – 11:00 PM</span>
              </div>
              <div className="hours-row">
                <span>Saturday</span>
                <span>6:00 AM – 9:00 PM</span>
              </div>
              <div className="hours-row">
                <span>Sunday</span>
                <span>7:00 AM – 2:00 PM</span>
              </div>
            </div>
          </div>

          <form className="form-box" onSubmit={handleSubmit}>
            {submitted && (
              <div className="form-success-alert">
                🎉 Trial booked! We will reach out to you shortly to confirm your session.
              </div>
            )}
            <div className="form-row">
              <div>
                <label htmlFor="fname">First Name</label>
                <input
                  id="fname"
                  type="text"
                  placeholder="Sam"
                  value={formData.fname}
                  onChange={handleChange}
                  required
                />
              </div>
              <div>
                <label htmlFor="lname">Last Name</label>
                <input
                  id="lname"
                  type="text"
                  placeholder="Patil"
                  value={formData.lname}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>
            <div className="form-row">
              <div>
                <label htmlFor="email">Email</label>
                <input
                  id="email"
                  type="email"
                  placeholder="you@email.com"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </div>
              <div>
                <label htmlFor="phone">Phone</label>
                <input
                  id="phone"
                  type="tel"
                  placeholder="+91 00000 00000"
                  value={formData.phone}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>
            <label htmlFor="program">Interested Program</label>
            <select
              id="program"
              style={{ marginBottom: '16px' }}
              value={formData.program}
              onChange={handleChange}
            >
              <option value="Strength Training">Strength Training</option>
              <option value="HIIT & Metcon">HIIT &amp; Metcon</option>
              <option value="Boxing Conditioning">Boxing Conditioning</option>
              <option value="Yoga & Mobility">Yoga &amp; Mobility</option>
              <option value="CrossFit Style">CrossFit Style</option>
              <option value="Cardio Blast">Cardio Blast</option>
            </select>
            <label htmlFor="message">Message</label>
            <textarea
              id="message"
              placeholder="Tell us about your goal..."
              value={formData.message}
              onChange={handleChange}
            ></textarea>
            <button
              type="submit"
              className="btn btn-primary"
              style={{ width: '100%', justifyContent: 'center' }}
            >
              Book Free Trial
            </button>
          </form>
        </div>
      </div>
    </section>
  );
}
