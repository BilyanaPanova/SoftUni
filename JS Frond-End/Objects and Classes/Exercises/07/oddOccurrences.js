function extraxtElements(string) {
    let allElements = string.split(" ").map(element => element.toLowerCase());

    while (allElements.length != 0) {
        let i = 0
        let currEl = allElements[i]
        let countEl = allElements.filter((word) => word == currEl)
        if (countEl.length % 2 != 0 ) {
            process.stdout.write(currEl + " ")
        }
        allElements = allElements.filter((word) => word != currEl)
    }

}

//or

function extractElements(string) {
    let allElements = string.split(" ").map(element => element.toLowerCase());

    let frequencies = {};
    allElements.forEach(word => {
        frequencies[word] = (frequencies[word] || 0) + 1;
    });
    Object.keys(frequencies).forEach(word => {
        if (frequencies[word] % 2 !== 0) {
            process.stdout.write(word + " ");
        }
    });
}
