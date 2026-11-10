/**
 * Mobile Web Integration Module for Chinese Vocal HSK.
 * Provides touch optimizations, safe-area adaptation, and drawer/modal dismissals.
 */

(function () {
  'use strict';

  function isDrawerOrModalOpen() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar && sidebar.classList.contains('active')) return true;

    const overlay = document.getElementById('drawer-overlay');
    if (overlay && overlay.classList.contains('active')) return true;

    const modal = document.getElementById('shortcuts-modal');
    if (modal && modal.classList.contains('active')) return true;

    const chModal = document.getElementById('chapter-picker-modal');
    if (chModal && chModal.classList.contains('active')) return true;

    const anyDrawer = document.querySelector('.ankineitor-drawer.active');
    if (anyDrawer) return true;

    const anyModal = document.querySelector('.modal-wrap.active');
    if (anyModal) return true;

    return false;
  }

  function initMobileBackButton() {
    // Standard browser history popstate handling to dismiss open modals/drawers
    window.addEventListener('popstate', function () {
      if (isDrawerOrModalOpen() && window.App && typeof window.App.closeDrawers === 'function') {
        window.App.closeDrawers();
      }
    });
  }

  // Prevent unwanted double-tap zoom delay on mobile touch targets
  function initTouchOptimizations() {
    document.addEventListener('touchstart', function () {}, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initMobileBackButton();
      initTouchOptimizations();
    });
  } else {
    initMobileBackButton();
    initTouchOptimizations();
  }
})();
