function divisibleByNine(start, end) {
    const numbers = Array.from({ length: end - start + 1 }, (_, i) => start + i);

    const divisible = numbers.filter(num => num % 9 === 0);

    const sum = divisible.reduce((acc, num) => acc + num, 0);

    console.log(`The sum: ${sum}`);
    divisible.forEach(num => console.log(num));
}
