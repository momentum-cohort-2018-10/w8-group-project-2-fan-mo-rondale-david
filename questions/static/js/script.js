function questionHTML(question){
    return `
    <div class="box question">
    <article class="media">
        xs
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
    document.querySelectorAll('.question-controls i').forEach(function(star){
        star.addEventListener('click', starHandler);
    });
    document.getElementById('new-question-cancel').addEventListener('click', toggleModal)
    document.getElementById('new-question-submit').addEventListener('click', postNewQuestion)

}
function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}
function toggleModal(){
    modal.classList.toggle('is-active');
}

init()

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