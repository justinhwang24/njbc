let slideIndex = 1;
let sessionId = 0;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  sessionId++;
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  sessionId++;
  showSlides(slideIndex = n);
}

function showSlides(n, temp) {
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (let i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  slideIndex++; 
  if (slideIndex > slides.length) {slideIndex = 1}
  if (slideIndex < 1) {slideIndex = slides.length}
  setTimeout(showSlides, 4000);
}