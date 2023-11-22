

const chooseSubjectForExam = function (e) {
  const subject = document.getElementById("subjectName").value;
  const chapterSelect = document.getElementById("chapterNameForExam");
  const attributesContainer = document.getElementById("attributesContainerForExam");
  const chapterContainer = document.getElementById("chapterContainerForExam");
  const difficultyContainer = document.getElementById("difficultyContainer");
  const objectiveContainer = document.getElementById("objectiveContainer");
  const createExamButton = document.getElementById('createExamButton')


  const url = `/create/get/chapters/${subject}/`;

  if (subject) {
    fetch(url, {chooseSubjectForExam,
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": '{{ csrf_token }}',
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("Network response was not ok.");
      })
      .then((data) => {
        chapterContainer.innerHTML = "";

        chapterSelect.isValid = true
        difficultyContainer.isValid = true
        objectiveContainer.isValid = true
        createExamButton.disabled = false

        chapterSelect.innerHTML = "";
        const chHeader = document.createElement("h4");
        chHeader.innerText = "Chapters: ";

        const container = document.createElement("div");
        const attrLabel = document.createElement("label");
        const numQuestions = document.createElement("input");


        attrLabel.innerText = "Total Questions";
        attrLabel.classList.add("btn");
        attrLabel.classList.add("btn-dark");
        attrLabel.classList.add("font-sm");
        attrLabel.classList.add("width-sm");


        container.classList.add("input-group");
        container.classList.add("my-1");
        container.classList.add("mb-5");

        numQuestions.name = "totalQuestions";
        numQuestions.id = "totalQuestions";
        attrLabel.setAttribute("for", "totalQuestions");

        numQuestions.placeholder = "Total number of questions 10:1000";
        numQuestions.value = 100;
        numQuestions.type = "number";
        numQuestions.min = "10";
        numQuestions.max = "1000";
        numQuestions.required = true;
        numQuestions.classList.add("form-control");
        numQuestions.classList.add("font-sm");
        numQuestions.onchange = numQuestionsChangeHandler

        container.appendChild(attrLabel);
        container.appendChild(numQuestions);

        chapterContainer.appendChild(container);

        var numberInput = document.getElementById("myNumberInput");

        numQuestions.addEventListener("change", function (event) {
          numQuestionsChangeHandler(event)
        });

        chapterSelect.appendChild(chHeader);
        let lastInput = null
        data.forEach((chapter) => {
          const container = document.createElement("div");
          const attrLabel = document.createElement("label");
          const inputChapter = document.createElement("input");
          lastInput = inputChapter

          attrLabel.innerText = chapter.name;
          attrLabel.classList.add("btn");
          attrLabel.classList.add("btn-dark");
          attrLabel.classList.add("font-sm");
          attrLabel.classList.add("width-sm");

          container.classList.add("input-group");
          container.classList.add("my-1");
          inputChapter.name = chapter.id;
          inputChapter.id = chapter.id;
          attrLabel.setAttribute("for", chapter.id);

          inputChapter.placeholder = "Number of questions";
          inputChapter.required = true;
          inputChapter.type = "number";
          inputChapter.value = "0";
          inputChapter.max = numQuestions.value;
          inputChapter.classList.add("form-control");
          inputChapter.classList.add("font-sm");
          inputChapter.addEventListener("change", function (event) {
            chapterChangeHandlerForInputs(event)
          });

          container.appendChild(attrLabel);
          container.appendChild(inputChapter);
          chapterSelect.appendChild(container);
        });

        lastInput.readOnly = true
        lastInput.value = numQuestions.value;

        
        chapterContainer.appendChild(chapterSelect);
        chapterContainer.hidden = false;
        attributesContainer.hidden = false;
        chapterChangeHandler()
        difficultyChangeHandler()
        objectiveChangeHandler()
      })
      .catch((error) => {
        console.error("There are error with this subject:", error);
      });
  } else {
    chapterContainer.hidden = true;
    attributesContainer.hidden = true;
  }
};
