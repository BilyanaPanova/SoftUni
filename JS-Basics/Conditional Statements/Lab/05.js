function solve(number) {
    let result = number < 100 ? "Less than 100" : number > 200 ? "Greater than 200" : "Between 100 and 200"
    console.log(result)
}

function solve(number) {
    if (number < 100) 
        console.log("Less than 100")
    else if (number > 200)
        console.log("Greater than 200")
    else
        console.log("Between 100 and 200")
}
