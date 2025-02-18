function calculate(num1, num2, operator) {
    const operations = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '*': (a, b) => a * b,
        '/': (a, b) => b !== 0 ? a / b : 'Cannot divide by zero',
        '%': (a, b) => b !== 0 ? a % b : 'Cannot divide by zero',
        '**': (a, b) => a ** b
    };

    const result = operations[operator] ? operations[operator](num1, num2) : 'Invalid operator';
    console.log(result);
}
