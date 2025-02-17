function sorting(arr) {

    const smallToBig = arr.sort((a, b) => a - b).slice();
    const bigToSmall = arr.sort((a, b) => b - a).slice();

    let result = [];

    for (let i = 0; i < smallToBig.length / 2; i++) {

        result.push(smallToBig[i]);
        if (result.length == arr.length) return result 
        result.push(bigToSmall[i]);
    }

    return result
}
