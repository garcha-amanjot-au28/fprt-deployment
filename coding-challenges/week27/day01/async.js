let products = [{name:"ac", cost:"60"},{name:"cooler",cost:"10"},{name:"waterfilter",cost:"20"}]


function getproducts(){
    setTimeout(() => {
        let res = '';
        products.forEach((items,idx)=>{
        res += `<li>${products[idx].name}</li>`
        
        })
        document.body.innerHTML = res

    },2000 );
}
function createproducts(product){
    console.log(product)
    return new Promise((success,failure)=>{
        setTimeout(()=>{
            products.push(product);

            let error = false
            success();
            if(!error){
            }
            else{
                failure('Error from Database')
            }
        },3000)
    })
}


async function result(){
    await createproducts({name:"laptop",cost:"500"});
    getproducts();
}

result();

