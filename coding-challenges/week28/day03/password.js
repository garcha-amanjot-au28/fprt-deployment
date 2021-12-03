console.log("hello")
// let passwordlength = document.getElementById("length").value

let upper = document.getElementById("uppercase")
let lower = document.getElementById("lowercase")
let number = document.getElementById("numbers")
let symbols = document.getElementById("symbols")
let button = document.getElementById("button")


function displaypassword(password){
    console.log(password);
    document.getElementById("input").value = password;
}



function generatepassword(){
    let passwordlength = document.getElementById("length").value
    console.log(passwordlength)
    var chars = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let numerics = "0123456789";
    let letters = "abcdefghijklmnopqrstuvwxyz";
    let capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let symbols = "!@#$%^&*()";
    let password = "";

    for (var i = 0 ; i <=passwordlength;i++) {

        var randomNumber = Math.floor(Math.random() * chars.length);
        password += chars.substring(randomNumber, randomNumber +1);
    
    }
    displaypassword(password)
}

button.addEventListener('click',generatepassword)