
let find = document.querySelector('#submit')

function hamming (){
    let string1 = document.querySelector('#string1').value
    let string2 = document.querySelector('#string2').value
    console.log(string1)
    var count = 0;
    
    for(i = 0; i < string1.length; i++){
        if (string1[i] !== string2[i]) count += 1;
    }
    console.log(count)
    document.getElementById('res').value = count;
}

document.addEventListener('DOMContentLoaded',function(){
    find.addEventListener('click',hamming)
});