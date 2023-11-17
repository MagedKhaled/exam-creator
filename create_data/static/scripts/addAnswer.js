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
        console.log(cloneElement)
        parentContainer.appendChild(cloneElement);
      } else {
        originalElement.children[2].innerText = "This chapter is added before ";
      }
    } else {
      originalElement.children[2].innerText =
        "chapter name must be at least 1 characters ";
    }
  };
  
  