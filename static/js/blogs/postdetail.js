document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector("textarea");
    if (textarea) {
        textarea.placeholder = "Write your comment...";
    }

    document.querySelectorAll(".edit-btn").forEach(btn => {
        btn.addEventListener("click", function () {
            const id = this.dataset.id;
            document.getElementById(`edit-box-${id}`).style.display = "block";
            console.log('edit button clicked')
        });
    });

    // CANCEL BUTTON
    document.querySelectorAll(".cancel-btn").forEach(btn => {
        btn.addEventListener("click", function () {
            const id = this.dataset.id;
            document.getElementById(`edit-box-${id}`).style.display = "none";
        });
    });

    // SAVE BUTTON
    document.querySelectorAll(".save-btn").forEach(btn => {
        btn.addEventListener("click", function () {
            const id = this.dataset.id;
            const content = document.getElementById(`edit-input-${id}`).value;

            fetch(`/blogs/comment/${id}/edit/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `content=${encodeURIComponent(content)}`
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    document.getElementById(`text-${id}`).innerText = data.content;
                    document.getElementById(`edit-box-${id}`).style.display = "none";
                } else {
                    alert("Error updating comment");
                }
            });
        });
    });

});

function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}