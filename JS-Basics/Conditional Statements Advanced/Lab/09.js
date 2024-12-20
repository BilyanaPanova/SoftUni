function solve(nameOfProduct) {
    const fruits = ["banana", "apple", "kiwi", "cherry", "lemon","grapes"]
    const vegetables = ["tomato", "cucumber", "pepper","carrot"]

    let result = fruits.includes(nameOfProduct) 
    ? "fruit" : vegetables.includes(nameOfProduct) 
    ? "vegetable" : "unknown"

    console.log(result)
}
