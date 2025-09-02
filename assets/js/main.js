// Main JavaScript file
document.addEventListener('DOMContentLoaded', function() {
  // Mobile menu toggle
  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');
  
  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', function() {
      const isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
      mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
      mobileMenu.classList.toggle('hidden');
    });
  }
});

// Lead tracking function
document.addEventListener('submit', (e) => {
  const f = e.target;
  if (f && f.id === 'lead-form' && window.dataLayer) {
    window.dataLayer.push({ event: 'generate_lead', method: 'contact_form' });
  }
});