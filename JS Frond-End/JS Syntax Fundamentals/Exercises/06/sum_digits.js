function sumDigits(digits) {
    let strDigits = String(digits)
    let sum = 0
    for (let char of strDigits) {
        sum += Number(char)
    }
    console.log(sum)
}
