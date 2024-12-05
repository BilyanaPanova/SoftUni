document.addEventListener('DOMContentLoaded', solve);

function solve() {
    let rightAnswers = 0;
    let currentQuestionIndex = 0;

    const correctAnswers = [
        "onclick",          
        "JSON.stringify()",  
        "A programming API for HTML and XML documents" ]

    const handleAnswerClick = (event) => {
        const selectedAnswer = event.target.textContent;

        if (selectedAnswer === correctAnswers[currentQuestionIndex]) {
            rightAnswers++;
        }

        const currentQuestion = document.querySelectorAll('.question')[currentQuestionIndex];
        currentQuestion.classList.add('hidden');

        currentQuestionIndex++;

        if (currentQuestionIndex < correctAnswers.length) {
            const nextQuestion = document.querySelectorAll('.question')[currentQuestionIndex];
            nextQuestion.classList.remove('hidden');
        } else {
            displayResults();
        }
    };

    const displayResults = () => {
        const resultsDiv = document.getElementById('results');
        let resultMessage = '';

        if (rightAnswers === 3) {
            resultMessage = "You are recognized as top JavaScript fan!";
        } else {
            resultMessage = `You have ${rightAnswers} right answer${rightAnswers !== 1 ? 's' : ''}`;
        }

        resultsDiv.textContent = resultMessage;
    };

    const answerElements = document.querySelectorAll('.quiz-answer');
    answerElements.forEach(answer => {
        answer.addEventListener('click', handleAnswerClick);
    });
}
