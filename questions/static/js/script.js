/* global fetch, $, Cookies, questions */

document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar)

function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}


function questionHTML(question){
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
    </article>
</div>
`
}




document.getElementById('ask-question').addEventListener('click', askQuestionModal)
// click button to ask a question, opens modal with form
function askQuestionModal(){
    modal.style.display = "block";
}


document.getElementById('close-modal').addEventListener('click', closeModal)
// click 'x' in top right of modal to close modal
function closeModal(){
    modal.style.display = "none";
}


document.getElementById('modal-background').addEventListener('click', closeBackgroundModal)
// click anywhere in backgroud of modal to close modal
function closeBackgroundModal(){
    modal.style.display = "none";
}


document.getElementById('new-question-cancel').addEventListener('click', closeQuestionCancel)
// click 'cancel' button to close modal
function closeQuestionCancel(){
    modal.style.display = "none";
}


document.getElementById('new-question-submit').addEventListener('click', postNewQuestion)
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
        $('#ask-question').removeClass('is-active')
        modal.style.display = "none"
    })
}


function loadQuestions(){
    $.get('/api/questions')
      .then(function (questions) {
          for (let question of questions) {
              addQuestionToList(question)
          }
      })
}


function addQuestionToList(question){
    $('question-list').append(questionHTML(question))
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

function startQuestions() {
    loadQuestions()
    setupCSRFAjax()
}

function csrfSafeMethod(method){
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

startQuestions()