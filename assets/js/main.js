/**
 * NusaGarden Landscape - Main JavaScript
 * Handles Navigation, Mobile Drawer, Sticky Header, FAQ Accordion, and Before-After Slider
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('is-open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
      const icon = mobileToggle.querySelector('svg');
      if (icon) {
        if (isOpen) {
          icon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>`;
        } else {
          icon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>`;
        }
      }
    });

    // Close on link click
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('is-open');
      });
    });
  }

  // 2. Sticky Header Shadow on Scroll
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('is-scrolled');
      } else {
        header.classList.remove('is-scrolled');
      }
    }, { passive: true });
  }

  // 3. FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const headerEl = item.querySelector('.faq-header');
    const contentEl = item.querySelector('.faq-content');

    if (headerEl && contentEl) {
      headerEl.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        // Close other items
        faqItems.forEach(otherItem => {
          if (otherItem !== item && otherItem.classList.contains('active')) {
            otherItem.classList.remove('active');
            const otherContent = otherItem.querySelector('.faq-content');
            if (otherContent) otherContent.style.maxHeight = null;
          }
        });

        // Toggle current item
        if (isActive) {
          item.classList.remove('active');
          contentEl.style.maxHeight = null;
        } else {
          item.classList.add('active');
          contentEl.style.maxHeight = contentEl.scrollHeight + 'px';
        }
      });
    }
  });

  // 4. Before-After Image Slider
  const baContainer = document.querySelector('.before-after-container');
  if (baContainer) {
    const beforeEl = baContainer.querySelector('.ba-before');
    const handleEl = baContainer.querySelector('.ba-slider-handle');
    let isDragging = false;

    const updateSlider = (clientX) => {
      const rect = baContainer.getBoundingClientRect();
      let offsetX = clientX - rect.left;
      if (offsetX < 0) offsetX = 0;
      if (offsetX > rect.width) offsetX = rect.width;

      const percentage = (offsetX / rect.width) * 100;
      beforeEl.style.width = `${percentage}%`;
      handleEl.style.left = `${percentage}%`;
    };

    const onPointerMove = (e) => {
      if (!isDragging) return;
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      updateSlider(clientX);
    };

    const stopDragging = () => {
      isDragging = false;
      window.removeEventListener('mousemove', onPointerMove);
      window.removeEventListener('touchmove', onPointerMove);
    };

    const startDragging = (e) => {
      isDragging = true;
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      updateSlider(clientX);
      window.addEventListener('mousemove', onPointerMove);
      window.addEventListener('touchmove', onPointerMove, { passive: true });
      window.addEventListener('mouseup', stopDragging, { once: true });
      window.addEventListener('touchend', stopDragging, { once: true });
    };

    baContainer.addEventListener('mousedown', startDragging);
    baContainer.addEventListener('touchstart', startDragging, { passive: true });
  }

  // 5. Contact Consultation Form (Sends data directly to WhatsApp)
  const contactForm = document.getElementById('consultationForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = contactForm.querySelector('#nama')?.value || '';
      const phone = contactForm.querySelector('#telepon')?.value || '';
      const city = contactForm.querySelector('#kota')?.value || '';
      const service = contactForm.querySelector('#jenis_layanan')?.value || '';
      const area = contactForm.querySelector('#luas_area')?.value || '-';
      const notes = contactForm.querySelector('#pesan')?.value || '';

      const waMessage = `Halo NusaGarden Landscape, saya ingin konsultasi pembuatan taman:\n\n` +
        `• *Nama:* ${name}\n` +
        `• *No. HP/WA:* ${phone}\n` +
        `• *Kota/Lokasi:* ${city}\n` +
        `• *Jenis Layanan:* ${service}\n` +
        `• *Perkiraan Luas Area:* ${area} m²\n` +
        `• *Catatan / Kebutuhan:* ${notes}\n\n` +
        `Mohon info estimasi jadwal survey dan konsultasi gratis. Terima kasih!`;

      const encoded = encodeURIComponent(waMessage);
      const waNumber = '6281234567890'; // Business WhatsApp
      window.open(`https://wa.me/${waNumber}?text=${encoded}`, '_blank');
    });
  }
});

