
class Person{
    constructor(name,age,city){
        this.name = name
        this.age = age
        this.city = city
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
        let now = new Date()
        console.log(`Admin name changed to ${naam} at ${now} `)
    }
}
let test = new Employee("aman","22",123)
test.outout();  
console.log(`Retrieving Employee name by getter function, name = ${test.Employeename}`)
let test2 = new Admin("Sooraj S.","33",1,"Sid")
console.log(` id = ${test2.id} name = ${test2.name} admin name = ${test2.admin}`)
test2.setname = "Suraj Singh"
setTimeout(function() {test2.updateadminname("Johal")}, 4000);
test2.updateadminname('Sidharth')
setTimeout(function()  {test2.updateadminname("hari")}, 2000);
setTimeout(function(){test2.updateadminname("jasi")},6000)
setTimeout(function(){test2.updateadminname("Danny")},8000)
