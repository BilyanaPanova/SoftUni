function calculateHistogram(input) {
    const n = input[0]; 
    const numbers = input.slice(1); 

    const p1 = (numbers.filter(num => num < 200).length / n * 100).toFixed(2);
    const p2 = (numbers.filter(num => num >= 200 && num < 400).length / n * 100).toFixed(2);
    const p3 = (numbers.filter(num => num >= 400 && num < 600).length / n * 100).toFixed(2);
    const p4 = (numbers.filter(num => num >= 600 && num < 800).length / n * 100).toFixed(2);
    const p5 = (numbers.filter(num => num >= 800).length / n * 100).toFixed(2);

    console.log(`${p1}%`);
    console.log(`${p2}%`);
    console.log(`${p3}%`);
    console.log(`${p4}%`);
    console.log(`${p5}%`);
}
