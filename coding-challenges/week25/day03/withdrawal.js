let  atm = (function(){
    let withdrawals= 0
    let Balance = 100000
    function withdrawal(amt){
        withdrawals += 1
        Balance -= amt
        let now = new Date()
        console.log("Withdrawal at "+now+ " of Rs."+amt)
        let count = `total withdrawals = ${withdrawals}`
        console.log(count)
    
    }
    return {
        decrease : function(amt){
            withdrawal(amt)
            
        },
        value : function(){
            console.log(Balance)

            
                
        }
    }
})()
atm.value()
atm.decrease(20000)
atm.value()
atm.decrease(40000)
atm.value()
atm.decrease(20000)