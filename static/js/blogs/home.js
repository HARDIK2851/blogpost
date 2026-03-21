document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".post-card");

    cards.forEach(card => {

        card.addEventListener("click", (e) => {

            // Prevent double navigation if clicking link
            if (e.target.tagName.toLowerCase() === "a") return;

            const url = card.getAttribute("data-url");
            window.location.href = url;
        });

    });

});