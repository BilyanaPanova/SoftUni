function calculate(num1, num2, operator) {
    const operations = {
        'add': (a, b) => a + b,
        'subtract': (a, b) => a - b,
        'multiply': (a, b) => a * b,
        'divide': (a, b) => b !== 0 ? a / b : 'Cannot divide by zero'
    };

    const result = (operations[operator](num1, num2));

    console.log(result);
}
