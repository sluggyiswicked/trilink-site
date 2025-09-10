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

  // Smart submenu positioning - only flip to left when needed
  function setupSmartMenus() {
    const submenus = document.querySelectorAll('.dropdown-submenu');
    
    submenus.forEach(submenu => {
      submenu.addEventListener('mouseenter', function() {
        const submenuEl = this.querySelector('.dropdown-submenu-menu');
        if (!submenuEl) return;
        
        // Remove flip class first to check natural position
        submenuEl.classList.remove('flip-left');
        
        // Force display to calculate position
        setTimeout(() => {
          const rect = submenuEl.getBoundingClientRect();
          const viewportWidth = window.innerWidth;
          
          // If submenu would go off right edge, flip it to the left
          if (rect.right > viewportWidth - 10) {
            submenuEl.classList.add('flip-left');
          }
        }, 10); // Small delay to ensure menu is rendered
      });
      
      submenu.addEventListener('mouseleave', function() {
        const submenuEl = this.querySelector('.dropdown-submenu-menu');
        if (submenuEl) {
          submenuEl.classList.remove('flip-left');
        }
      });
    });
  }
  
  // Initialize smart menus
  setupSmartMenus();
  
  // Re-initialize on window resize
  window.addEventListener('resize', setupSmartMenus);
});

// Lead tracking function
document.addEventListener('submit', (e) => {
  const f = e.target;
  if (f && f.id === 'lead-form' && window.dataLayer) {
    window.dataLayer.push({ event: 'generate_lead', method: 'contact_form' });
  }
});