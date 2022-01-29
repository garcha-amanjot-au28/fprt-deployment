let string = document.querySelector('#string');

let output = document.querySelector('#output');

let get = document.querySelector('#get');


get.addEventListener('click',() => {
    let str = string.value;
   let updated = [];
   if(str[0] !== '#'){
       updated.push(str[0])
   }
    console.log(str);
    for(let i = 1 ; i<str.length;i++){
        if (str[i]==='#' && updated !== []){
            updated.pop()
            
        }
        else{
            updated.push(str[i])
        }
    }
    console.log(updated)
    updated = updated.join("");
    output.innerHTML = updated;
})