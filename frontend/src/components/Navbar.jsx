import React, { useState, useEffect } from 'react';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileOpen, setIsMobileOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('home');

  useEffect(() => {
    const handleScroll = () => {
      // Sticky header state
      setIsScrolled(window.scrollY > 40);

      // Active nav link scroll-spy
      const sectionIds = ['home', 'about', 'program', 'trainer', 'contact-section'];
      let current = 'home';

      for (const id of sectionIds) {
        const section = document.getElementById(id);
        if (section) {
          const top = section.offsetTop - 130;
          if (window.scrollY >= top) {
            current = id;
          }
        }
      }
      setActiveSection(current);
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check

    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const toggleMobileMenu = () => {
    setIsMobileOpen((prev) => !prev);
  };

  const closeMobileMenu = () => {
    setIsMobileOpen(false);
  };

  return (
    <>
      <header id="siteHeader" className={isScrolled ? 'scrolled' : ''}>
        <div class="wrap">
          <nav>
            <a href="#home" className="logo" onClick={closeMobileMenu}>
              CORE<span>SA</span>
            </a>
            <ul className="nav-links">
              <li>
                <a href="#home" className={activeSection === 'home' ? 'active' : ''}>
                  Home
                </a>
              </li>
              <li>
                <a href="#about" className={activeSection === 'about' ? 'active' : ''}>
                  About
                </a>
              </li>
              <li>
                <a href="#program" className={activeSection === 'program' ? 'active' : ''}>
                  Program
                </a>
              </li>
              <li>
                <a href="#trainer" className={activeSection === 'trainer' ? 'active' : ''}>
                  Trainer
                </a>
              </li>
              <li>
                <a href="#contact-section" className={activeSection === 'contact-section' ? 'active' : ''}>
                  Contact
                </a>
              </li>
            </ul>
            <div className="nav-cta">
              <a href="#contact-section" className="btn btn-outline">
                Get In Touch
              </a>
              <button
                className="burger"
                id="burgerBtn"
                aria-label="Open menu"
                onClick={toggleMobileMenu}
              >
                <span></span>
                <span></span>
                <span></span>
              </button>
            </div>
          </nav>
        </div>
      </header>

      {/* Mobile Menu Drawer */}
      <div className={`mobile-menu ${isMobileOpen ? 'open' : ''}`} id="mobileMenu">
        <button
          className="mobile-close"
          id="mobileClose"
          aria-label="Close menu"
          onClick={closeMobileMenu}
        >
          ×
        </button>
        <a href="#home" onClick={closeMobileMenu}>
          Home
        </a>
        <a href="#about" onClick={closeMobileMenu}>
          About
        </a>
        <a href="#program" onClick={closeMobileMenu}>
          Program
        </a>
        <a href="#trainer" onClick={closeMobileMenu}>
          Trainer
        </a>
        <a href="#contact-section" onClick={closeMobileMenu}>
          Contact
        </a>
      </div>
    </>
  );
}
