// script.js

window.addEventListener('DOMContentLoaded', () => {
  // Bind popup openers
  document.querySelectorAll('[data-popup-trigger]').forEach(el => {
    el.addEventListener('click', openPopup);
  });

  // Trigger fade-in animations
  document.querySelectorAll('.fade-in.about, .fade-in.services').forEach(el => {
    el.style.animationName = 'fadeInUp';
    el.style.animationPlayState = 'running';
  });

  document.querySelectorAll('#why-list li').forEach((li, i) => {
    li.style.animationName = 'fadeInUp';
    li.style.animationDelay = `${i * 0.3 + 0.2}s`;
    li.style.animationPlayState = 'running';
  });
});

function openPopup() {
  const popup = document.getElementById('popup');
  popup.classList.add('active');
  document.body.style.overflow = 'hidden'; // Disable scroll behind popup
}

function closePopup() {
  const popup = document.getElementById('popup');
  popup.classList.remove('active');
  document.body.style.overflow = ''; // Restore scroll
}

// Close popup when clicking outside its content
document.addEventListener('click', e => {
  const popup = document.getElementById('popup');
  if (popup.classList.contains('active') && e.target === popup) {
    closePopup();
  }
});
