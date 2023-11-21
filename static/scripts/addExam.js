const chooseSubjectForExam = function (e) {
  const subject = document.getElementById("subjectName").value;
  const chapterSelect = document.getElementById("chapterNameForExam");
  const attributesContainer = document.getElementById("attributesContainerForExam");


  const url = `/create/get/chapters/${subject}/`;

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
        const chHeader = document.createElement("h3")
        chHeader.innerText = 'Chapters: '


        const numQuestions = document.createElement("input")
        const container = document.createElement("div");
        const attrLabel = document.createElement("label");

        attrLabel.innerText = 'Total Questions';
        attrLabel.classList.add("btn");
        attrLabel.classList.add("btn-secondary");
        attrLabel.style.width = "200px";

        container.classList.add("input-group");
        container.classList.add("my-1");
        container.classList.add("mb-5");

        numQuestions.name = 'totalQuestions';
        numQuestions.placeholder = "Total number of questions 10:1000";
        numQuestions.value = 100
        numQuestions.type = 'number'
        numQuestions.min = '10'
        numQuestions.max = '1000'
        numQuestions.required = true;
        numQuestions.classList.add("form-control");

        container.appendChild(attrLabel);
        container.appendChild(numQuestions);
        chapterSelect.appendChild(container);


        var numberInput = document.getElementById('myNumberInput');

        numQuestions.addEventListener('change', function() {
            if (numQuestions.value === '') {
                numQuestions.value = '10';
            }
            else if (parseInt(numQuestions.value) < 10){
                numQuestions.value = '10';

            }
        });



        chapterSelect.appendChild(chHeader)




        data.forEach((chapter) => {
          const container = document.createElement("div");
          const attrLabel = document.createElement("label");
          const inputChapter = document.createElement("input");

          attrLabel.innerText = chapter.name;
          attrLabel.classList.add("btn");
          attrLabel.classList.add("btn-secondary");
          attrLabel.style.width = "200px";

          container.classList.add("input-group");
          container.classList.add("my-1");

          inputChapter.name = chapter.id;
          inputChapter.placeholder = "Number of questions";
          inputChapter.required = true;
          inputChapter.type = 'number'
          inputChapter.classList.add("form-control");

          container.appendChild(attrLabel);
          container.appendChild(inputChapter);
          chapterSelect.appendChild(container);
        });
        chapterSelect.hidden = false;
        attributesContainer.hidden = false;
      })
      .catch((error) => {
        console.error("There are error with this subject:", error);
      });
  } else {
    chapterSelect.hidden = true;
    attributesContainer.hidden = true;

  }
};
