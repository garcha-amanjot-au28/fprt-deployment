const button1 = document.getElementById('btn1');
const button2 = document.getElementById('btn2');
const button3 = document.getElementById('btn3');
const button4 = document.getElementById('btn4');
const button5 = document.getElementById('btn5');
const button6 = document.getElementById('btn6');
const button7 = document.getElementById('btn7');
const button8 = document.getElementById('btn8');
var list = document.getElementById('list')

cart = []

async function fetchData(){
const response = await fetch('https://fakestoreapi.com/products?limit=8');
const json = await response.json()
console.log(json)
printData(json)
return json
}



const data = fetchData()

function printData(data){

    button1.addEventListener('click',() =>{
        cart.push(data[0])
        addItem(data[0])
    })
    button2.addEventListener('click',() =>{
        cart.push(data[1])
        addItem(data[1])
    })
    button3.addEventListener('click',() =>{
        cart.push(data[2])
        addItem(data[2])
    });
    button4.addEventListener('click',() =>{
        cart.push(data[3])
        addItem(data[3])
    })
    button5.addEventListener('click',() =>{
        cart.push(data[4])
        addItem(data[4])
    })
    button6.addEventListener('click',() =>{
        cart.push(data[5])
        addItem(data[5])
    })
    button7.addEventListener('click',() =>{
        cart.push(data[6])
        addItem(data[6])
    })
    button8.addEventListener('click',() =>{
        cart.push(data[7])
        addItem(data[7])
    })
    console.log(data)
}

function addItem(entry){
    
    
    
    // if (item == ''){
    //     alert('Please enter a todo item and then click add button')
    //     return
    // }
    // console.log(item)
    var newSpan = document.createElement('span');
    var title = document.createElement('h6');
    
    title.innerHTML = entry.title;
    // newSpan.style.position= 'absolute';
    // newSpan.style.right = '0';
    var price = document.createElement('input');
    price.style.margin = "10px";
    price.readOnly = true;
    price.style.width = "70px";
    price.value ='$' +entry.price
    var quantity = document.createElement('input');
    quantity.style.width = "50px";
    quantity.type = 'number';
    quantity.id = 'qty';
    quantity.value = 1;
    var removebutton = document.createElement('button');
    removebutton.style.marginLeft = "10px";
    var label = document.createElement('label');
    label.setAttribute('for',"qty");
    label.innerHTML = '   Qty :';
    label.style.marginLeft = "5px";
    var subTotal  =  document.createElement('h6');
    subTotal.style.display = 'inline';
    subTotal.style.margin = "10px";
    subTotal.innerHTML = '  Sub-Total$  ' + entry.price * quantity.value;
    
    
    quantity.addEventListener('change',function(){
        subTotal.innerHTML = '  Sub-Total$  ' + entry.price * quantity.value;

    });
    
    removebutton.innerHTML = 'Delete';
    removebutton.addEventListener('click',function(){
        newLiItem.remove();
        
    })
    var newLiItem = document.createElement('Li');
    // newLiItem.innerHTML = entry.title;
    
    
    newSpan.append(title);
    newSpan.append(price);
    newSpan.append(label); 
    newSpan.append(quantity);
    newSpan.append(removebutton);
    newSpan.append(subTotal);  
    newLiItem.append(newSpan);
    list.append(newLiItem);
    
   
    
    // todobutton.disabled = true;
}

