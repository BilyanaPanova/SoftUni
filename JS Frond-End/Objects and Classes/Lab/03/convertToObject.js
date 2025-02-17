function convertToObject(jsonString) {

    const obj = JSON.parse(jsonString);

    for (let key in obj) {
        console.log(`${key}: ${obj[key]}`);
    }
}
