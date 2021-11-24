let products =[{name : "fridge" ,cost :"20" }, {name:"videogame",cost:"10"}]


function getproducts(){
    setTimeout(() => {
        let result = '';
        products.forEach((item,idx)=>{
            
            result += `<li>${item.name}</li>`

        })
        document.body.innerHTML = `Using Callback function`+ result 
    },2000
    )
}
//Below passing getproducts as a callback function to createproducts so that it will only get executed once createproducts is 
// executed. 
function createproducts(items,callback){
    setTimeout(()=>{
        products.push(items)
        callback()
    },3000
    )
    
}

createproducts({name:"tv",cost:"50"},getproducts);
