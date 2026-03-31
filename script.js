// Typing effect
const typedSpan = document.getElementById("typed");
const roles = ["AI/ML Engineer", "Full Stack Developer"];
let idx = 0, charIdx = 0;
let isDeleting = false;

function typeEffect() {
    const currentWord = roles[idx];
    if(isDeleting) charIdx--; else charIdx++;
    typedSpan.textContent = currentWord.substring(0, charIdx);
    
    let speed = isDeleting ? 50 : 100;
    if(!isDeleting && charIdx === currentWord.length) { speed = 2000; isDeleting = true; }
    else if(isDeleting && charIdx === 0) { isDeleting = false; idx = (idx + 1) % roles.length; speed = 500; }
    setTimeout(typeEffect, speed);
}
document.addEventListener("DOMContentLoaded", typeEffect);

// Scroll reveal
function reveal() {
    document.querySelectorAll(".reveal").forEach(el => {
        if(el.getBoundingClientRect().top < window.innerHeight - 100) el.classList.add("active");
    });
}
window.addEventListener("scroll", reveal);
reveal();

// Mobile Nav
document.getElementById("mobile-btn").addEventListener("click", () => document.getElementById("sidebar").classList.toggle("show"));

// Active section link highlighting
const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-link");
window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach(sec => { if(scrollY >= sec.offsetTop - 150) current = sec.getAttribute("id"); });
    navLinks.forEach(link => {
        link.classList.remove("active");
        if(link.getAttribute("href").includes(current)) link.classList.add("active");
    });
});

// Experience Intersection Observer
const expItems = document.querySelectorAll('.t-item');
const observerOptions = {
    threshold: 0.4,
    rootMargin: "-10% 0px -10% 0px"
};

const expObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        } else {
            entry.target.classList.remove('active');
        }
    });
}, observerOptions);

expItems.forEach(item => expObserver.observe(item));

// Contact Form Handling
const contactForm = document.getElementById('contact-form');
const formStatus = document.getElementById('form-status');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Simple client-side simulation
        const formData = new FormData(contactForm);
        const name = formData.get('name');
        
        // Visual feedback
        contactForm.style.opacity = '0.5';
        contactForm.style.pointerEvents = 'none';
        
        setTimeout(() => {
            contactForm.classList.add('hidden');
            formStatus.classList.remove('hidden');
            console.log(`Message received from ${name}`);
        }, 800);
    });
}
