function calculate(num1, operator, num2) {
    const operations = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => b !== 0 ? a / b : 'Cannot divide by zero',
        '%': (a, b) => b !== 0 ? a % b : 'Cannot divide by zero',
        '**': (a, b) => a ** b
    };

    const result = (operations[operator](num1, num2)).toFixed(2);
    console.log(result);
}
