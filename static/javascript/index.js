// Javascript code for header and footer
let searchForm;
searchForm=document.forms["search-form"]
searchForm.addEventListener('submit',(e)=>{
	let searchFormInput=document.getElementById('search-form-input').value
	if((searchFormInput.trim()).length==0){
		e.preventDefault()
	}
	
})

function show(){
	let donateButton=document.querySelector(".donate")
	donateButton.classList.toggle("hide-donate")
	searchForm=document.forms["search-form"]
	searchForm.classList.toggle("show")
}

function toggleFormIcons(){
	let closeIcon;
	let searchIcon;
	searchIcon=document.querySelector(".search")
	closeIcon=document.querySelector(".close-icon")
	searchIcon.classList.toggle('dont-show')
	closeIcon.classList.toggle('dont-show')
}

function hamburgerMenu(e){
	let menu;
	menu=document.querySelector(".main-menu");
	menu.classList.toggle('show-menu');
	e.target.classList.toggle("close")
}

// Hamburger Menu
let hamburger=document.querySelector(".hamburger")
hamburger.addEventListener('click',hamburgerMenu)

// Event for the search form
let showSearchForm=document.querySelector('.show-search-form')
showSearchForm.addEventListener('click',show)
showSearchForm.addEventListener('click',toggleFormIcons)


