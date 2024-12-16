function greening(meters) {
    const priceOneMeter = 7.61
    const discount = 0.18

    const total = meters * priceOneMeter
    const totalDiscount = discount * total
    const totalCost = total - totalDiscount

    console.log(`The final price is: ${totalCost} lv.`)
    console.log(`The discount is: ${totalDiscount} lv.`)
}
