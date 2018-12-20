/* globals $ */

document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar)

function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
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
    })
}

function addQuestionToList(question){
    $('question-list').append(question)
}