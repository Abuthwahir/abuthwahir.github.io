// System Boot Sequence (Runs once per session)
const initBootSequence = () => {
    if (sessionStorage.getItem('system_booted') === 'true') return;

    const heroText = document.querySelector('.hero-text');
    if (!heroText) return;

    const originalGreeting = "Hello, World_";
    const originalName = "Abuthwahir H M";

    const greetingEl = heroText.querySelector('.greeting');
    const nameEl = heroText.querySelector('.name');
    const contentToHide = heroText.querySelectorAll('.title, .desc, .hero-btns');

    // Hide peripheral content initially
    contentToHide.forEach(el => el.style.opacity = '0');

    const chars = '!@#$%^&*()_+{}|:<>?~[]-=`';
    let iterations = 0;
    const maxIterations = 15; // Animation duration control

    // Create the glitch effect interval
    const scrambleInterval = setInterval(() => {
        // Scramble greeting
        greetingEl.textContent = ">>> LOADING_PROFILE" + ".".repeat(iterations % 4);

        // Scramble name with random chars matching length
        nameEl.textContent = originalName.split('').map((char, index) => {
            if (char === ' ') return ' ';
            // Progressively reveal actual characters
            if (index < (iterations / maxIterations) * originalName.length) {
                return originalName[index];
            }
            return chars[Math.floor(Math.random() * chars.length)];
        }).join('');

        iterations++;

        // End animation
        if (iterations > maxIterations) {
            clearInterval(scrambleInterval);
            greetingEl.textContent = originalGreeting;
            nameEl.textContent = originalName;

            // Fade peripheral content back in
            contentToHide.forEach(el => {
                el.style.transition = 'opacity 0.8s ease-in';
                el.style.opacity = '1';
            });

            sessionStorage.setItem('system_booted', 'true');
        }
    }, 60); // 60ms * 15 iterations = ~900ms duration
};

// Typing effect
const typedSpan = document.getElementById("typed");
const roles = ["AI/ML Engineer", "Full Stack Developer"];
let idx = 0, charIdx = 0;
let isDeleting = false;

function typeEffect() {
    const currentWord = roles[idx];
    if (isDeleting) charIdx--; else charIdx++;
    typedSpan.textContent = currentWord.substring(0, charIdx);

    let speed = isDeleting ? 50 : 100;
    if (!isDeleting && charIdx === currentWord.length) { speed = 2000; isDeleting = true; }
    else if (isDeleting && charIdx === 0) { isDeleting = false; idx = (idx + 1) % roles.length; speed = 500; }
    setTimeout(typeEffect, speed);
}
document.addEventListener("DOMContentLoaded", () => {
    initBootSequence();
    typeEffect();
});

// Scroll reveal
function reveal() {
    document.querySelectorAll(".reveal").forEach(el => {
        if (el.getBoundingClientRect().top < window.innerHeight - 100) el.classList.add("active");
    });
}
window.addEventListener("scroll", reveal);
reveal();

// Mobile Nav
const mobileBtn = document.getElementById("mobile-btn");
const sidebar = document.getElementById("sidebar");

if (mobileBtn && sidebar) {
    mobileBtn.addEventListener("click", () => sidebar.classList.toggle("show"));

    // Close sidebar when clicking on a link (on mobile)
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", () => {
            if (window.innerWidth <= 768) sidebar.classList.remove("show");
        });
    });

    // Close sidebar when clicking outside on mobile
    document.addEventListener("click", (e) => {
        if (window.innerWidth <= 768 &&
            sidebar.classList.contains("show") &&
            !sidebar.contains(e.target) &&
            !mobileBtn.contains(e.target)) {
            sidebar.classList.remove("show");
        }
    });
}

// Active section link highlighting
const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-link");
window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach(sec => { if (scrollY >= sec.offsetTop - 150) current = sec.getAttribute("id"); });
    navLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href").includes(current)) link.classList.add("active");
    });
});

// Experience and Focus Cards Intersection Observer
const expItems = document.querySelectorAll('.t-item, .focus-card');
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

// --- EmailJS INIT ---
(function () {
    emailjs.init("WVn1amxKA0i-b12Nk");
})();

const contactForm = document.getElementById('contact-form');
const submitBtn = document.getElementById('submit-btn');
const formStatus = document.getElementById('form-status');

