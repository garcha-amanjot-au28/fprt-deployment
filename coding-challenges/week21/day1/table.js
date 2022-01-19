const input = prompt("please enter number to display its table");

let limit = prompt("Please enter till what to display table");

function displayTable(table, limit){
    if(limit == false){
        limit = 10;
    }
    for (let i = 1;i<= limit;i++){
        
        console.log(`${table} * ${i} = ${table*i}`)

    }
    
}




console.log(limit);
displayTable(input,limit);