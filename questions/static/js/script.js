/* globals */

document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar)

function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}


document.getElementById('ask-question').addEventListener('click', askQuestionModal)

function askQuestionModal(){
    modal.style.display = "block";
}


document.getElementById('close-modal').addEventListener('click', closeModal)

function closeModal(){
    modal.style.display = "none";
}

document.getElementById('modal-background').addEventListener('click', backgroundCloseModal)

function backgroundCloseModal(){
    modal.style.display = "none";
}