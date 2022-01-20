let num = prompt("Please enter a number");
num = num.toString();
let len = num.length;

function checkArmstrong(num,len){
    let sum = 0;
    for(let i = 0 ; i < len ; i++){
        sum += num[i]**len
    };
    if (sum != num){
        return `${num} is not an Armstrong Number`
    };
    return `${num} is an Armstrong Number`
;}

let ans = checkArmstrong(num,len);

alert(ans);