
// Generic functions

const isRequired = value => value === '' ? false : true;

const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};


const isPasswordSecure = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return re.test(password);
};

const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    input.classList.remove('success');
    input.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    input.classList.remove('error');
    input.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}


const checkInputField = (usernameEl) => {

    let valid = false;
    
    const username = usernameEl.value.trim();

    if (!isRequired(username)) {
        showError(usernameEl, 'This field cannot be blank.');
    } else {
        showSuccess(usernameEl);
        valid = true;
    }
    return valid;
}


const checkNumberField = (usernameEl) => {

    let valid = false;
    
    const username = usernameEl.value.trim();

    if (!isRequired(username)) {
        showError(usernameEl, 'Enter a number in this field.');
    } else {
        showSuccess(usernameEl);
        valid = true;
    }
    return valid;
}



const checkEmail = (emailEl) => {
    let valid = false;
    const email = emailEl.value.trim();
    if (!isRequired(email)) {
        showError(emailEl, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showError(emailEl, 'Email is not valid.')
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
}


const checkPassword = (passwordEl) => {

    let valid = false;

    const password = passwordEl.value.trim();

    if (!isRequired(password)) {
        showError(passwordEl, 'Password cannot be blank.');
    } else if (!isPasswordSecure(password)) {
        showError(passwordEl, 'Password must have at least 8 characters that include at least 1 lowercase character, 1 uppercase character, 1 number, and 1 special character in (!@#$%^&*)');
    } else {
        showSuccess(passwordEl);
        valid = true;
    }

    return valid;
};


const checkConfirmPassword = (confirmPasswordEl) => {
    let valid = false;
    // check confirm password
    const confirmPassword = confirmPasswordEl.value.trim();
    const password = passwordEl.value.trim();

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordEl, 'Please enter the password again');
    } else if (password !== confirmPassword) {
        showError(confirmPasswordEl, "Passwords don't match");
    } else {
        showSuccess(confirmPasswordEl);
        valid = true;
    }
    return valid;
};


function CheckFileUpload(fileUploaded){
	valid=true
    if(fileUploaded.files.length === 0){
        showError(fileUploaded, 'Please upload a file');
        fileUploaded.focus();
        valid=false;
    }
    else{
    	showSuccess(fileUploaded)
    }
    return valid
}
