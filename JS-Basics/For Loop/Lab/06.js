function solve(text) {
    const letters = {a:1,e:2,i:3,o:4,u:5}

    let sum = 0

    for (let x of text) {
        if (x in letters) {
            sum += letters[x]
        }
    }
    
    console.log(sum)
}
