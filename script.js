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

// EmailJS Initialization
(function() {
    // Replace with your real EmailJS Public Key
    emailjs.init("YOUR_PUBLIC_KEY");
})();

// Contact Scroll Observer (Premium Focus Swap)
const contactCards = document.querySelectorAll('.contact-card');
const contactObserverOptions = {
    threshold: 0.5,
    rootMargin: "-10% 0px -10% 0px"
};

const contactObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('focused');
        } else {
            entry.target.classList.remove('focused');
        }
    });
}, contactObserverOptions);

contactCards.forEach(card => contactObserver.observe(card));

// Refined EmailJS Form Handling
const contactForm = document.getElementById('contact-form');
const formStatus = document.getElementById('form-status');
const submitBtn = document.getElementById('submit-btn');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // UI Feedback: Loading State
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'TRANSMITTING... <span class="terminal-arrow">▶</span>';
        submitBtn.style.opacity = '0.7';
        
        // EmailJS sendForm: Replace SERVICE_ID and TEMPLATE_ID with your own
        emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', contactForm)
            .then(() => {
                // Success State
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'RUN_CONTACT.sh <span class="terminal-arrow">▶</span>';
                submitBtn.style.opacity = '1';
                contactForm.reset();
                alert("Transmission Successful 🚀");
            }, (error) => {
                // Error State
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'RETRY_TRANSMISSION.sh <span class="terminal-arrow">▶</span>';
                submitBtn.style.opacity = '1';
                console.error("Transmission Failed:", error);
                alert("Transmission Failed. Please check your EmailJS configuration or try again later.");
            });
    });
}

// Topbar Interactive Panels
const notifBtn = document.getElementById('notif-btn');
const settingsBtn = document.getElementById('settings-btn');
const notifDropdown = document.getElementById('notif-dropdown');
const settingsPane = document.getElementById('settings-pane');

function togglePanel(panel, otherPanel) {
    if (panel) {
        panel.classList.toggle('hidden');
        if (otherPanel) otherPanel.classList.add('hidden');
    }
}

document.addEventListener('click', (e) => {
    // Toggle Notifications
    if (notifBtn && notifBtn.contains(e.target)) {
        togglePanel(notifDropdown, settingsPane);
    } 
    // Toggle Settings
    else if (settingsBtn && settingsBtn.contains(e.target)) {
        togglePanel(settingsPane, notifDropdown);
    }
    // Close panels on click outside
    else {
        if (notifDropdown && !notifDropdown.contains(e.target)) {
            notifDropdown.classList.add('hidden');
        }
        if (settingsPane && !settingsPane.contains(e.target)) {
            settingsPane.classList.add('hidden');
        }
    }
});

// Settings Toggle Simulation
document.querySelectorAll('.toggle').forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevents closing the pane
        toggle.classList.toggle('active');
    });
});
