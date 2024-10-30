function calculation (start,end ) {
    let sum = 0
    for (let i = start; i <= end ; i++) {
        sum += i
        process.stdout.write(String(i) + " ")
    }
    console.log(`\nSum: ${sum}`)
}
