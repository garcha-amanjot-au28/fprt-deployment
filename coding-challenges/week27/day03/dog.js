const getdog = document.getElementById("getdog")
const dogimg = document.getElementById('dogimg')

getdog.addEventListener('click',getRandomDog)

function getRandomDog(){
    fetch("https://dog.ceo/api/breeds/image/random")
    .then(res => res.json())
    .then(val => {

            dogimg.innerHTML = `<img src = "${val.message}"> `
        })
}




