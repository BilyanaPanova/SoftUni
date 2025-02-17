function findSmallestNumber() {
    let result = Array.from(arguments).sort((a,b) => a-b)
    console.log(result[0])
}
