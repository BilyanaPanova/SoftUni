function solve(age,priceWashingMachine,toyPrice) {
    toysCount = 0
    moneyCount = 10
    money = 0


    for (let i = 1; i <= age; i++) {
        if (i % 2 === 0) {
            money += moneyCount - 1
            moneyCount += 10
        }
        else {
            toysCount += 1
        }
    }

    money += toyPrice * toysCount

    if (priceWashingMachine > money) {
        console.log(`No! ${(priceWashingMachine - money).toFixed(2)}`)
    }
    else {
        console.log(`Yes! ${(money - priceWashingMachine).toFixed(2)}`)
    }
}
