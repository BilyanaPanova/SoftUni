function calculateOrder(product,count) {
    const productsObject = {
        "coffee":1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }

    let result = productsObject[product] * count
    
    console.log(`${result.toFixed(2)}`)
}
