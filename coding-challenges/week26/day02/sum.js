

var Sumi = document.getElementById('btn');


function dosum (){
    var Num1 = parseInt(document.getElementById('num1').value);
    console.log(Num1)
    var Num2 = parseInt(document.getElementById('num2').value);
    var result = document.getElementById('result').value = Num1 + Num2;
    
    

}
document.addEventListener('DOMContentLoaded' , function(){
    if (Sumi){
    Sumi.addEventListener('click' , dosum)
    }
});