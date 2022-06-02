let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  slideIndex = 1;
  let slides = [];
  for (let i = 1; i <= 3; i++) {
    slides.push(document.getElementById("image" + i));
  }
  console.log(slides.length)
//   let dots = document.getElementsByClassName("demo");
//   let captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
//   for (let i = 0; i < dots.length; i++) {
    // dots[i].className = dots[i].className.replace(" active", "");
//   }
  slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
//   captionText.innerHTML = dots[slideIndex-1].alt;
}