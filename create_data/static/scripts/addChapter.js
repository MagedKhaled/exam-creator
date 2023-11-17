const removeChapter = function (e) {
  listChapters = listChapters.filter(
    (chapter) => chapter !== e.target.parentElement.children[0].value
  );
  e.target.parentElement.remove();
};
let listChapters = [];
const addChapter = function (e) {
  let originalElement = e.target.parentElement;
  if (originalElement.children[0].value.length > 2) {
    if (!listChapters.includes(originalElement.children[0].value)) {
      originalElement.children[2].innerText = "";
      let cloneElement = originalElement.cloneNode(true);
      let parentContainer = document.getElementById("chapterContainer");
      originalInput = originalElement.children[0];
      originalButton = originalElement.children[1];

      originalButton.classList.remove("btn-success");
      originalButton.classList.add("btn-danger");
      originalButton.onclick = removeChapter;
      originalButton.innerText = "Cancel";
      originalInput.name = originalInput.value;

      listChapters.push(originalInput.value);
      cloneElement.children[0].value = "";
      parentContainer.appendChild(cloneElement);
    } else {
      originalElement.children[2].innerText = "This chapter is added before ";
    }
  } else {
    originalElement.children[2].innerText =
      "chapter name must be at least 3 characters ";
  }
};



