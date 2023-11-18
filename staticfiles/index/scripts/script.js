window.addEventListener('load', function () {
    const loader = document.querySelector('.loader');
    loader.classList.add('hidden');
})

window.onload = function() {
    let container = document.querySelector('.container');

    setTimeout(function() {
        container.style.left = '0';
    }, 500); // Delay for the image to slide from the left

}

function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 20;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}

window.addEventListener("scroll", reveal);
