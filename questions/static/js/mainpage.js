$(document).ready(function () {
    init()
    getAllQuestions();
    // 
});

function clearQuestions() {
    $("#questionsPanel").text("");
}

function updateQuestionEventHandlers() {
    document.querySelectorAll('.question-controls .unstarred').forEach(function (star) {
        star.addEventListener('click', starItem);
    });
}

function getAllQuestions() {
    var url = "/api/questions";
    var logMessage = "[Search Request] " + url;
    writeLog(logMessage);
    $.get(url, null, displayQuestions);
}

function displayQuestions(data, status, xhr) {

    if (data == undefined) {
        writeLog("[No data returned from REST request]");
    }
    var qCount = data.length;
    writeLog("[Displaying " + qCount + " questions...]");
    clearQuestions();

    data.forEach(function (question) {
        var qContent = buildQuestionContent(question);
        writeLog("Adding question content:" + qContent);
        $("#questionsPanel").append(qContent);
        getAnswersFor(question.id)
    });
}

function getAnswersFor(questionId) {
    var url = "/api/questions/" + questionId + "/answers";
    var logMessage = "[Search Request] " + url;
    writeLog(logMessage);
    $.get(url, null, displayAnswers);
}

function displayAnswers(data, status, xhr) {

    if (data == undefined) {
        writeLog("[No data returned from REST request]");
        return;
    }

    data.forEach(function (answer) {
        var aContent = buildAnswerContent(answer);
        writeLog("Adding answer content: Question " + answer.question + ", Answer: " + answer.id);
        $("#answerBox-" + answer.question).append(aContent);
    });
}

function buildQuestionContent(question) {
    return `
    <div class="box question">
    <article class="media">
        
        <div class="media-content">
            <div class="content">
                <p>
                    <small>${question.author}</small> <small>31m</small>
                    <br>
                    ${question.text}
                </p>
            </div>
            <nav class="level is-mobile">
                <div class="level-left">

                    <a class="level-item" aria-label="reply">
                        <span class="icon is-small">
                            <i class="fas fa-reply fa-lg" aria-hidden="true"></i>
                        </span>
                    </a>
                    
                    <a class="level-item" aria-label="like">
                        <span class="icon is-small">
                            <i class="fas fa-star fa-lg" aria-hidden="true"></i>
                        </span>
                    </a>
                </div>
            </nav>
        </div>
        <div id="answerBox-${question.id}" class="answer-box">

        </div> 
        
    </article>
</div>
`
}


// "id": 194,
// "question": 51,
// "text": "There sound training defense. Subject born organization expert. Change into leg total southern production drug.\nCamera five parent hair wind fight light. Evidence Republican off involve success whom pretty. Assume husband yet region majority.",
// "author": "Shelby.Byrd",
// "star_count": 0,
// "created_at": "2018-12-25T20:40:51.581640-05:00",
// "answer_detail_link": "http://127.0.0.1:8000/api/answers/194/",
// "star_list_link": "http://127.0.0.1:8000/api/answers/194/stars/"
function buildAnswerContent(answer) {
    return `
        <div id="answer-${answer.question}-${answer.id}" class="response">
            <p>
                <small>${answer.author}</small> - <small>${answer.created_at}</small>
                <br />
                ${answer.text}
            </p>
    </div> 
    `
}


function writeLog(message) {
    console.log(message);
}