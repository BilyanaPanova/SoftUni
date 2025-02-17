function matrix(count) {
    let result = ((count + " ").repeat(count).trim() + "\n").repeat(count);
    console.log(result)
}

//or

function matrix(count) {
    let row = (count + " ").repeat(count).trim();
    for (let i = 0; i < count; i++) {
        console.log(row);
    }
}

