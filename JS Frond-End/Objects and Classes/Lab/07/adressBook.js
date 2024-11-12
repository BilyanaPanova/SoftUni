function adressBook(arr) {
    let obj = arr.reduce((acc, entry) => {
        let [name, adress] = entry.split(":");
        acc[name] = adress;
        return acc;
    }, {});

    for (let key of Object.keys(obj).sort()) console.log(`${key} -> ${obj[key]}`)

}
