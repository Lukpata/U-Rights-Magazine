
// For submission form

let submitForm=document.forms["submit-form"]
let firstName=submitForm.firstName
let lastName=submitForm.lastName
let emailEl=submitForm.email
// let bio = tinyMCE.get('tinyeditor').getContent()
let file=submitForm.file

// Adding an eventlistener to validate submission form
submitForm.addEventListener('submit', function (e) {
    // validate forms
    let isEmailValid;
    let isFirstNameValid;
    let isLastNameValid;
    let isFileValid;

    	isFirstNameValid = checkInputField(firstName);
    	isLastNameValid = checkInputField(lastName);
        isEmailValid = checkEmail(emailEl);
        isFileValid=CheckFileUpload(file)
        // isBioValid = checkInputField(bio);

    let isFormValid = isFirstNameValid &&
        isEmailValid && isLastNameValid && isFileValid
        

    if (!isFormValid) {
    	e.preventDefault();
    }
});

// For instant feedback of submit form

submitForm.addEventListener('input', function (e) {
    switch (e.target.id) {
        case 'first-name':
            checkInputField(firstName);
            break;

        case 'last-name':
            checkInputField(lastName);
            break;

        case 'email':
            checkEmail(emailEl);
            break;

        case 'file':
            CheckFileUpload(file);
            break;
    }
});
