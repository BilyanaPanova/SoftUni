function calculateArea(shape,...numbers) {
    if (shape === "square") {
        let side = numbers[0]
        console.log((side * side).toFixed(3));
    } 
    else if (shape === "rectangle") {
        let length =numbers[0]
        let width = numbers[1]
        console.log((length * width).toFixed(3));
    } 
    else if (shape === "circle") {
        let radius = numbers[0]
        console.log((Math.PI * radius * radius).toFixed(3));
    } 
    else if (shape === "triangle") {
        let base = numbers[0]
        let height = numbers[1]
        console.log(((base * height) / 2).toFixed(3));
    } 
    
}
