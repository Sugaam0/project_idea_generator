document.addEventListener('DOMContentLoaded', () => {
            const form = document.querySelector('.fade-in');
            if (form) {
                form.style.opacity = '0';
                form.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    form.style.opacity = '1';
                    form.style.transform = 'translateY(0)';
                }, 100);
            }
        });

        document.addEventListener('DOMContentLoaded', () => {
        const elements = document.querySelectorAll('.pspark-fade-in');
        elements.forEach((el) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            setTimeout(() => {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, 100);
        });
    });

