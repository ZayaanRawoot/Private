

// Fade in animation for about and services sections on load
window.addEventListener('DOMContentLoaded', () => {
    const about = document.querySelector('.fade-in.about');
    const services = document.querySelector('.fade-in.services');
    if (about) {
        about.style.animationPlayState = 'running';
        about.style.animationName = 'fadeInUp';
    }
    if (services) {
        services.style.animationPlayState = 'running';
        services.style.animationName = 'fadeInUp';
    }

    // Fade in Why Choose Us li items one by one
    const whyItems = document.querySelectorAll('#why-list li');
    whyItems.forEach((li, i) => {
        li.style.animationName = 'fadeInUp';
        li.style.animationDelay = `${i * 0.3 + 0.2}s`;
        li.style.animationPlayState = 'running';
    });
});

// Popup open and close functions
function openPopup() {
    document.getElementById('popup').style.display = 'flex';
    document.body.style.overflow = 'hidden'; // prevent background scroll
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
    document.body.style.overflow = ''; // restore scroll
}

// Close popup on clicking outside the popup box
document.getElementById('popup').addEventListener('click', (e) => {
    if (e.target === e.currentTarget) {
        closePopup();
    }
});
