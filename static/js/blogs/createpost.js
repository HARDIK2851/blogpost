document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.querySelector('input[type="file"]');

    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const file = this.files[0];

            if (file) {
                const reader = new FileReader();

                reader.onload = function (e) {
                    let preview = document.querySelector(".image-preview");

                    if (!preview) {
                        preview = document.createElement("img");
                        preview.classList.add("image-preview");
                        fileInput.parentElement.appendChild(preview);
                    }

                    preview.src = e.target.result;
                };

                reader.readAsDataURL(file);
            }
        });
    }
});