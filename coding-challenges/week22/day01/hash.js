function backspacehash(a){
    var res = '';
    var rem = '';
    for (var i = 0 ; i < a.length;i++){
        if (a[i] === '#' && res !== ''){
            rem += res.slice(res.length-1);
            res =   res.slice(0,res.length-1);
        }else{
            res += a[i];
        }
    }
    return ['Correct processed string = '+res , "Deleted String = "+rem ];

}

var a = "abc#d##c";
console.log(backspacehash(a));