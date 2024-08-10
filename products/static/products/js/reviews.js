const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_description");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    let reviewDescription = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewDescription;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}