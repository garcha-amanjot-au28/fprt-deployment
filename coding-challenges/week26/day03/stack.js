let push = document.querySelector('#push')
let pop = document.querySelector('#pop')
let stack = [];
console.log(push)

function addtostack (){
    let item = document.getElementById('number').value;
    console.log(item)
    stack.push(item)
    document.getElementById('result').innerHTML = stack;
}


document.addEventListener('DOMContentLoaded',function(){
    push.addEventListener('click',addtostack)

});
pop.addEventListener('click', function(){
    if (stack != []) stack.pop();
    document.getElementById('result').innerHTML = stack;
    
})


