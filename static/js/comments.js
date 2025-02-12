const editButtons = document.getElementsByClassName("btn-edit");
const userComment = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitBtn = document.getElementById("submitButton");


for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let commentNew = document.getElementById(`comment${commentId}`).innerText;
      userComment.value = commentNew;
      submitBtn.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }