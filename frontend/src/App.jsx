import React from 'react';
import './styles/App.css';

import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Programs from './components/Programs';
import Trainers from './components/Trainers';
import Contact from './components/Contact';
import Footer from './components/Footer';

export default function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <About />
      <Programs />
      <Trainers />
      <Contact />
      <Footer />
    </>
  );
}
