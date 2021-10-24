function hamming (arr1,arr2){
    
    var count = 0;

    for(i = 0; i < arr1.length; i++){
        if (arr1[i] !== arr2[i]) count += 1;
    }
    return "Hamming Distance between the two strings is = "+count;

} 

console.log(hamming("equality","equalize"));
//document.getElementById("hamming").innerHTML = hamming("equality","equalize");
document.write(hamming("equality","equalize"));
window.alert(hamming("equality","equalize"));