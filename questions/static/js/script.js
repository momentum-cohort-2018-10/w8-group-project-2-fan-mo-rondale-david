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

function init() {
    document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar);
    document.getElementById('ask-question').addEventListener('click', toggleModal);
    document.getElementById('close-modal').addEventListener('click', toggleModal);
    document.getElementById('modal-background').addEventListener('click', toggleModal);
    document.querySelectorAll('.question-controls .unstarred').forEach(function(star){
        star.addEventListener('click', starItem);
    });
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
    
    console.log(icon);
}