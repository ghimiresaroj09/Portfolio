document.addEventListener("DOMContentLoaded", () => {
    const menuIcon = document.getElementById("menu-icon");
    const navbar = document.querySelector(".navbar");

    menuIcon.addEventListener("click", () => {
        navbar.classList.toggle("active");
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const menuIcon = document.getElementById("menu-icon");
    const navbar = document.querySelector(".navbar");
    const typingElement = document.querySelector(".typing");
    const roles = ["Backend Developer", "Software Engineer", "IT Enthusiast"];
    let roleIndex = 0;
    let charIndex = 0;
    let currentRole = "";
    let isDeleting = false;

    menuIcon.addEventListener("click", () => {
        navbar.classList.toggle("active");
    });

    function type() {
        if (isDeleting) {
            currentRole = roles[roleIndex].substring(0, charIndex - 1);
            charIndex--;
        } else {
            currentRole = roles[roleIndex].substring(0, charIndex + 1);
            charIndex++;
        }

        typingElement.textContent = currentRole;

        if (!isDeleting && charIndex === roles[roleIndex].length) {
            isDeleting = true;
            setTimeout(type, 2000);
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            setTimeout(type, 500);
        } else {
            setTimeout(type, isDeleting ? 50 : 150);
        }
    }

    type();
});


document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".navbar a");

    window.addEventListener("scroll", function() {
        let current = "";

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= sectionTop - sectionHeight / 3) {
                current = section.getAttribute("id");
            }
        });

        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(current)) {
                link.classList.add("active");
            }
        });
    });
});
