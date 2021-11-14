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
class Admin extends Employee{
    constructor(name,age,id,admin){
        super(name,age,id)
        this.admin = admin
    }
    updateemployeename(naam){
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
let test2 = new Admin("Sooraj S.","33",1,"Sid")
console.log(` id = ${test2.id} name = ${test2.name} admin name = ${test2.admin}`)
test2.updateemployeename("Suraj Singh")
test2.updateadminname('Sidharth')