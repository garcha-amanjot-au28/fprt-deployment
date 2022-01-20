let string = prompt("Please enter a string ");
let len = string.length;
function checkPalindrome(string, len){
    let i = 0
    let j = len-1
    while(i<j){
        if(string[i] !== string[j]){
            return `${string} is not a Palindrome`
        }
        i++;
        j--;
    }
    return `${string} is a valid Palindrome`
};

let ans = checkPalindrome(string,len);

alert(ans)