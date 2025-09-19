const image = document.querySelector('.image');
const hover = document.querySelector('.hover');
const modal = document.querySelector('.modal');
const close = document.querySelector('.close');

function show(){
    hover.classList.add('active');
    modal.classList.add('show');
}

function hide(){
    hover.classList.remove('active');
    modal.classList.remove('show');
}

image.addEventListener('click', show);
close.addEventListener('click', hide);

// more info ... 

function toggleText() {
    const textElement = document.getElementById('aboutText');
    const readMoreBtn = document.getElementById('readMoreBtn');

    if (readMoreBtn.innerHTML === 'more info ...') {
        textElement.style.webkitLineClamp = 'unset'; // Show full text
        readMoreBtn.innerHTML = 'Read less';
    } else {
        textElement.style.webkitLineClamp = '2'; // Limit to 2 lines
        readMoreBtn.innerHTML = 'more info ...';
    }
}

// Check if the text exceeds 2 lines
function checkTextOverflow() {
    const textElement = document.getElementById('aboutText');
    const readMoreBtn = document.getElementById('readMoreBtn');

    const lineHeight = parseInt(window.getComputedStyle(textElement).lineHeight);
    const maxLines = 2;
    const maxHeight = lineHeight * maxLines;

    if (textElement.scrollHeight > maxHeight) {
        readMoreBtn.style.display = 'inline'; // Show the more info ... button if text overflows
    } else {
        readMoreBtn.style.display = 'none'; // Hide the more info ... button if text fits
    }
}

window.onload = checkTextOverflow;



// gallary img 

const gallery = document.getElementById('gallery');
const galleryImage = document.getElementById('gallery-image');
const closeGallery = document.getElementById('close-gallery');
const openGalleryLinks = document.querySelectorAll('.open-gallery');

openGalleryLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const imgSrc = this.querySelector('img').getAttribute('src');
        galleryImage.setAttribute('src', imgSrc);
        gallery.classList.add('active');
        gallery.classList.remove('closing'); // Remove closing state
    });
});

closeGallery.addEventListener('click', function() {
    gallery.classList.add('closing'); // Add closing state for animation
    setTimeout(() => {
        gallery.classList.remove('active');
    }, 500); // Delay removal for the animation to complete
});

gallery.addEventListener('click', function(e) {
    if (e.target === gallery) {
        gallery.classList.add('closing');
        setTimeout(() => {
            gallery.classList.remove('active');
        }, 500); // Delay for close animation
    }
});