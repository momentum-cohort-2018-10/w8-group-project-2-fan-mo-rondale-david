let apiPage = 1;
let controller, scene;
function init() {
    let navBar = document.querySelector('.navbar-burger');
    if (navBar) {
        navBar.addEventListener('click', toggleNavBar);
    }

    let modalCloser = document.getElementById('close-modal');
    if (modalCloser) {
        modalCloser.addEventListener('click', toggleModal);
    }

    let modalBackground = document.getElementById('modal-background');
    if (modalBackground) {
        modalBackground.addEventListener('click', toggleModal);
    }


    let questionList = document.querySelector('section#question-list');
    if (questionList) {
        loadTenQuestions()
        // Following code is for infinite scrolling feature

        // init controller
        controller = new ScrollMagic.Controller()
        // create scene
        scene = new ScrollMagic.Scene({triggerElement: "#loader", triggerHook: "onEnter"})
                .addTo(controller)
                .addIndicators()
                .on("enter", function (e) {
                    if (!$("#loader").hasClass("active")) {
                        $("#loader").addClass("active");

                        console.log("loading new items");
                        loadTenQuestions()


                    }
                });
            

        questionList.addEventListener('click', function(e) {
            let et = e.target;
            
            
            if (et && et.matches('.answer-controls i')) {
                e.stopPropagation();
                starAnswerHandler(et);
            } else if (et && et.matches('.question-controls i')) {
                e.stopPropagation();
                starQuestionHandler(et);
            } else if(et && et.matches('.answer-controls .check')) {
                e.stopPropagation();
                resolveQuestion(et);
                
            } else if(et && et.matches('.submit-answer')) {
                e.stopPropagation();
                submitAnswer(et);
                
            } else if(et && et.matches('.box.question, .box.question *')) {
                e.stopPropagation();
                while (!et.matches('.box.question')) {
                    et = et.parentNode;
                 }
                
                loadAnswers(et);
            }
        })
    }
    
}
init()

function loadTenQuestions() {
    
    requestAQuestion(apiPage);
    apiPage += 1;
    
}


function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}

function toggleModal(){
    modal.classList.toggle('is-active');
}


//STARRING ITEMS
function starQuestionHandler(et) {

    if (et['attributes']['data-star']) {
        let pk = et['attributes']['data-star'].value;
        unstarItem(pk);
    } else {
        let pk = et['attributes']['data-question'].value;
        starItem('question', pk);
    }
}

function starAnswerHandler(et) {
    if (et['attributes']['data-star']) {
        let pk = et['attributes']['data-star'].value;
        unstarItem(pk);
    } else {
        let pk = et['attributes']['data-answer'].value;
        starItem('answer', pk);
    }

}

function starItem(item, pk){
    
    $.ajax({
        method: 'POST',
        url: `api/${item}s/${pk}/stars/`
    }).done(function(response) {
        let star = document.querySelector(`i[data-${item}='${response.object_id}']`);
        star.setAttribute('data-star', response.pk);
        toggleStar(star);
        console.log(response);
    }).fail(function(response) {
        console.log("There was an error making the star");
        console.log(response);
    });
}

function unstarItem(pk){
    
    $.ajax({
        method: 'DELETE',
        url: `api/stars/${pk}/`,
        dataType: 'text'
    }).done(function(response) {
        let star = document.querySelector(`i[data-star='${pk}']`);
        star.removeAttribute('data-star');
        toggleStar(star);
        
    });
}

function toggleStar(icon){
    icon.classList.toggle('unstarred');
    icon.classList.toggle('starred');

}

//RESOLVING QUESTIONS
function resolveQuestion(et){

    let pk = et.attributes['data-question'].value;
    let answer = et.attributes['data-answer'].value;
    
    $.ajax({
        method: 'POST',
        url: `/api/questions/${pk}/resolve/`,
        data: {
            resolving_answer: answer
        }
    }).done(function(response){
        console.log(response);
        addResolutionBlock(response.resolving_answer);
        removeResolveButtons(response.resolved_question);
        
        console.log(response);
    }).fail(function(response){
        console.log('There was an error resolving this question');
        console.log(response);
    });
}

