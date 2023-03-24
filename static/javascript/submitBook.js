
// For registration form

let submitBook=document.forms["submitBookForm"]
let bookTitle=submitBook.bookTitle
let publisher=submitBook.publisher
let author=submitBook.author
let year=submitBook.year
let pages=submitBook.pages
let price=submitBook.price
let url=submitBook.url
let file=submitBook.file
let plan=submitBook.plan

let pricediv=document.getElementById('price')
let urldiv=document.getElementById('url')

for (let i=0;i<plan.length;i++) {
    plan[i].addEventListener('click',(e)=>{
        if (e.target.id=="free") {
            pricediv.classList.add("hidden-controls")
            urldiv.classList.remove("hidden-controls")
        }else{
            pricediv.classList.remove("hidden-controls")
            urldiv.classList.add("hidden-controls")
        }
    })
}

window.addEventListener('load',()=>{
    let free=document.getElementById('not-free')
    free.checked=true;
})



// Adding an eventlistener to validate redgistration form
submitBook.addEventListener('submit', function (e) {
    // validate forms
    let isBookTitleValid;
    let isPublisherValid;
    let isAuthorValid;
    let isYearValid;
    let isPagesValid;
    let isPriceValid;
    let isFileValid;

    	isBookTitleValid = checkInputField(bookTitle),
    	isPublisherValid = checkInputField(publisher),
    	isAuthorValid = checkInputField(author),
        isYearValid = checkNumberField(year),
        isPagesValid = checkNumberField(pages),
        isPriceValid = pricediv.classList.contains('hidden-controls')? true: checkNumberField(price);
        // isPriceValid = price!==null? checkNumberField(price):true;
        isFileValid=CheckFileUpload(file)



    let isFormValid = isBookTitleValid &&
        isPublisherValid &&
        isAuthorValid &&
        isYearValid && isPagesValid && isPriceValid;

    if (!isFormValid) {
    	e.preventDefault();
    }
});

// For instant feedback of book submission form

submitBook.addEventListener('input', function (e) {
    switch (e.target.id) {
        case 'book-title':
            checkInputField(bookTitle);
            break;

        case 'publisher':
            checkInputField(publisher);
            break;

        case 'author':
            checkInputField(author);
            break;

        case 'year':
            checkNumberField(year);
            break;

        case 'pages':
            checkNumberField(pages);
            break;

        case 'price-input':
            checkNumberField(price);
            break;

        case 'file':
            CheckFileUpload(file);
            break;
    }
});
