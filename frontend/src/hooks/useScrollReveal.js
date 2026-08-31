import { useEffect, useRef } from 'react';

/**
 * Custom Hook: useScrollReveal
 * Translates IntersectionObserver logic into a reusable React Hook.
 * Attach the returned ref to a container element or an individual reveal element.
 * When elements with the `.reveal` class enter the viewport, the `.in` class is added.
 */
export function useScrollReveal(options = { threshold: 0.15 }) {
  const containerRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          observer.unobserve(entry.target);
        }
      });
    }, options);

    const el = containerRef.current;
    if (!el) return;

    // Observe the container itself if it has the 'reveal' class
    if (el.classList && el.classList.contains('reveal')) {
      observer.observe(el);
    }

    // Observe all nested elements with the 'reveal' class
    const revealChildren = el.querySelectorAll ? el.querySelectorAll('.reveal') : [];
    revealChildren.forEach((child) => observer.observe(child));

    return () => {
      if (el && el.classList && el.classList.contains('reveal')) {
        observer.unobserve(el);
      }
      revealChildren.forEach((child) => observer.unobserve(child));
    };
  }, [options.threshold]);

  return containerRef;
}
