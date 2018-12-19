document.querySelector('.navbar-burger').addEventListener('click', toggleNavBar)

function toggleNavBar(){
    this.classList.toggle('is-active');
    document.querySelector('.navbar-menu').classList.toggle('is-active');
}