function solve(num1,num2) {
    const biggest = Math.max(num1,num2)

    console.log(biggest)
}

//or 

function solve(num1,num2) {

    let result = num1 > num2 ? num1 : num2

    console.log(result)
    
}

//or

function solve(num1,num2) {
    if (num1 > num2) 
        console.log(num1)
    else 
        console.log(num2)
}
