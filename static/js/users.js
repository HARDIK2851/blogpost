// simple UI enhancement

document.addEventListener("DOMContentLoaded", () => {

    const button = document.querySelector(".primary");

    if (button) {
        button.addEventListener("mouseover", () => {
            button.style.transform = "translateY(-1px)";
        });

        button.addEventListener("mouseout", () => {
            button.style.transform = "translateY(0)";
        });
    }

});