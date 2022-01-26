let push = document.querySelector('#push')
let pop = document.querySelector('#pop')
let reset = document.querySelector('#reset')
let res = document.getElementById('result')
let queue = [];

console.log(push)

function addtoqueue (){
    let item = document.getElementById('number');
    console.log(item.value)
    
    queue.push(item.value)
    var node = document.createElement("P");
    var node1 = document.createElement("Span");
    var node2 = document.createElement("Span");
    var node3 = document.createElement("Span");
    for (let i = 0 ; i<queue.length;i++){
        
        if(i===0){
            
            node1.style.color = 'red';
            var textnode = document.createTextNode(queue[i])
            var comma = document.createTextNode(',')
            node1.append(textnode);
            node1.append(comma);
            node.append(node1)
        }
        else if(i === (queue.length-1)){
            
            node2.style.color = 'green';
            var textnode = document.createTextNode(queue[i])
            node2.append(textnode);
            node.append(node2)
        }
        else{
            
            node3.style.color = 'black';
            var textnode = document.createTextNode(queue[i])
            var comma = document.createTextNode(',')
            
            node3.append(textnode);
            node3.append(comma);
            node.append(node3)

        }
        // var textnode = document.createTextNode(queue[i])
        // node1.append(textnode);
        // node.append(node1)
        
        // res.append(node);
        
        
    }
    console.log(node);
    res.innerHTML = '';
    res.append(node);
    
    
    // res.style.color = 'red';
    item.value = '';
}


// document.addEventListener('DOMContentLoaded',function(){
//     push.addEventListener('click',addtostack)

// });
push.addEventListener('click',addtoqueue)
reset.addEventListener('click',function(){
    res.innerHTML = '';
})
pop.addEventListener('click', function(){
    if (queue != []) queue.shift();
    // res.innerHTML = queue;
    var node = document.createElement("P");
    var node1 = document.createElement("Span");
    var node2 = document.createElement("Span");
    var node3 = document.createElement("Span");
    for (let i = 0 ; i<queue.length;i++){
        
        if(i===0){
            
            node1.style.color = 'red';
            var textnode = document.createTextNode(queue[i])
            var comma = document.createTextNode(',')
            node1.append(textnode);
            node1.append(comma);
            node.append(node1)
        }
        else if(i === (queue.length-1)){
            
            node2.style.color = 'green';
            var textnode = document.createTextNode(queue[i])
            node2.append(textnode);
            node.append(node2)
        }
        else{
            
            node3.style.color = 'black';
            var textnode = document.createTextNode(queue[i])
            var comma = document.createTextNode(',')
            
            node3.append(textnode);
            node3.append(comma);
            node.append(node3)

        }
        // var textnode = document.createTextNode(queue[i])
        // node1.append(textnode);
        // node.append(node1)
        
        // res.append(node);
        
        
    }
    console.log(node);
    res.innerHTML = '';
    res.append(node);
    
    
    // res.style.color = 'red';
    item.value = '';

    
})


