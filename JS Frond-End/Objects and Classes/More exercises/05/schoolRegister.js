function register(arr) {
    let info = {}

    arr.forEach(element => {
        let name = element.split(", ")[0].split(": ")[1]
        let grade = Number(element.split(", ")[1].split(": ")[1]) + 1
        let average = Number(element.split(", ")[2].split(": ")[1])

        if (average >= 3) {
            if (!(grade in info)) {
                info[grade] = {"Names":[],"Average":[]}

            }
            info[grade]["Names"].push(name)
            info[grade]["Average"].push(average)

        }
    });
    
    Object.keys(info).sort((a, b) => Number(a) - Number(b)).forEach(element => {
        console.log(`${element} Grade`)
        console.log(`List of students: ${info[element]["Names"].join(", ")}`)
        let averageNumber = info[element]["Average"].reduce((accumulator, currentValue) => {
            return accumulator + currentValue;
        }, 0) / info[element]["Average"].length;
        console.log(`Average annual score from last year: ${averageNumber.toFixed(2)}`)
        console.log()
    });

    
}
