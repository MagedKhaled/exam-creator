
const createExamButton = document.getElementById('createExamButton')

const chapterChangeHandler = (event) => {
    const numQuestions = document.getElementById('totalQuestions').value
    const chapterContainer = document.getElementById('chapterNameForExam')
    const difficultyContainer = document.getElementById('difficultyContainer')
    const objectiveContainer = document.getElementById('objectiveContainer')
    const inputElements = chapterContainer.querySelectorAll('input')

    let valueSum = 0
    for (i=0; i<inputElements.length-1; i++){
        inputElements[i].max = numQuestions
        valueSum = valueSum + parseInt(inputElements[i].value)
    }

    const lastChapter = inputElements[inputElements.length-1]
    lastChapter.value = numQuestions - valueSum

    if(parseInt(lastChapter.value) < 0){
        chapterContainer.isValid = false 
        lastChapter.classList.add('text-danger')

        createExamButton.disabled = true

    }
    else{
        chapterContainer.isValid = true 
        lastChapter.classList.remove('text-danger')
        
        if(objectiveContainer.isValid && difficultyContainer.isValid){
            createExamButton.disabled = false
        }
    }

}

const chapterChangeHandlerForInputs = (event) => {
    const numQuestions = document.getElementById('totalQuestions').value
    const inputChapter = event.target
    
    if (inputChapter.value === "" || inputChapter.value.includes('e')) {
        inputChapter.value = "0";
        } else if (parseInt(inputChapter.value) < 0) {
        inputChapter.value = "0";
        } else if (parseInt(inputChapter.value)>parseInt(numQuestions.value)){
        inputChapter.value = numQuestions.value
        }

    chapterChangeHandler()

}



const difficultyChangeHandler = () => {
    const numQuestions = document.getElementById('totalQuestions').value

    const chapterContainer = document.getElementById('chapterNameForExam')
    const difficultyContainer = document.getElementById('difficultyContainer')
    const objectiveContainer = document.getElementById('objectiveContainer')    
    
    const inputElements = difficultyContainer.querySelectorAll('input')

    inputElements[0].max = numQuestions
    inputElements[1].value = numQuestions - inputElements[0].value

    if(parseInt(inputElements[1].value) < 0){
        difficultyContainer.isValid = false 
        inputElements[1].classList.add('text-danger')

        createExamButton.disabled = true
    }
    else{
        difficultyContainer.isValid = true 
        inputElements[1].classList.remove('text-danger')

        if(objectiveContainer.isValid && chapterContainer.isValid){
            createExamButton.disabled = false
        }

    }
}

const difficultyChangeHandlerForInputs = (event) => {
    const numQuestions = document.getElementById('totalQuestions').value
    const inputChapter = event.target
    
    if (inputChapter.value === "" || inputChapter.value.includes('e')) {
        inputChapter.value = "0";
        } else if (parseInt(inputChapter.value) < 0) {
        inputChapter.value = "0";
        } else if (parseInt(inputChapter.value)>parseInt(numQuestions.value)){
        inputChapter.value = numQuestions.value
        }

    difficultyChangeHandler()

}



const objectiveChangeHandler = () => {
    const numQuestions = document.getElementById('totalQuestions').value

    const chapterContainer = document.getElementById('chapterNameForExam')
    const difficultyContainer = document.getElementById('difficultyContainer')
    const objectiveContainer = document.getElementById('objectiveContainer')    
    
    const inputElements = objectiveContainer.querySelectorAll('input')

    inputElements[0].max = numQuestions
    inputElements[1].max = numQuestions
    inputElements[2].value = numQuestions - inputElements[0].value - inputElements[1].value

    if(parseInt(inputElements[2].value) < 0){
        objectiveContainer.isValid = false 
        inputElements[2].classList.add('text-danger')

        createExamButton.disabled = true

    }
    else{
        objectiveContainer.isValid = true 
        inputElements[2].classList.remove('text-danger')

        if(chapterContainer.isValid && difficultyContainer.isValid){
            createExamButton.disabled = false
        }

        

    }
}

const objectiveChangeHandlerForInputs = (event) => {
    const numQuestions = document.getElementById('totalQuestions').value
    const inputChapter = event.target
    
    if (inputChapter.value === "" || inputChapter.value.includes('e')) {
        inputChapter.value = "0";
        } else if (parseInt(inputChapter.value) < 0) {
        inputChapter.value = "0";
        } else if (parseInt(inputChapter.value)>parseInt(numQuestions.value)){
        inputChapter.value = numQuestions.value
        }

    objectiveChangeHandler()

}


const numQuestionsChangeHandler = (event) => {
    const numQuestions = event.target
    if (numQuestions.value === "") {
        numQuestions.value = "10";
    } else if (parseInt(numQuestions.value) < 10) {
        numQuestions.value = "10";
    } else if (parseInt(numQuestions.value) > 1000) {
        numQuestions.value = "1000";
    }
    chapterChangeHandler()
    difficultyChangeHandler()
    objectiveChangeHandler()
}



