document.addEventListener("DOMContentLoaded", () => {

const cards = document.querySelectorAll(".post-card");

cards.forEach(card => {

card.addEventListener("mouseenter", () => {
card.style.transform = "translateY(-3px)";
});

card.addEventListener("mouseleave", () => {
card.style.transform = "translateY(0)";
});

});

});