 // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Change navbar background on scroll
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('bg-dark');
                navbar.classList.add('shadow');
            } else {
                navbar.classList.remove('bg-dark');
                navbar.classList.remove('shadow');
            }
        });

        // Auto-dismiss alert after 5 seconds
        document.addEventListener('DOMContentLoaded', function() {
            var alert = document.getElementById('auto-dismiss-alert');
            if (alert) {
                // Use Bootstrap's built-in fade functionality
                setTimeout(function() {
                    var bsAlert = new bootstrap.Alert(alert);
                    bsAlert.close();
                }, 5000);
            }
        });