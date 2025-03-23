// Scroll
const nav = document.getElementById("navbar");

let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
    if (window.scrollY > lastScrollY) {
    nav.classList.add("hidden");
    } else {
    nav.classList.remove("hidden");
}
    lastScrollY = window.scrollY;
});
//===========================
const slider = document.querySelector('.slider-1');
const slides = document.querySelectorAll('.slide');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

let index = 0; // المؤشر الحالي
const totalSlides = slides.length;

// دالة لتحريك السلايدر
function moveSlider() {
  slider.style.transform = `translateX(-${index * 100}%)`;
}

// زر التالي
nextButton.addEventListener('click', () => {
  index = (index + 1) % totalSlides; // التنقل كحلقة
  moveSlider();
});

// زر السابق
prevButton.addEventListener('click', () => {
  index = (index - 1 + totalSlides) % totalSlides; // التنقل كحلقة
  moveSlider();
});

// تشغيل السلايدر تلقائيًا
setInterval(() => {
  index = (index + 1) % totalSlides;
  moveSlider();
}, 5000); // تغيير كل 5 ثوانٍ

document.querySelectorAll(".slider").forEach((slider) => {
    const cards = slider.querySelectorAll(".card");
    const prevBtn = slider.parentElement.querySelector(".prev-button");
    const nextBtn = slider.parentElement.querySelector(".next-button");
  
    let currentIndex = 0;
    const visibleCards = 6; 
  
    function updateSliderPosition() {
        const cardWidth = cards[0].offsetWidth + 33;
        slider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }
  
    nextBtn.addEventListener("click", () => {
        const maxIndex = cards.length - visibleCards;
        if (currentIndex < maxIndex) {
            currentIndex++;
            updateSliderPosition();
        }
    });
  
    prevBtn.addEventListener("click", () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateSliderPosition();
        }
    });
  });
