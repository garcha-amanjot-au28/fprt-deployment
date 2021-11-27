var a = document.getElementById("a")
var b = document.getElementById("b")
var c = document.getElementById("c")
var  d = document.getElementById("d")
var e = document.getElementById("e")
var f = document.getElementById("f")
var g = document.getElementById("g")
var h = document.getElementById("h")
var i = document.getElementById("i")
var k = document.getElementById("k")


var list = [];
let getinfo = () => {
    fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(val => {
    //     for (var x in val){
    //         list.append(val[x].name);
    //     }
        a.innerHTML = val[1].name
        b.innerHTML = val[2].name
        c.innerHTML = val[3].name
        d.innerHTML = val[4].name
        e.innerHTML = val[5].name
        f.innerHTML = val[6].name
        g.innerHTML = val[7].name
        h.innerHTML = val[8].name
        i.innerHTML = val[9].name
        k.innerHTML = val[10].name
        
            
    });
}
function myFunction() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
getinfo();