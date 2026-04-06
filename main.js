document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.navbar');

    // Premium Navbar Scroll Effect
    const handleScroll = () => {
        if (window.scrollY > 20) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Initial check

    // Global AOS Animation Configuration
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            once: true,
            offset: 100,
            easing: 'ease-out-cubic',
            delay: 100
        });
    }

    // Refresh AOS on dynamic content changes (if any)
    window.addEventListener('load', () => {
        if (typeof AOS !== 'undefined') {
            AOS.refresh();
        }
    });
});
