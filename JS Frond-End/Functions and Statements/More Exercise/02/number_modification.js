function modification(number) {
    let arrNumbers = String(number).split("").map(Number)

    while ((arrNumbers.reduce((acc,x) => acc + x,0) / arrNumbers.length) <= 5 ) {
        arrNumbers.push(9)
    }

    console.log(arrNumbers.join(""))
}
