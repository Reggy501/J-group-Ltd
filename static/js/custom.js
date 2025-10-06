// static/js/custom.js
document.addEventListener('DOMContentLoaded', function () {
    // Form validation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            const email = document.getElementById('email');
            const name = document.getElementById('name');
            const message = document.getElementById('message');
            if (!email.value.includes('@') || !name.value.trim() || !message.value.trim()) {
                e.preventDefault();
                alert('Please fill out all fields correctly.');
            }
        });
    }

    // Smooth scrolling for navbar links
    document.querySelectorAll('a.nav-link').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href.startsWith('/')) {
                e.preventDefault();
                window.scrollTo({ top: 0, behavior: 'smooth' });
                setTimeout(() => window.location.href = href, 500); // Navigate after scroll
            }
        });
    });

    // Ensure carousel auto-plays
    const carousel = document.querySelector('#homeCarousel');
    if (carousel) {
        new bootstrap.Carousel(carousel, {
            interval: 5000, // Auto-slide every 5 seconds
            wrap: true
        });
    }

    console.log("Jaspax site loaded");
});