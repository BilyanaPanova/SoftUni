function divideFactorials(num1, num2) {
    let result = 1;

    for (let i = 2; i <= num1; i++) {
        result *= i;
    }

    let factorial1 = result;
    result = 1; 

    for (let i = 2; i <= num2; i++) {
        result *= i;
    }

    let factorial2 = result;

    let divisionResult = (factorial1 / factorial2).toFixed(2);
    console.log(divisionResult);
}
