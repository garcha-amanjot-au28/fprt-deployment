function armstrong(start , end){

    for (var i = start ; i <= end;i++){
        var a = i.toString();
        var b = 0;
        for (var j = 0 ; j< a.length ; j++){
            b += a[j]**3;
        }
        if (b == i) console.log(i);
    }

}
armstrong(100,999);