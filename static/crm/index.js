const burgerBtn = document.querySelector("header .burgerBtn");
const burger = document.querySelector(".burger");

burgerBtn.addEventListener("click", () => {
    burgerBtn.classList.toggle("active");
    burger.classList.toggle("active");
    document.body.classList.toggle("active");
})