function removeResolveButtons(question){
    let questionBlock = document.querySelector(`div[data-question="${question}"]`);
    
    questionBlock.querySelectorAll('a.check').forEach(function(button){
        button.parentNode.innerHTML = "";
    });
}

function addResolutionBlock(answer){
    let response = document.querySelector(`a[data-answer="${answer}"]`);

    while (!response.matches('.response')) {
        response = response.parentNode;

     }
    response.classList.add('resolution');
}

//ADDING ANSWERS
function answerHTML(answer, resolved) {
    
    let questionAuthor = document.querySelector(
        `.question[data-question="${answer.question}"] .box-information small`).firstChild.data;

    return `
        <div class="response ${answer.resolved_answer
                                ? 'resolution'
                                : ''}">
            <p>
                <small>${answer.author}</small> - <small>${moment(answer.created_at).format("MMM. D, YYYY, hh:mm a")}</small>
                <br>
                <p>${answer.text_as_html}</p>
                
                <div class="answer-controls">
                    ${answer.starred
                        ? `<i class="fas fa-star fa-lg starred"aria-hidden="true" data-answer="${answer.id}" data-star="${answer.starred}"></i>`
                        : `<i class="fas fa-star fa-lg unstarred"aria-hidden="true" data-answer="${answer.id}"></i>`
                    }

                    ${answer.author === questionAuthor && !resolved
                        ? `<div class="answer-controls">
                                <a class="button is-outlined is-small check" data-question="${answer.question}" data-answer="${answer.id}">
                                    <i class="fas fa-check"></i> &nbsp; Mark as Resolved
                                </a>
                            </div>` 
                        : ''}
                        
                </div>
            </p>
        </div>
    `
}


function submitAnswer(et) {
    
    let pk = et.attributes['data-question'].value;
    let textarea = document.querySelector(`textarea[data-question='${pk}']`);

    let questionBlock = document.querySelector(`.box.question[data-question='${pk}']`);
    
    
    $.ajax({
        method: 'POST',
        url: `/api/questions/${pk}/answers/`,
        data: {
            text: textarea.value
        }
    }).done(function(response){
        textarea.value = "";
        addAnswer(response);
    }).fail(function(response){
        console.log('There was an issue submitting this answer.');
        console.log(response);
    })

}

function addAnswer(answer) {
    let textarea = document.querySelector(`textarea[data-question='${answer.question}']`);

    while (!textarea.matches('.answer-box')) {
        textarea = textarea.parentNode;
    }
    console.log(textarea);
    
    
    textarea.insertAdjacentHTML('beforeend', answerHTML(answer, false));
}

function loadAnswers(e) {
    
    let pk = e.getAttribute('data-question');
    
    $.ajax({
        method: 'GET',
        url: `/api/questions/${pk}/answers/`,
    }).done(function(response){
        
        if (response.results[0]) {
            
            loadAnswersInDom(response.results);
            
        }
        
        
    }).fail(function(error){
        console.log('There was an issue getting a response');
        console.log(error);
    })
}

function loadAnswersInDom(answers) {
    if (answers[0]) {
        let questionBlock = document.querySelector(`.box.question[data-question="${answers[0].question}"]`);
        
        let answerBlocks = questionBlock.querySelectorAll('.response');
        for (answer of answerBlocks) {
            answer.remove()
        }
        let resolved = false;
        
        
        console.log(answers);
        let answerArea = questionBlock.querySelector(`.answer-box`);
        for (answer of answers) {
            
            if (answer.resolved_answer) {
                resolved = true;
            }
        }
        
        for (answer of answers) {
            console.log('resolved', resolved);
            answerArea.insertAdjacentHTML('beforeend', answerHTML(answer, resolved));
        }
        
    }
}

function removeAnswersFromPrevious(pk) {
    let questionBlock = document.querySelector(`.box.question[data-question="${pk}"]`);
    if (questionBlock) {
        let responses = questionBlock.querySelectorAll('.response');
        
        for (response of responses) {
            response.remove();
        }
        
        putResolveBack(pk);
        
    }
    
}

