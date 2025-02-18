function addressBook(arr) {
    let obj = arr.reduce((acc, entry) => {
        let [name, address] = entry.split(":");
        acc[name] = address;
        return acc;
    }, {});

    for (let key of Object.keys(obj).sort()) console.log(`${key} -> ${obj[key]}`)

}
