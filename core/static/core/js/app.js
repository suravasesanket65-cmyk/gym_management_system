// sticky header
const header = document.getElementById('siteHeader');
if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
  });
}

// mobile menu
const burger = document.getElementById('burgerBtn');
const mobileMenu = document.getElementById('mobileMenu');
const mobileClose = document.getElementById('mobileClose');

if (burger && mobileMenu) {
  burger.addEventListener('click', () => mobileMenu.classList.add('open'));
}

if (mobileClose && mobileMenu) {
  mobileClose.addEventListener('click', () => mobileMenu.classList.remove('open'));
}

if (mobileMenu) {
  mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobileMenu.classList.remove('open')));
}

// scroll reveal
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in');
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });
revealEls.forEach(el => io.observe(el));

// active nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');
if (sections.length && navLinks.length) {
  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(sec => {
      const top = sec.offsetTop - 120;
      if (window.scrollY >= top) current = sec.getAttribute('id');
    });
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === '#' + current);
    });
  });
}
