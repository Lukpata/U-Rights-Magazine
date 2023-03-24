
// For registration form

let registrationForm=document.forms["registration-form"]
let firstName=registrationForm.firstName
let lastName=registrationForm.lastName
let country=registrationForm.country
let emailEl=registrationForm.email
let passwordEl=registrationForm.password
let confirmPasswordEl=registrationForm.confirmation

// Adding an eventlistener to validate redgistration form
registrationForm.addEventListener('submit', function (e) {
    // validate forms
    let isEmailValid;
    let isFirstNameValid;
    let isLastNameValid;
    let isPasswordValid;
    let isConfirmPasswordValid;
    let isCountryValid;

    	isFirstNameValid = checkInputField(firstName),
    	isCountryValid = checkInputField(country),
    	isLastNameValid = checkInputField(lastName),
        isEmailValid = checkEmail(emailEl),
        isPasswordValid = checkPassword(passwordEl),
        isConfirmPasswordValid = checkConfirmPassword(confirmPasswordEl);

    let isFormValid = isFirstNameValid &&
        isEmailValid &&
        isPasswordValid &&
        isConfirmPasswordValid && isLastNameValid && isCountryValid;

    if (!isFormValid) {
    	e.preventDefault();
    }
});

// For instant feedback of registration form

registrationForm.addEventListener('input', function (e) {
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

        case 'country':
            checkInputField(country);
            break;

        case 'password':
            checkPassword(passwordEl);
            break;

        case 'confirmation':
            checkConfirmPassword(confirmPasswordEl);
            break;
    }
});


// For loading the countries select control

window.addEventListener('load',()=>{
    fetch('https://restcountries.com/v3.1/all').then((response)=>{
        return response.json()
    }).then((data)=>{
        let output=[];
        let outputData="";
        data.forEach((countries)=>{
            output.push(countries.name['common'])
        })
        output.sort()
        for (let i=0;i<output.length;i++) {
            outputData+=`<option>${output[i]}</option>`
        }
        country.innerHTML=outputData;
    }).catch((error)=>{
        console.log(error)
    })

})