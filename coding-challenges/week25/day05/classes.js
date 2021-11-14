console.log("hello")
class Person{
    constructor(name,age){
        this.name = name
        this.age = age
    }
    outout(){
        console.log(this.name)
    }


    
}

class Employee extends Person{
    constructor(name,age,id){
        super(name,age)
        this.id = id
    }
}
class Admin extends Person{
    constructor(name,age,admin){
        super(name,age)
        this.admin = admin
    }
    update(){
        this.name = "sooraj"
        this.admin = "neeraj"
        console.log(this.name,this.admin)
    }
}
let test = new Employee("aman","22",123)
test.outout();  
let test2 = new Admin("jai","33","sid")
console.log(test2.name,test2.admin)
test2.update()