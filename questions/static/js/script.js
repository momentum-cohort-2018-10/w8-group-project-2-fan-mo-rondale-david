function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let csrftoken = getCookie('csrftoken');

function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}
function toggleModal(){
    modal.classList.toggle('is-active');
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


function init() {
    document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar);
    // click button to ask a question, opens modal with form
    document.getElementById('ask-question').addEventListener('click', toggleModal);
    document.getElementById('close-modal').addEventListener('click', toggleModal);
    document.getElementById('modal-background').addEventListener('click', toggleModal);
    document.querySelectorAll('.question-controls .unstarred').forEach(function(star){
        star.addEventListener('click', starItem);
    });
    document.getElementById('new-question-cancel').addEventListener('click', toggleModal)
    document.getElementById('new-question-submit').addEventListener('click', postNewQuestion)

}


init()

function starItem(){
    pk = this.attributes['data-question'].value;
    $.ajax({
        method: 'POST',
        url: `api/questions/${pk}/stars/`,
        data: {
            csrfmiddlewaretoken: csrftoken,
        }
    }).done(function(response) {
        star = document.querySelector(`i[data-question='${response.object_id}']`);
        toggleStar(star);
        console.log(response);
    }).fail(function(response) {
        console.log("There was an error");
        console.log(response);
    });
}

function unstarItem(){
    pk = this.attributes['data-question'].value;
    $.ajax({
        method: 'DELETE',
        url: `api/questions/${pk}/stars/`,
        data: {
            csrfmiddlewaretoken: csrftoken,
        }
    }).done(function(response) {
        star = document.querySelector(`i[data-question='${response.object_id}']`);
        toggleStar(star);
        console.log(response);
    }).fail(function(response) {
        console.log("There was an error");
        console.log(response);
    });
}

function toggleStar(icon){
    icon.classList.toggle('unstarred');
    icon.classList.toggle('starred');

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