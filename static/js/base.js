document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".base-nav-link");

    links.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add("active");
        }
    });
});