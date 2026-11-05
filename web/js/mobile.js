/**
 * Mobile and Android Native Integration Module for Chinese Vocal HSK.
 * Provides Capacitor hardware back button interception, safe-area adaptation,
 * and seamless mobile app lifecycle management.
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

    return false;
  }

  function initMobileBackButton() {
    // Check if running in Capacitor environment
    if (window.Capacitor && window.Capacitor.Plugins && window.Capacitor.Plugins.App) {
      const CapApp = window.Capacitor.Plugins.App;
      CapApp.addListener('backButton', function (status) {
        if (isDrawerOrModalOpen()) {
          if (window.App && typeof window.App.closeDrawers === 'function') {
            window.App.closeDrawers();
          }
        } else {
          // If no modal is open and user presses back, minimize or exit
          if (status.canGoBack) {
            window.history.back();
          } else {
            CapApp.exitApp();
          }
        }
      });
    }

    // Standard browser popstate fallback
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
