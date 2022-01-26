// function armstrong(start , end){

//     for (var i = start ; i <= end;i++){
//         var a = i.toString();
//         var b = 0;
//         for (var j = 0 ; j< a.length ; j++){
//             b += a[j]**3;
//         }
//         if (b == i) console.log(i);
//     }

// }


function armstrong(start,end){
    for (var i = start; i<=end; i++){
        var res = [];
        let  a = i.toString();
        let b = Object.assign([],a);
        var c = b.map(function(item){
            return item**3;
        });
        var d = c[0] + c[1] +c[2];
        if ( d == i) console.log(i);
        
    }

}
armstrong(100,999);

// function nums(numbers){
    

//     var sqnumbers = 0;

//     var sqnumbers = numbers.map(function(item){
//         return item**3;
//     });
//     return sqnumbers
// }
// numbers = [1,2,3,4,5,6];
// console.log(nums(numbers));