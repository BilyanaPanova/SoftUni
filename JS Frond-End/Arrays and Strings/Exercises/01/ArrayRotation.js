function solve(arr,number) {

    let result = [...arr.slice(number % arr.length), ...arr.slice(0, number % arr.length)].join(" ");

    console.log(result)
    
}
