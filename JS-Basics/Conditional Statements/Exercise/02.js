function solve(startNumber) {
    let bonusPoints = 0

    if (startNumber <= 100) {
        bonusPoints += 5
    }
    else if (startNumber > 1000) {
        bonusPoints += startNumber * 0.10
    }
    else {
        bonusPoints += startNumber * 0.20
    }
 
    if (startNumber % 2 === 0) 
        bonusPoints += 1

    if (String(startNumber).slice(-1) == "5")
        bonusPoints += 2

    console.log(bonusPoints)
    console.log(bonusPoints + startNumber)
}
