function gladiatorExpenses () {
    const priceEquipment = {"helmet":arguments[1],"sword":arguments[2],"shield":arguments[3],"armor":arguments[4]}
    let total = null

    for (let i = 1 ; i <= arguments[0]; i++) {
        if (i % 12 == 0) total += priceEquipment["armor"]
        if (i % 6 == 0) total += priceEquipment["shield"]
        if (i % 3 == 0) total += priceEquipment["sword"]
        if (i % 2 == 0) total += priceEquipment["helmet"]
    }

    console.log(`Gladiator expenses: ${total.toFixed(2)} aureus`)
}
