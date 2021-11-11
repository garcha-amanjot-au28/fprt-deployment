var  atm = (function(){
    withdrwals = 0
    Balance = 100000
    function withdrwal(amt){
        withdrwals += 1
        Balance -= amt
        if (Balance < 0 ) Balance += amt, console.log("ATM does not have enough cash , plz enrter smaller amt")
    }
    function deposit(amt){
        Balance += amt
    }
    return {
        increase : function(amt){
            deposit(amt)
        },
        decrease : function(amt){
            withdrwal (amt)
        },
        value : function(){
            console.log("ATM Balance = " + Balance)
            console.log("Total withdrawals at the ATM = " + withdrwals)
        }

    }
})()
atm.value()
atm.increase(20000)
atm.value()
atm.decrease(20000)
atm.value()
atm.decrease(50000)
atm.value()
atm.decrease(30000)
atm.value()
atm.decrease(20000)
atm.value()
atm.decrease(500)
atm.value()
