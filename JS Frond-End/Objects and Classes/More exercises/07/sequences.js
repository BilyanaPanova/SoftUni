function sortedSequences(arr) {

    let result = []

    arr.forEach(element => {
        let arrElement = JSON.stringify(JSON.parse(element).sort((a,b)=>b-a))
        if (!result.includes(arrElement)) {
            result.push(arrElement)
        }

        
    });

    result.sort((a, b) => JSON.parse(a).length - JSON.parse(b).length).forEach(element => {
        let output = `[${JSON.parse(element).join(", ")}]`
        console.log(output)
    })
    
    
}
