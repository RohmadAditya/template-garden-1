/**
 * NusaGarden Landscape - Portfolio Filter & Detail Modal
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Portfolio Category Filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  if (filterButtons.length > 0 && projectCards.length > 0) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        // Active class toggle
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filterCategory = btn.getAttribute('data-filter');

        projectCards.forEach(card => {
          const cardCategory = card.getAttribute('data-category');
          if (filterCategory === 'all' || cardCategory === filterCategory) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 2. Project Modal Details
  const modal = document.getElementById('projectModal');
  const modalImg = document.getElementById('modalImg');
  const modalTitle = document.getElementById('modalTitle');
  const modalCategory = document.getElementById('modalCategory');
  const modalLocation = document.getElementById('modalLocation');
  const modalArea = document.getElementById('modalArea');
  const modalDuration = document.getElementById('modalDuration');
  const modalDesc = document.getElementById('modalDesc');
  const modalCloseBtn = document.querySelector('.modal-close-btn');

  const openButtons = document.querySelectorAll('.project-view-btn');

  if (modal) {
    openButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const card = btn.closest('.project-card');
        if (!card) return;

        const title = card.querySelector('.project-title')?.textContent || '';
        const category = card.querySelector('.project-category-badge')?.textContent || '';
        const img = card.querySelector('.project-img-wrapper img')?.getAttribute('src') || '';
        const location = card.getAttribute('data-location') || 'Jabodetabek';
        const area = card.getAttribute('data-area') || '45 m²';
        const duration = card.getAttribute('data-duration') || '5 Hari';
        const desc = card.getAttribute('data-detail') || card.querySelector('.project-desc')?.textContent || '';

        if (modalImg) modalImg.src = img;
        if (modalTitle) modalTitle.textContent = title;
        if (modalCategory) modalCategory.textContent = category;
        if (modalLocation) modalLocation.textContent = location;
        if (modalArea) modalArea.textContent = area;
        if (modalDuration) modalDuration.textContent = duration;
        if (modalDesc) modalDesc.textContent = desc;

        modal.classList.add('is-open');
        document.body.style.overflow = 'hidden';
      });
    });

    const closeModal = () => {
      modal.classList.remove('is-open');
      document.body.style.overflow = '';
    };

    if (modalCloseBtn) {
      modalCloseBtn.addEventListener('click', closeModal);
    }

    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('is-open')) {
        closeModal();
      }
    });
  }
});

