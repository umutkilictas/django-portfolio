/**
 * Tema Yönetimi (Açık / Koyu Tema)
 * LocalStorage ve sistem tercihi destekli
 */

(function () {
    const THEME_STORAGE_KEY = 'portfolio_theme';
    const htmlElement = document.documentElement;

    // 1. Tercih edilen temayı belirle
    function getPreferredTheme() {
        const storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
        if (storedTheme) {
            return storedTheme;
        }
        // Sistem tercihini kontrol et
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return systemPrefersDark ? 'dark' : 'light';
    }

    // 2. Temayı sayfaya uygula
    function applyTheme(theme) {
        htmlElement.setAttribute('data-theme', theme);
        const iconSpan = document.getElementById('themeToggleIcon');
        if (iconSpan) {
            iconSpan.textContent = theme === 'dark' ? '🌙' : '☀️';
        }
    }

    // İlk yüklemede temayı hemen ayarla
    const currentTheme = getPreferredTheme();
    applyTheme(currentTheme);

    // DOM yüklendiğinde buton dinleyicisini bağla
    document.addEventListener('DOMContentLoaded', function () {
        const toggleBtn = document.getElementById('themeToggleBtn');
        const iconSpan = document.getElementById('themeToggleIcon');

        // İkonu mevcut temaya göre güncelle
        if (iconSpan) {
            iconSpan.textContent = htmlElement.getAttribute('data-theme') === 'dark' ? '🌙' : '☀️';
        }

        if (toggleBtn) {
            toggleBtn.addEventListener('click', function () {
                const activeTheme = htmlElement.getAttribute('data-theme');
                const nextTheme = activeTheme === 'dark' ? 'light' : 'dark';
                
                applyTheme(nextTheme);
                localStorage.setItem(THEME_STORAGE_KEY, nextTheme);
            });
        }
    });
})();