function putResolveBack(pk) {
    let questionBlock = document.querySelector(`.box.question[data-question="${pk}"]`);

    $.ajax({
        method: 'GET',
        url: `/api/questions/${pk}/resolve/`
    }).done(function(response) {
        if (response[0]) {
            let answerArea = questionBlock.querySelector('.answer-box');
            
            answerArea.insertAdjacentHTML('afterbegin', answerHTML(response[0].resolving_answer, true));
            
        }
    }).fail(function(response) {
        console.log("There was an issue getting the resolution");
    });
}


//ADDING QUESTIONS
function questionHTML(question){
    return `
    <div class="box question" data-question="${question.id}">
        <article class="media">
            <div class="media-content">
                <div class="content">
                    <h2>${question.title}</h2>
                        <p class="box-information">
                        <small>${question.author}</small> - <small>${moment(question.created_at).format("MMM. D, YYYY, hh:mm a")}</small>
                        </p>
                        ${question.text_as_html}
                </div>
                <nav class="level is-mobile">
                    <div class="level-left question-controls">
                        <a class="level-item" aria-label="like">
                            <span class="icon is-medium">
                                ${question.starred 
                                    ? `<i class="fas fa-star fa-lg starred" aria-hidden="true" data-question="${question.id}" data-star="${question.starred}"></i>`
                                    : `<i class="fas fa-star fa-lg unstarred" aria-hidden="true" data-question="${question.id}"></i>`
                                }
                                
                            </span>
                        </a>
                        <div>
                            <p><strong>${question.answer_count} ${humanizeAnswers(question.answer_count)}</strong></p>
                        </div>
                    </div>
                </nav>
            </div>
            <div class="answer-box">
                    
            ${question.resolved
                ? `<div class="response resolution">
                        <p>
                            <small>${question.resolved.resolving_answer.author}</small> - <small>${question.resolved.resolving_answer.created_at}</small>
                            <br>
                            <p>${question.resolved.resolving_answer.text}</p>
                        </p>
                    </div>`
                : `<div class="response-field">
                        <div class="field">
                            <form action="">
                                <label class="label" for="text">Respond to Question</label>
                                <textarea name="text" cols="30" rows="10" data-question="${question.id}" class="textarea"></textarea>
                            </form>
                        </div>
                        <div class="control">
                            <button class="button is-link submit-answer" data-question="${question.id}">Submit</button>
                        </div>
                    </div>`
                }

            </div>
        </article>
    </div>
`
}

function humanizeAnswers(num) {
    if (num === 1) {
        return 'Answer';
    } else {
        return 'Answers';
    }
}

function postNewQuestion(){
    let question = {
        title: $('#new-question-title').val(),
        text: $('#new-question-text').val()
    }
    $.ajax({
        url: '/api/questions/',
        method: 'POST',
        data: JSON.stringify(question), 
        contentType: 'application/json'
    }).then(function (question) {

        addQuestionToList(question)
        toggleModal();
    });
}


function addQuestionToList(question){
    
    document.getElementById('question-list').insertAdjacentHTML('afterbegin', questionHTML(question));
    
}

function startQuestions() {
    // click button to ask a question, opens modal with form
    let questionButton = document.getElementById('ask-question');
    if (questionButton) {
        questionButton.addEventListener('click', toggleModal);
    }

    let questionClose = document.getElementById('new-question-cancel');
    if (questionClose) {
        questionClose.addEventListener('click', toggleModal);
    }
    
    let questionSubmit = document.getElementById('new-question-submit');
    if (questionSubmit) {
        questionSubmit.addEventListener('click', postNewQuestion);
    }

    setupCSRFAjax()
}
startQuestions()

function requestAQuestion(page) {

    $.ajax({
        url: `/api/questions/?page=${page}`,
        method: 'GET',
        contentType: 'application/json'
    }).done(function(response) {
        console.log(response);
        loadQuestionsToDom(response.results);
        
        scene.update();
        $("#loader").removeClass("active")
    }).fail(function(response) {
        $('#loader').remove();

    });

}


function loadQuestionsToDom(questions){
    for (question of questions) {
        document.getElementById('question-list').insertAdjacentHTML('beforeend', questionHTML(question));
    }
    
}


function setupCSRFAjax () {
    var csrftoken = Cookies.get('csrftoken')
  
    $.ajaxSetup({
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader('X-CSRFToken', csrftoken)
        }
      }
    })
}

function csrfSafeMethod(method){
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}