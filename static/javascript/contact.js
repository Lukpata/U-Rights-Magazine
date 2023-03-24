
// Validation for contact forms
let contactForm=document.forms["contactForm"]
let fullName=contactForm.fullName
let contactEmail=contactForm.email
let message=contactForm.message

contactForm.addEventListener('submit', function (e) {
    // validate forms
    let isFullNameValid;
    let isContactEmailValid;
    let isMessageValid;
    

    	isFullNameValid = checkInputField(fullName),
    	isMessageValid = checkInputField(message),
        isContactEmailValid = checkEmail(contactEmail)
        

    let isFormValid = isFullNameValid &&
        isContactEmailValid &&
        isMessageValid;
        

    if (!isFormValid) {
    	e.preventDefault();
    }
});



// For instant feedback of contact form

contactForm.addEventListener('input', function (e) {
    switch (e.target.id) {
        case 'fullName':
            checkInputField(fullName);
            break;

        case 'email':
            checkEmail(contactEmail);
            break;

        case 'message':
            checkInputField(message);
            break;
    }
});
