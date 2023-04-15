const burgerBtn = document.querySelector("header .burgerBtn");
const burger = document.querySelector(".burger");

burgerBtn.addEventListener("click", () => {
    burgerBtn.classList.toggle("active");
    burger.classList.toggle("active");
    document.body.classList.toggle("active");
})

const lang = document.querySelector(".header__block div")

lang.addEventListener("click", () => {
    lang.classList.toggle("active")
})