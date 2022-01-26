// function multiples (n){
//     for (var i = 1 ; i < n+1 ; i++){
//         if (i % 3 == 0 && i % 5 == 0 ) console.log("FizzBuzz");
//         else if (i%3 == 0) console.log("Fizz");
//         else if (i%5 == 0) console.log("Buzz");
//         else console.log(i)
//     }
// }


// console.log(multiples(100))

// var bal = (function(){
//     var balance = 0

//     function changebalance(amt){
//         balance+=amt 
//     }
//     return{
//     increase : function(){
//         changebalance(1)
//     },
//     decrease : function(){
//         changebalance(-1)
//     },
//     value:function(){
//         return balance
//     }
//     }
// })()

// console.log(bal.value())
// bal.increase()
// console.log(bal.value())

var now = new Date()
console.log(now)
var now2 = new Date("2020-11-07")
console.log(now2)