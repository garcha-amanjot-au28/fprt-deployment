
let today =  new Date ();
let atm = (() => {
    let Balance = 100000
    let withdrwals = 0
    function withdraw (amt){
        Balance -= amt
        withdrwals +=1 
        
        let date = today.getFullYear()+"-"+(today.getMonth()+1)+'-'+today.getDate();
        let time = today.getHours()+":"+today.getMinutes()+":"+today.getSeconds();
        let datetime = date+' '+time
        // let timestamp = `${amt} withdrawn at ${datetime} ATM Balance : ${Balance}`
        // console.log(timestamp)
        // console.log(`Total withdrwals = ${withdrwals}`)
        return [datetime,withdrwals,amt,Balance]

    }
    return {
        decrease : amt => withdraw(amt),
        value : () => console.log(Balance)
    }
})()

let [dt,w,a,b] = atm.decrease(10000)
console.log(`${a} was withdrawn at ${dt} remaining Balance is ${b}`)
console.log(`Total withdrawals = ${w}`)
let [d,wi,aa,bb] =atm.decrease(20000)
console.log(`${aa} was withdrawn at ${d} remaining Balance is ${bb}`)
console.log(`Total withdrawals = ${wi}`)
let [dd,wit,aaa,bbb] =atm.decrease(20000)
console.log(`${aaa} was withdrawn at ${dd} remaining Balance is ${bbb}`)
console.log(`Total withdrawals = ${wit}`)
