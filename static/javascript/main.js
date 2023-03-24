// Javascript code for the main section



// For slideshow

let index = 0;  
slideShow(index);  

 function init(){
    setInterval("slideShow(1)",7000)
 }
 

 function slideShow(n){
    let sliderImage=document.getElementsByClassName('slider-image');
    let paragraph=document.getElementsByClassName('snippets');
    index+=n;
    if (index>=sliderImage.length){
        index=0
    }
    if (index<0){
        index=(sliderImage.length)-1;
    }
    for(i=0;i<paragraph.length;i++){
        paragraph[i].style.display='none';
        sliderImage[i].style.display='none'
    }
    paragraph[index].style.display="block";
    sliderImage[index].style.display="block";
 }

 window.addEventListener("load",init)

 let next=document.querySelector('.next')
 let previous=document.querySelector('.previous')

 next.addEventListener('click',()=>{
    slideShow(1)
 })

 previous.addEventListener('click',()=>{
    slideShow(-1)
 })


//  For growing circles
function growCircle(n){
	let circle=document.getElementsByClassName('circle')
	for(let i=0;i<circle.length;i++){
		setTimeout(() => {
			circle[i].style.height=60+"px";
			circle[i].style.width=60+"px"
		}, n);
		n+=4000;
	}

	for(let j=0;j<circle.length;j++){
		circle[j].style.height=0;
		circle[j].style.width=0;
	}
}

function growCaller(){
	setInterval(() => {
		growCircle(3000)
	}, 10000);
}

window.addEventListener('load',growCaller)