function grades (marks){
    for (var i in marks){
        var j = marks[i];
        switch(j){
            case (j < 60)  && j :
                output = i + "'s grade is F";
                break;
            case (j < 70) && j :
                output = i + "'s grade is D";
                break;
            case (j < 80) && j  :
                output = i + "'s grade is C";
                break;
            case (j < 90) && j  :
                output = i + "'s grade is B";
                break;
            case (j < 100) && j :
                output = i + "'s grade is A";
                break;
            
        }
        console.log(output);
    }
}
var numbers = {
    David : 80,
    Vinoth : 77,
    Divya : 88,
    Ishitha : 95,
    Thomas : 68,
};
grades(numbers);