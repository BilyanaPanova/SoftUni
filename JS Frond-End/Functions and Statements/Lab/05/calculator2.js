const calculate = (num1, num2, operator) => {
    const operations = new Map([
        ['add', (a, b) => a + b],
        ['subtract', (a, b) => a - b],
        ['multiply', (a, b) => a * b],
        ['divide', (a, b) => a / b]
    ]);
    
    console.log(operations.get(operator)(num1, num2))
}
