function catalogue(arr) {
    let products = {

    }

    arr.forEach(element => {

        let [key,value] = element.split(" : ")
        let firstLetter = key[0]

        if (!(firstLetter in products)) {
            products[firstLetter] = []
        }

        products[firstLetter].push({ [key] : Number(value) })
    });

    Object.keys(products).sort().forEach(firstLetter => {
        console.log(firstLetter);
    
        products[firstLetter]
            .sort((a, b) => Object.keys(a)[0].localeCompare(Object.keys(b)[0]))
            .forEach(item => {
                let key = Object.keys(item)[0];
                let value = item[key];
                console.log(`${key}: ${value}`);
            });
    });
}

