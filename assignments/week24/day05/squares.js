function squares(n,perfectsquares){
    
    count = 0
    for (var i = 0; i <perfectsquares.length;i++){
        if (perfectsquares[i] < n) count+=1
        else return count
    }
}


var     perfectsquares = []
n =  1000000
for (i=1;i<=n;i++){
    perfectsquares.push(i*i)
    
}

console.log(squares(9,perfectsquares))
console.log(squares(10,perfectsquares))
console.log(squares(1,perfectsquares))
console.log(squares(3,perfectsquares))