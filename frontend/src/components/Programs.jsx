import React from 'react';
import { useScrollReveal } from '../hooks/useScrollReveal';

const programsData = [
  {
    id: '01',
    tag: '01 · Strength',
    title: 'Strength Training',
    desc: 'Barbell-based programming to build raw, functional strength with progressive overload tracking.',
    img: 'https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=700&q=80',
    alt: 'Strength training program',
  },
  {
    id: '02',
    tag: '02 · Conditioning',
    title: 'HIIT & Metcon',
    desc: 'High-output interval circuits designed to burn fat and build engine capacity in 40 minutes flat.',
    img: 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=700&q=80',
    alt: 'HIIT conditioning program',
  },
  {
    id: '03',
    tag: '03 · Combat',
    title: 'Boxing Conditioning',
    desc: 'Pad work, bag rounds, and footwork drills that double as one of our hardest calorie burns.',
    img: 'https://images.unsplash.com/photo-1575052814086-f385e2e2ad1b?auto=format&fit=crop&w=700&q=80',
    alt: 'Boxing training program',
  },
  {
    id: '04',
    tag: '04 · Recovery',
    title: 'Yoga & Mobility',
    desc: 'Guided mobility flows and breathwork sessions to keep joints healthy under heavy load.',
    img: 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=700&q=80',
    alt: 'Yoga and mobility program',
  },
  {
    id: '05',
    tag: '05 · Functional',
    title: 'CrossFit Style',
    desc: 'Varied, high-intensity functional movements scaled to every level — from first-timers to competitors.',
    img: 'https://images.unsplash.com/photo-1526506118085-60ce8714f8c5?auto=format&fit=crop&w=700&q=80',
    alt: 'CrossFit functional training program',
  },
  {
    id: '06',
    tag: '06 · Endurance',
    title: 'Cardio Blast',
    desc: 'Treadmill, rower, and bike intervals structured around heart-rate zone training.',
    img: 'https://images.unsplash.com/photo-1571008887538-b36bb32f4571?auto=format&fit=crop&w=700&q=80',
    alt: 'Cardio training program',
  },
];

export default function Programs() {
  const programsRef = useScrollReveal();

  return (
    <section id="program" ref={programsRef}>
      <div className="wrap">
        <div className="section-head reveal">
          <div>
            <div className="eyebrow">What We Offer</div>
            <h2 style={{ marginTop: '18px' }}>Programs Built Around Your Goal</h2>
          </div>
          <p>
            Six focused tracks, each run by coaches who specialize in that discipline — pick one or stack them into a full week.
          </p>
        </div>

        <div className="program-grid reveal">
          {programsData.map((prog) => (
            <div className="program-card" key={prog.id}>
              <img src={prog.img} alt={prog.alt} />
              <div className="pc-body">
                <div className="program-tag">{prog.tag}</div>
                <h3>{prog.title}</h3>
                <p>{prog.desc}</p>
                <a href="#contact-section" className="program-link">
                  Join Program{' '}
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                    <path
                      d="M5 12h14M13 6l6 6-6 6"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                    />
                  </svg>
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
