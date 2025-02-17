function dictionary(arr) {
    let dict = {};

    arr.forEach(element => {
        let obj = JSON.parse(element);
        Object.assign(dict, obj);
    });

    let sortedKeys = Object.keys(dict).sort((a, b) => a.localeCompare(b));

    sortedKeys.forEach(key => {
        console.log(`Term: ${key} => Definition: ${dict[key]}`);
    });
}
