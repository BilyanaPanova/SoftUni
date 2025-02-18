function evenAndOddSubtraction (numbers) {
    const evenNumbers = numbers.filter((num) => num % 2 == 0)
    const oddNumbers = numbers.filter((num) => num % 2 != 0)

    let result = evenNumbers.reduce((x,y) => x + y,0) - oddNumbers.reduce((x,y) => x + y,0)

    console.log(result)
}
