const removeMessage = function () {
  const messageElement = document.getElementById("messageLabel");

  function changeContent() {
    messageElement.textContent = "";
  }
  setTimeout(changeContent, 10000);
};

if (window.location.href === "http://127.0.0.1:8000/create/question/") {
  removeMessage();
}

const removeAnswer = function (e) {
  listAnswers = listAnswers.filter(
    (question) => question !== e.target.parentElement.children[0].value
  );
  e.target.parentElement.remove();
};

let listAnswers = [];

const addAnswer = function (e) {
  const originalElement = e.target.parentElement;
  if (originalElement.children[0].value.length > 0) {
    if (!listAnswers.includes(originalElement.children[0].value)) {
      originalElement.children[2].innerText = "";

      const cloneElement = originalElement.cloneNode(true);

      const parentContainer = document.getElementById("wrong_answer_container");

      const originalInput = originalElement.children[0];
      const originalButton = originalElement.children[1];

      originalButton.classList.remove("btn-success");
      originalButton.classList.add("btn-danger");
      originalButton.onclick = removeAnswer;
      originalButton.innerText = "Cancel";
      originalInput.name = originalInput.value;

      listAnswers.push(originalInput.value);
      cloneElement.children[0].value = "";
      parentContainer.appendChild(cloneElement);
    } else {
      originalElement.children[2].innerText = "This chapter is added before ";
    }
  } else {
    originalElement.children[2].innerText =
      "chapter name must be at least 1 characters ";
  }
};

const chooseSubject = function (e) {
  subject = document.getElementById("subjectName").value;
  chapterSelect = document.getElementById("chapterName");

  url = `/create/get/chapters/${subject}/`;

  console.log("subject", subject);

  if (subject) {
    fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("Network response was not ok.");
      })
      .then((data) => {
        chapterSelect.innerHTML = "";
        const option = document.createElement("option");
        option.value = "";
        option.textContent = "Chapter Name";

        chapterSelect.appendChild(option);

        data.forEach((chapter) => {
          const option = document.createElement("option");
          option.value = chapter.id;
          option.textContent = chapter.name;
          chapterSelect.appendChild(option);
        });
        chapterSelect.hidden = false;
      })
      .catch((error) => {
        console.error("There are error with this subject:", error);
      });
  } else {
    chapterSelect.hidden = true;
  }
};

const handleAddQuestion = function (e) {
  if (listAnswers.length < 3) {
    e.preventDefault();
    errorLabel = document.getElementById("errorLabel");
    errorLabel.innerText = "you must add at least 3 wrong answers! ";
  }
};



