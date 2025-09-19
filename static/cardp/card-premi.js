// Function to view the image in fullscreen
document.querySelectorAll('.view').forEach(function (viewLink) {
    viewLink.addEventListener('click', function (e) {
        e.preventDefault();
        const imgSrc = this.closest('.item').querySelector('img').src;
        const fullscreenOverlay = document.getElementById('fullscreen-overlay');
        const fullscreenImg = document.getElementById('fullscreen-img');
        fullscreenImg.src = imgSrc;
        fullscreenOverlay.style.display = 'flex';
    });
});

document.querySelector('.close').addEventListener('click', function () {
    document.getElementById('fullscreen-overlay').style.display = 'none';
});

// Function to handle sending the enquiry
function handleSendEnquiry() {
    // Retrieve values from the form fields
    const name = document.getElementById('enquiryName').value.trim();
    const phone = document.getElementById('phoneNumber').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    
    // Retrieve the dynamic email value from the hidden input field
    const premiumEmail = document.getElementById('premium-email').value.trim();

    // Validation: Check if all fields are filled
    if (!name || !phone || !email || !message) {
        alert('Please fill in all fields.');
        return;
    }

    // Additional validation checks (optional)
    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    if (!validatePhone(phone)) {
        alert('Please enter a valid phone number.');
        return;
    }

    // Prepare the mailto link with the collected form data
    const mailtoLink = `mailto:${premiumEmail}?subject=Enquiry from ${encodeURIComponent(name)}&body=${encodeURIComponent(
        `Name: ${name}\nPhone: ${phone}\nEmail: ${email}\nMessage: ${message}`
    )}`;

    // Open the mailto link to launch the user's email client
    window.location.href = mailtoLink;
}

// Optional: Validate email format
function validateEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Optional: Validate phone format (basic check for numbers only)
function validatePhone(phone) {
    const phonePattern = /^[0-9]{10}$/; // Adjust this pattern based on requirements
    return phonePattern.test(phone);
}


// Function to open and close the modal
function openModal() {
    document.getElementById("myModal").style.display = "block";
}

function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

// Function to update the country code
function updateCountryCode() {
    var newCountryCode = document.getElementById("modal-country-code").value;
    if (/^\+\d{1,5}$/.test(newCountryCode)) {  // Check if the input is a valid country code format
        document.getElementById("country-code").innerText = newCountryCode; // Update the label
        closeModal();
    } else {
        alert("Please enter a valid country code (e.g., +91).");
    }
}

// Function to share the link on WhatsApp
function shareOnWhatsApp(event) {
    event.preventDefault();  // Prevent default anchor behavior

    // Get the input phone number
    var inputNumber = document.getElementById("whatsapp-input").value;
    var countryCode = document.getElementById("country-code").innerText || "+91"; // Default country code

    // Ensure the phone number has 10 digits
    if (inputNumber.length === 10) {
        // Construct the WhatsApp share URL with the current URL included in the message
        var currentUrl = window.location.href;
        var message = `Check this  link for reach this person card f: ${currentUrl}`;
        var whatsappUrl = `https://wa.me/${countryCode}${inputNumber}?text=${encodeURIComponent(message)}`;

        // Open WhatsApp share URL in a new tab
        window.open(whatsappUrl, '_blank');
    } else {
        alert("Please enter a valid 10-digit mobile number.");
    }
}

// Function to download the premium card
function downloadPremiumCard(id, theme) {
    const cardElement = document.getElementById('card-container');
    html2canvas(cardElement).then(canvas => {
        const imageUrl = canvas.toDataURL('image/png');
        const downloadLink = document.createElement('a');
        downloadLink.href = imageUrl;
        downloadLink.download = `premium_card_${id}.png`; // Adjust as necessary
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    }).catch(error => {
        console.error('Error converting the card to an image:', error);
    });
}
