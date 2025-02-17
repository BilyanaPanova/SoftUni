function sumAddAndOdd(number) {
    
    let arrNumbers = String(number).split("")

    let oddNumber = arrNumbers.map(Number)
    .filter(x => x % 2 != 0)
    .reduce((acc, x) => acc + x, 0); 

    let evenNumber = arrNumbers.map(Number)
    .filter(x => x % 2 == 0)
    .reduce((acc, x) => acc + x, 0); 

    console.log(`Odd sum = ${oddNumber}, Even sum = ${evenNumber}`)
}
