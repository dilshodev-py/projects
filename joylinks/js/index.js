window.addEventListener('DOMContentLoaded', () => {
    const elMenuBtn = document.querySelector('.header__button-wrapper')
    const elHeader = document.querySelector('.header') 


   if (elMenuBtn) {
    elMenuBtn.addEventListener('click', (evt) => {
        elHeader.classList.toggle('header__button--click')
        console.log('hello');
    })
   }
})


