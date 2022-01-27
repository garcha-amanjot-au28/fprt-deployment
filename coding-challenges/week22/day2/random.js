const generate = document.querySelector('#generate');
let col1 = document.querySelector("#color1");
let ran = [];

// col1.style.backgroundColor = ran[0];
function randomColors(){
    
    for(let i = 0 ; i<5;i++){
    const random = Math.floor(Math.random()*16777215).toString(16);
    ran.push('#' + random);
    }
    
}
console.log(ran);
generate.addEventListener('click',randomColors);
generate.addEventListener('click',function(){
    document.querySelector(".cols div:nth-child(1)").style.backgroundColor = ran[0];
    document.querySelector(".cols div:nth-child(2)").style.backgroundColor = ran[1];
    document.querySelector(".cols div:nth-child(3)").style.backgroundColor = ran[2];
    document.querySelector(".cols div:nth-child(4)").style.backgroundColor = ran[3];
    document.querySelector(".cols div:nth-child(5)").style.backgroundColor = ran[4];
    ran = [];
})