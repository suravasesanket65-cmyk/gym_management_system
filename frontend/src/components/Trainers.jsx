import React from 'react';
import { useScrollReveal } from '../hooks/useScrollReveal';

const trainersData = [
  {
    id: '1',
    name: 'Arjun Mehta',
    role: 'Head Strength Coach',
    img: 'https://images.unsplash.com/photo-1571731956672-f2b94d7dd0cb?auto=format&fit=crop&w=500&q=80',
    alt: 'Coach Arjun Mehta, head strength coach',
    socials: [
      { label: 'Instagram', text: 'IG', link: '#' },
      { label: 'LinkedIn', text: 'IN', link: '#' },
    ],
  },
  {
    id: '2',
    name: 'Priya Nair',
    role: 'HIIT & Conditioning',
    img: 'https://images.unsplash.com/photo-1548690312-e3b507d8c110?auto=format&fit=crop&w=500&q=80',
    alt: 'Coach Priya Nair, HIIT and conditioning coach',
    socials: [
      { label: 'Instagram', text: 'IG', link: '#' },
      { label: 'LinkedIn', text: 'IN', link: '#' },
    ],
  },
  {
    id: '3',
    name: 'Rohan Deshmukh',
    role: 'Boxing Coach',
    img: 'https://images.unsplash.com/photo-1567013127542-490d757e51fc?auto=format&fit=crop&w=500&q=80',
    alt: 'Coach Rohan Deshmukh, boxing coach',
    socials: [
      { label: 'Instagram', text: 'IG', link: '#' },
      { label: 'LinkedIn', text: 'IN', link: '#' },
    ],
  },
  {
    id: '4',
    name: 'Sana Sheikh',
    role: 'Mobility & Yoga',
    img: 'https://images.unsplash.com/photo-1594381898411-846e7d193883?auto=format&fit=crop&w=500&q=80',
    alt: 'Coach Sana Sheikh, mobility and yoga coach',
    socials: [
      { label: 'Instagram', text: 'IG', link: '#' },
      { label: 'LinkedIn', text: 'IN', link: '#' },
    ],
  },
];

export default function Trainers() {
  const trainersRef = useScrollReveal();

  return (
    <section id="trainer" ref={trainersRef}>
      <div className="wrap">
        <div className="section-head reveal">
          <div>
            <div className="eyebrow">Meet The Floor</div>
            <h2 style={{ marginTop: '18px' }}>
              Coaches Who Show Up<br />Every Rep With You
            </h2>
          </div>
          <p>
            Every CORESA coach is certified, still trains competitively, and carries a caseload small enough to actually know your form.
          </p>
        </div>

        <div className="trainer-grid reveal">
          {trainersData.map((trainer) => (
            <div className="trainer-card" key={trainer.id}>
              <div className="trainer-img">
                <img src={trainer.img} alt={trainer.alt} />
              </div>
              <div className="trainer-info">
                <h3>{trainer.name}</h3>
                <div className="trainer-role">{trainer.role}</div>
                <div className="trainer-social">
                  {trainer.socials.map((soc, sIdx) => (
                    <a key={sIdx} href={soc.link} aria-label={soc.label}>
                      {soc.text}
                    </a>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
