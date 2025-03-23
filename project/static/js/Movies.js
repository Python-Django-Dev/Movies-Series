// const slider = document.querySelector(".slider");
// const cards = document.querySelectorAll(".card");
// const prevBtn = document.getElementById("prev-button");
// const nextBtn = document.getElementById("next-button");

// let currentIndex = 0;
// const visibleCards = 7; 

// function updateSliderPosition() {
//     const cardWidth = cards[0].offsetWidth+20 ; 
//     slider.style.transform = ` translateX(-${currentIndex * cardWidth}px)`;
//   }
//   nextBtn.addEventListener("click", () => {
//     const maxIndex = cards.length - visibleCards;
//     // if (currentIndex < maxIndex) {
//     if (currentIndex < 7) {
//       currentIndex+=7;
//       updateSliderPosition();
//     }
//   });

  
//   prevBtn.addEventListener("click", () => {
//     if (currentIndex > 0) {
//       currentIndex-=7;
//       updateSliderPosition();
//     }
//   });
// استهداف جميع السلايدرز
document.querySelectorAll(".slider").forEach((slider) => {
    const cards = slider.querySelectorAll(".card");
    const prevBtn = slider.parentElement.querySelector(".prev-button");
    const nextBtn = slider.parentElement.querySelector(".next-button");

    let currentIndex = 0;
    const visibleCards = 7; // عدد الكروت المرئية

    function updateSliderPosition() {
        const cardWidth = cards[0].offsetWidth + 20; // عرض الكارت + المسافة بين الكروت
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