if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const originalBtnHTML = 'RUN_CONTACT.sh <span class="terminal-arrow">▶</span>';

        submitBtn.disabled = true;
        submitBtn.innerText = 'TRANSMITTING...';
        formStatus.classList.add('hidden');

        // GET VALUES
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const message = document.getElementById('message').value;

        // --- EMAILJS SEND ---
        emailjs.send("service_r1zs8gx", "template_1csdxjf", {
            name: name,
            email: email,
            phone: phone,
            message: message
        })
            .then(() => {
                // SUCCESS
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHTML;

                formStatus.innerHTML = '<span class="text-neon">> MESSAGE_SENT_SUCCESSFULLY</span>';
                formStatus.classList.remove('hidden');

                contactForm.reset();
            })
            .catch((error) => {
                console.error("EmailJS ERROR:", error);

                // --- FALLBACK MAILTO ---
                const subject = encodeURIComponent(`Portfolio Contact from ${name}`);
                const body = encodeURIComponent(
                    `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\n\nMessage:\n${message}`
                );

                window.location.href = `mailto:hmabuthwahir@gmail.com?subject=${subject}&body=${body}`;

                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHTML;

                formStatus.innerHTML =
                    '<span style="color:#ff5f56;">> TRANSMISSION_FAILED - OPENING_MAIL_CLIENT</span>';
                formStatus.classList.remove('hidden');
            });
    });
}
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

// Topbar Interactive Panels
const settingsBtn = document.getElementById('settings-btn');
const settingsPane = document.getElementById('settings-pane');

function togglePanel(panel) {
    if (panel) {
        panel.classList.toggle('hidden');
    }
}

document.addEventListener('click', (e) => {
    // Toggle Settings
    if (settingsBtn && settingsBtn.contains(e.target)) {
        togglePanel(settingsPane);
    }
    // Close panels on click outside
    else {
        if (settingsPane && !settingsPane.contains(e.target)) {
            settingsPane.classList.add('hidden');
        }
    }
});

// Functional Toggles for Settings
const darkModeToggle = document.getElementById('dark-mode-toggle');
const hudToggle = document.getElementById('hud-toggle');

// Initialize Themes from LocalStorage
if (localStorage.getItem('theme') === 'light') {
    document.body.classList.add('light-mode');
    if (darkModeToggle) darkModeToggle.classList.add('active');
}

if (localStorage.getItem('hud') === 'active') {
    document.body.classList.add('hud-active');
    if (hudToggle) hudToggle.classList.add('active');
}

// Dark Mode Toggle Logic
if (darkModeToggle) {
    darkModeToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        const isLightMode = darkModeToggle.classList.toggle('active');
        if (isLightMode) {
            document.body.classList.add('light-mode');
            localStorage.setItem('theme', 'light');
        } else {
            document.body.classList.remove('light-mode');
            localStorage.setItem('theme', 'dark');
        }
    });
}

// Recruiter HUD Toggle Logic
if (hudToggle) {
    hudToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        const isActive = hudToggle.classList.toggle('active');
        if (isActive) {
            document.body.classList.add('hud-active');
            localStorage.setItem('hud', 'active');
        } else {
            document.body.classList.remove('hud-active');
            localStorage.setItem('hud', 'inactive');
        }
    });
}

// Hover/Click Flip-Card Logic
document.querySelectorAll('.project-flip').forEach(card => {
    let hoverTimer;

    card.addEventListener('click', function (e) {
        // Prevent flipping if interacting with a link/button specifically
        if (e.target.closest('a') || e.target.closest('button')) return;

        const isFlipped = this.classList.contains('flipped');

        // Remove 'flipped' from all cards
        document.querySelectorAll('.project-flip.flipped').forEach(f => f.classList.remove('flipped'));

        // Add 'flipped' back to clicked card only if it wasn't flipped initially
        if (!isFlipped) {
            this.classList.add('flipped');
        }
    });

    // Auto-Flip on prolonged Hover (Delay of 1.2s)
    card.addEventListener('mouseenter', function () {
        hoverTimer = setTimeout(() => {
            if (!this.classList.contains('flipped')) {
                // Remove flipped from all sibling cards to keep screen clean
                document.querySelectorAll('.project-flip.flipped').forEach(f => f.classList.remove('flipped'));
                this.classList.add('flipped');
            }
        }, 400);
    });

    card.addEventListener('mouseleave', function () {
        // Cancel the flip if they scrub the mouse out before the timer completes
        if (hoverTimer) clearTimeout(hoverTimer);
    });
});
