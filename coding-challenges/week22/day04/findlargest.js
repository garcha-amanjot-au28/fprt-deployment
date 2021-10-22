function findlargest(arr){
    var max = Number.NEGATIVE_INFINITY;
    for (var i = 0 ; i < arr.length ; i++){
        //console.log(arr[i]);
        if (arr[i] > max) max = arr[i];
    } 
    return max;
}
//var arr= [-5, -2, -6, 0, -1]
window.alert("The Maximmum number is =  " + findlargest([-5, -2, -6, 0, -1]));