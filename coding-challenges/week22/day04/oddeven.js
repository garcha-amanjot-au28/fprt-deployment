function oddeven(){
    res = [];
    for (i= 0 ; i < 16; i++){
   
        if (i % 2 == 0) { 
            res.push(i + " is a an even number.");
        }
        else {
            res.push(i + " is an odd number.");
        }
        
    }
    //return res.join('\r\n');
    return res;

    
    
}

//console.log(oddeven());
result = oddeven();
console.log(result);
result2 = result.split(',').join("<br />"));
document.write(result2);