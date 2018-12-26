function init() {
    document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar);
    document.getElementById('close-modal').addEventListener('click', toggleModal);
    document.getElementById('modal-background').addEventListener('click', toggleModal);
    document.querySelectorAll('.question-controls i').forEach(function(star){
        star.addEventListener('click', starHandler);
    });
    document.querySelectorAll('.answer-controls .check').forEach(function(check){
        check.addEventListener('click', resolveQuestion);
    });

    document.querySelectorAll('.submit-answer').forEach(function(button){
        button.addEventListener('click', submitAnswer);
    });
}
init()

function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}


function starHandler() {
    console.log(this);
    if (this.attributes['data-star']) {
        pk = this.attributes['data-star'].value;
        unstarItem(pk);
    } else {
        pk = this.attributes['data-question'].value;
        starItem(pk);
    }
}

function starItem(pk){
    
    $.ajax({
        method: 'POST',
        url: `api/questions/${pk}/stars/`
    }).done(function(response) {
        star = document.querySelector(`i[data-question='${response.object_id}']`);
        star.setAttribute('data-star', response.pk);
        star.addEventListener('click', unstarItem);
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
        star = document.querySelector(`i[data-star='${pk}']`);
        star.removeAttribute('data-star');
        toggleStar(star);
        
    });
}

function toggleStar(icon){
    icon.classList.toggle('unstarred');
    icon.classList.toggle('starred');

}


function resolveQuestion(){
    pk = this.attributes['data-question'].value;
    answer = this.attributes['data-answer'].value;
    console.log(pk, answer);
    $.ajax({
        method: 'POST',
        url: `/api/questions/${pk}/resolve/`,
        data: {
            resolving_answer: answer
        }
    }).done(function(response){
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
    response.parentNode.parentNode.classList.add('resolution')
}


function answerHTML(answer) {
    questionAuthor = document.querySelector(
        `.question[data-question='${answer.question}'] .box-information small`).firstChild.data;
    return `
    <div class="response">
        <p>
            <small>${answer.author}</small> - <small>${answer.created_at}</small>
            <br>
            ${answer.text}
            ${answer.author === questionAuthor ? `<div class="answer-controls">
            <a class="button is-outlined is-small check" data-question="${answer.question}" data-answer="${answer.id}">
                <i class="fas fa-check"></i> &nbsp; Mark as Resolved
            </a>
            </div>` : ''}    
        </p>
    </div>
`
}

function submitAnswer() {
    pk = this.attributes['data-question'].value;
    textarea = document.querySelector(`textarea[data-question='${pk}']`);

    $.ajax({
        method: 'POST',
        url: `/api/questions/${pk}/answers/`,
        data: {
            text: textarea.value
        }
    }).done(function(response){
        console.log(response);
        textarea.value = "";
        addAnswer(response);
    }).fail(function(response){
        console.log('There was an issue submitting this answer.');
        console.log(response);
    })

}

function addAnswer(answer) {
    textarea = document.querySelector(`textarea[data-question='${answer.question}']`);
    textarea.parentNode.parentNode.parentNode.insertAdjacentHTML('afterend', answerHTML(answer));
}


function questionHTML(question){
    return `
    <div class="box question" data-question="${question.id}">
        <article class="media">
            <div class="media-content">
                <div class="content">
                    <h2>${question.title}</h2>
                        <p class="box-information">
                        <small>${question.author}</small> - <small>${question.created_at}</small>
                        </p>
                        ${question.text}
                </div>
                <nav class="level is-mobile">
                    <div class="level-left question-controls">
                        <a class="level-item" aria-label="like">
                            <span class="icon is-medium">
                                    <i class="fas fa-star fa-lg unstarred" aria-hidden="true" data-question="${question.id}"></i>
                            </span>
                        </a>
                        <div>
                            <p><strong>0 Answers</strong></p>
                        </div>
                    </div>
                </nav>
            </div>
        </article>
    </div>
`
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
        console.log(question);
        addQuestionToList(question)
        toggleModal();
    });
}


function loadQuestions(){
    $.get('/api/questions/')
      .then(function (questions) {
        //   for (let question of questions) {
        //       addQuestionToList(question)
        //   }
      })
}

function addQuestionToList(question){
    document.getElementById('question-list').insertAdjacentHTML('afterbegin', questionHTML(question));
    document.querySelector('.question-controls i').addEventListener('click', starHandler);
}

function startQuestions() {
    // click button to ask a question, opens modal with form
    document.getElementById('ask-question').addEventListener('click', toggleModal);
    document.getElementById('new-question-cancel').addEventListener('click', toggleModal);
    document.getElementById('new-question-submit').addEventListener('click', postNewQuestion);
    loadQuestions()
    setupCSRFAjax()
}
startQuestions()

function toggleModal(){
    modal.classList.toggle('is-active');
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



// Following code is for infinite scrolling feature

// init controller
var controller = new ScrollMagic.Controller()
// create scene
var scene = new ScrollMagic.Scene({triggerElement: "#loader", triggerHook: "onEnter"})
        .addTo(controller)
        .addIndicators()
        .on("enter", function (e) {
            if (!$("#loader").hasClass("active")) {
                $("#loader").addClass("active");
                
                console.log("loading new items");
                loadTenQuestions()
                
                
            }
        });

function loadTenQuestions() {
    let lastQuestion = document.querySelector('section#question-list').lastElementChild.getAttribute('data-question');
    lastQuestion = 1
    for (let i=1; i<11; i++) {
        let nextQuestion = lastQuestion-i;
        if (nextQuestion < 0) {
            $('#loader').remove();
            
            
        }
        try {
            requestAQuestion(nextQuestion);
        }
        catch(error) {
            console.log(error);
        }
    }
    
}

function requestAQuestion(pk) {
    $.ajax({
        url: `/api/questions/${pk}`,
        method: 'GET',
        contentType: 'application/json'
    }).done(function (response) {
            console.log(response);
            loadQuestionToDom(response);
            // loadQuestions()
            // addMore(10)
            scene.update();
            $("#loader").removeClass("active")
    });

}


function loadQuestionToDom(question){
    document.getElementById('question-list').insertAdjacentHTML('beforeend', questionHTML(question));
    document.querySelector('.question-controls i').addEventListener('click', starHandler);
}


startQuestions()
