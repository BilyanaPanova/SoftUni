function phoneBook(arr) {
    let obj = arr.reduce((acc, entry) => {
        let [name, phonenumber] = entry.split(" ");
        acc[name] = phonenumber;
        return acc;
    }, {});

    Object.entries(obj).forEach(([name, phonenumber]) => 
        console.log(`${name} -> ${phonenumber}`)
    );
}


//or

function phoneBook(arr) {
    let obj = {}

    arr.forEach(element => {
        let [name,phonenumber] = element.split(" ")
        obj[name] = phonenumber
    });

    for (const [key, value] of Object.entries(obj)) {
        console.log(`${key} -> ${value}`);
      }
}
