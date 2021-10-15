
function checkpalindrome(a){
    var i = 0;
    var j = a.length-1;
    
    while(i<j){
        if(a[i] != a[j]){
            return 'not palindrome';
        }
        i++;
        j--; 
    }
    return 'is palindrome'
}
var a = 'nitin';
console.log(checkpalindrome(a));