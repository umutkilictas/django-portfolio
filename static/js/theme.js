/**
 * Tema Yönetimi (Açık / Koyu Tema)
 *
 * Bootstrap 5.3'ün yerleşik "data-bs-theme" özniteliğini kullanır.
 * İlk tema, <head> içindeki küçük script ile sayfa çizilmeden önce uygulanır;
 * bu dosya yalnızca tema butonunu ve ikonunu yönetir.
 */

(function () {
    const THEME_STORAGE_KEY = 'portfolio_theme';
    const htmlElement = document.documentElement;

    function currentTheme() {
        return htmlElement.getAttribute('data-bs-theme') === 'light' ? 'light' : 'dark';
    }

    // Buton, gidilecek temanın ikonunu gösterir (koyudayken güneş, açıktayken ay)
    function syncToggle(theme) {
        const btn = document.getElementById('themeToggleBtn');
        if (!btn) return;
        const sun = btn.querySelector('.icon-sun');
        const moon = btn.querySelector('.icon-moon');
        if (sun) sun.classList.toggle('d-none', theme !== 'dark');
        if (moon) moon.classList.toggle('d-none', theme !== 'light');
        const label = theme === 'dark' ? 'Açık temaya geç' : 'Koyu temaya geç';
        btn.setAttribute('aria-label', label);
        btn.setAttribute('title', label);
    }

    function applyTheme(theme) {
        htmlElement.setAttribute('data-bs-theme', theme);
        syncToggle(theme);
    }

    document.addEventListener('DOMContentLoaded', function () {
        syncToggle(currentTheme());

        const toggleBtn = document.getElementById('themeToggleBtn');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', function () {
                const nextTheme = currentTheme() === 'dark' ? 'light' : 'dark';
                applyTheme(nextTheme);
                try {
                    localStorage.setItem(THEME_STORAGE_KEY, nextTheme);
                } catch (e) {}
            });
        }
    });
})();
