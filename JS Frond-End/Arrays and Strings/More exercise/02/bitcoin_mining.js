function mining(days) {
    const gold = 67.51
    const bitcoin = 11949.16

    let amount = 0
    let count = 0
    let day = 0

    for (let i = 1; i <= days.length;i++) {
        if (i % 3 == 0) days[i-1] *=0.7

        amount += days[i-1] * gold

        while (amount - bitcoin >= 0) {
            count += 1
            amount -= bitcoin

            if (day == 0) day = i
        }
    }

    console.log(`Bought bitcoins: ${count}`);
    if (day !== 0) {
        console.log(`Day of the first purchased bitcoin: ${day}`);
    }
    console.log(`Left money: ${amount.toFixed(2)} lv.`);
    

}
