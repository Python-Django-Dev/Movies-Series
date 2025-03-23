// 
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


document.querySelectorAll(".slider").forEach((slider) => {
    const cards = slider.querySelectorAll(".card");
    const prevBtn = slider.parentElement.querySelector(".prev-button");
    const nextBtn = slider.parentElement.querySelector(".next-button");

    let currentIndex = 0;
    const visibleCards = 6;

    // تعديل الاتجاه ليصبح RTL
    function updateSliderPosition() {
        const cardWidth = cards[0].offsetWidth + 33; // عرض الكارد مع المسافة بين الكروت
        const offset = currentIndex * cardWidth;
        slider.style.transform = `translateX(${offset}px)`; // لاحظ الاتجاه الموجب
    }

    // الزر التالي (حركة للخلف لأننا في RTL)
    nextBtn.addEventListener("click", () => {
        const maxIndex = cards.length - visibleCards;
        if (currentIndex > 0) {
            currentIndex--;
            updateSliderPosition();
        }
    });

    // الزر السابق (حركة للأمام لأننا في RTL)
    prevBtn.addEventListener("click", () => {
        const maxIndex = cards.length - visibleCards;
        if (currentIndex < maxIndex) {
            currentIndex++;
            updateSliderPosition();
        }
    });



    
});
  const footer = document.querySelector('footer');
  let lastScrollTop = 0;

  window.addEventListener('scroll', () => {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

      if (scrollTop > lastScrollTop) {
          footer.classList.remove('show');
      } else {
          footer.classList.add('show');
      }

      lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
  });
