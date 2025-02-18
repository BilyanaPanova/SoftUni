
function sorting(arr) {
    arr.sort((a,b) => a-b)
    let result = [];

    while (arr.length > 0) {
        result.push(arr.shift(),arr.pop())
    }

    return result
}

