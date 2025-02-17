function solve(text) {
    let sum = 0

    for (let x of text) {
        sum += Number(x)
    }

    console.log(`The sum of the digits is:${sum}`)
}
