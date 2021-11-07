function Sum(n, callback) {
    var Total = 0
    f = n.toString()
    
    N = f.length
    
    if (f.length == 1 ) return 1;
    for (var i=0; i<N; i++) {
        
        Total =  Total + parseInt(f[i])

    }
    
    return callback(Total)

}

function checkPalindrome(Total){
    
    var i = 0
    

    
    res = Total.toString()
    
    var j = res.length -1
    
    while (i<j){
        
        
        if (res[i] != res[j]) return 0
        i+=1
        j-=1
    }
    return 1
}


console.log("Output for 56  = "+ Sum(56,checkPalindrome))
console.log("Output for 66 =  "+ Sum(66,checkPalindrome))
console.log("Output for 12345 = "+ Sum(12345,checkPalindrome))
console.log("Output for 38 = "+ Sum(38,checkPalindrome))