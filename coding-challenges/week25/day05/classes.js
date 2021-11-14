console.log("hello")
class Person{
    constructor(name,age){
        this.name = name
        this.age = age
    }
    outout(){
        console.log(`Employee name is ${this.name} and age is ${this.age}`)
    }


    
}

class Employee extends Person{
    constructor(name,age,id){
        super(name,age)
        this.id = id
    }
    get Employeename(){
        return this.name
    }
}
class Admin extends Employee{
    constructor(name,age,id,admin){
        super(name,age,id)
        this.admin = admin
    }
    set setname(naam){
        this.name = naam
        
        console.log(`Employee with id no.${this.id} changed to ${naam}`)
    }
    updateadminname(naam){
        this.admin = naam
        console.log(`Admin name changed to ${naam}`)
    }
}
let test = new Employee("aman","22",123)
test.outout();  
console.log(`Retrieving Employee name by getter function, name = ${test.Employeename}`)
let test2 = new Admin("Sooraj S.","33",1,"Sid")
console.log(` id = ${test2.id} name = ${test2.name} admin name = ${test2.admin}`)
test2.setname = "Suraj Singh"
test2.updateadminname('Sidharth')