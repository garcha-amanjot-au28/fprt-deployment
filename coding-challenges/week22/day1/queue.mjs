

let push = document.querySelector('#push')
let pop = document.querySelector('#pop')
let reset = document.querySelector('#reset')
let res = document.getElementById('result')
let queue = [];

// console.log(push)

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


// // document.addEventListener('DOMContentLoaded',function(){
// //     push.addEventListener('click',addtostack)

// // });
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



// console.log("Line 1");

// let myPromise = new Promise(function (resolve, reject){
//     // resolve("Line2");
//     reject("It was rejected")
// })


// console.log("LIne3")


// myPromise.then((val) =>{
//     console.log(val)
// });


// myPromise.catch((val) =>{
//     console.log(val)
// });


// fetch('https://jsonplaceholder.typicode.com/todos/1')
// .then((response) => console.log(response))
// .then((data) => console.log(data)); 

// function translatePigLatin(str) {
//     let vowels = ['a','e','i','o','u'];
//     let conts = '';
//     let rest = '';
    
    
//     if(vowels.includes(str[0])===true){
        
//       return str + 'way';
//     }
    
    
//     for (let i = 0; i<str.length; i++){
        
//         if ( vowels.includes(str[i]) === false && i !== str.length-1){
                
//             conts = conts + str.slice(i , i+1);
//             }
//         else if (vowels.includes(str[i]) === false){
            
//             conts = conts + str.slice(i);
//             }
//         else {
//             return  rest = rest + str.slice(i) + conts +'ay';
            
//             }
//     }
    
//     return str + 'ay';
//   }
  
//   console.log(translatePigLatin("rhythm"));


// function factorialize(num) {
//     if (num === 0){
//       return 1;
//     }
//     else {
//         return num * factorialize(num-1);
//     }
// }
// factorialize(5);

// let string = 'aA';

// let caps = string[1].toUpperCase() ;    

// console.log(string, caps);

// const str = 'captain picard';

// const caps = str.charAt(0).toUpperCase() + str.slice(1);
// console.log(caps);

// let a = "hello World";

// console.log(a);

// a = a.split(" ");

// console.log(a);

// let b = 'a-b-c-d-e';

// console.log(b);
// b = b.split("-");
// console.log(b);

// function titleCase(str) {
//     let a = str.split(" ");
    
//     for (let i = 0 ; i<a.length;i++){
//         // console.log(a[i])
//         // console.log(a[i][0])
//       if(a[i].length === 1){
//         a[i] = a[i].toUpperCase();
//       }
//       else {
//       a[i] = a[i][0].toUpperCase() + a[i].slice(1).toLowerCase();
//       }
      
//     }
//     str = a.join(' ');
//     return str;
//   }
  
//   console.log(titleCase("I'm a little tea pot"));


  // function bouncer(arr) {
  //   let arra =[];
  //   for(let i in arr){
      
  //     if(typeof arr[i] === 'string' && arr[i] !=='') arra.push(arr[i]);
  //     else if(arr[i] == false ||  arr[i] == undefined || arr[i] ==null || isNaN(arr[i])) continue;
  //     else arra.push(arr[i]);
  //   }
  //   return arra;
  // }
  // console.log(bouncer([7, "ate", "", false, 9]));

  // let myPromise =  new Promise((resolve, reject) => {
  //   resolve('this promise is resolved')
  //   resolve('this promise is resolved');
  // })

  // myPromise 
  // .then((val) => console.log(val))

  // const promise1 = Promise.reject("First Promise");

  // const promise2 = new Promise((resolve, reject) => {
  //   setTimeout(resolve, 500, "second promise")
  // })

  // const promise3 = new Promise((resolve, reject) => {
  //   setTimeout(resolve, 1000, "third promise")
  // })


  // Promise.all([promise1,promise2,promise3]).then((val) => {
  //   console.log(val);
  // });

  // Promise.any([promise1,promise2,promise3])
  // .then((val) => {
  //   console.log(val);
  // });
  
  // 
  
  // let arr = [1,2,3,4];

  // let iteratorObj = arr[Symbol.iterator]();

  // console.log(iteratorObj.next());

  // localStorage.setItem('str',"hey guys");
  // localStorage.setItem('num',25);
  // localStorage.setItem('str',"hey guys");
  // localStorage.setItem('obj', JSON.stringify({name:"aman",age:22}));

  // let num = localStorage.getItem('num');

  // let obj = localStorage.getItem('obj');

  // console.log(obj);

  // console.log(JSON.parse(obj));

  // console.log(num);

  // localStorage.removeItem('num');

//   const promise3 = new Promise((resolve, reject) => {

//     setTimeout(resolve, 2000, 'Third Promise.')

// });

 

// const promise4 = new Promise((resolve, reject) => {

//     setTimeout(reject, 4000, 'Fourth Promise.')

// });

// function* child(){
//   console.log('child called')
//   yield 22;
// }

// function* generator ( num2, num3){
//     console.log('Number 1')
//     yield* child();
//     console.log('NUmber 2')
//     yield num2
//     console.log('Number 3')
//     yield num3
// }

// let gen = generator(2,3)

// console.log(gen.next().value);
// console.log(gen.next().value);
// console.log(gen.next().value);
