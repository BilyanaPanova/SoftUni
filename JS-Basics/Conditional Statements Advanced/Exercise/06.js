function calculate(number1, number2, operator) {
    let result = 0;
    let evenOrOdd = '';

    if (operator === "+") {
        result = number1 + number2;
        evenOrOdd = result % 2 === 0 ? "even" : "odd";
        console.log(`${number1} ${operator} ${number2} = ${result} - ${evenOrOdd}`);
      
    } else if (operator === "-") {
        result = number1 - number2;
        evenOrOdd = result % 2 === 0 ? "even" : "odd";
        console.log(`${number1} ${operator} ${number2} = ${result} - ${evenOrOdd}`);
      
    } else if (operator === "*") {
        result = number1 * number2;
        evenOrOdd = result % 2 === 0 ? "even" : "odd";
        console.log(`${number1} ${operator} ${number2} = ${result} - ${evenOrOdd}`);
      
    } else if (operator === "/") {
        if (number2 === 0) {
            console.log(`Cannot divide ${number1} by zero`);
        } else {
            result = number1 / number2;
            console.log(`${number1} / ${number2} = ${result.toFixed(2)}`);
        }
      
    } else if (operator === "%") {
        if (number2 === 0) {
            console.log(`Cannot divide ${number1} by zero`);
        } else {
            result = number1 % number2;
            console.log(`${number1} % ${number2} = ${result}`);
        }
    }
}
