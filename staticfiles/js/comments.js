const editButtons = document.getElementsByClassName("btn-edit");
const userComment = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitBtn = document.getElementById("submitButton");
const CancelButtonModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteCommentButtons = document.getElementsByClassName("btn-delete");
const deleteConfirmModal = document.getElementById("deleteConfirm");


  /**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `editConfirm` link's href to point to the 
*  endpoint for the specific comment.
*/

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment_id");
      let commentNew = document.getElementById(`comment${commentId}`).innerText;
      userComment.value = commentNew;
      submitBtn.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }

  
  /**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

  for (let button of deleteCommentButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment_id");
      deleteConfirmModal.href = `delete_comment/${commentId}`;
      CancelButtonModal.show();
    });
  }
  
  