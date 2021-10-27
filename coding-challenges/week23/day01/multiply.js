function multiply(a,b){
    function innermultiply(x){
        return a * x ;
    }
    if (a && b) return a * b ;
    else if (a) return innermultiply;
    else return ("Please provide atleast 1 argument")
}

console.log(multiply(4,5));
console.log(multiply(3,3));
console.log(multiply());

const double = multiply(2);
console.log(double(5));
console.log(double(11));


