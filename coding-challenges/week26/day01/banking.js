class Account{
    constructor(Balance,number){
        this.Balance = Balance
        this.number = number
    }
    deposit(amt){
        this.Balance += amt
    }
    withdraw(amt,account){
        if (account == 'savings' & this.number === 3) console.log('Maximum limit of 3 reached for withdrwals') 
              
        
        else{
            this.Balance -= amt
            this.number += 1
        }
    }

}

class Chequing extends Account{
    checkbal(){
        console.log(this.Balance)
    }

}
class Savings extends Account{
    checkbal(){
        console.log(this.Balance)
    }
}

let test = new Savings(0,0)
test.checkbal()
test.deposit(100000)
test.checkbal()
test.withdraw(3000,'savings')
test.checkbal()
test.withdraw(6000,'savings')
test.checkbal()
test.withdraw(10000,'savings')
test.checkbal()
test.withdraw(2000,'savings')
test.checkbal()