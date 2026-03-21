document.addEventListener("DOMContentLoaded", () => {

    const deleteForms = document.querySelectorAll(".delete-form");

    deleteForms.forEach(form => {
        form.addEventListener("submit", (e) => {
            const confirmDelete = confirm("Are you sure you want to delete this post?");
            if (!confirmDelete) {
                e.preventDefault();
            }
        });
    });

});