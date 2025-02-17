function catsSayMeow(arr) {
    let cats = arr.map(entry => {
        let [name, age] = entry.split(" ");
        return { name, age };
    });

    cats.forEach(cat => {
        console.log(`${cat.name}, age ${cat.age} says Meow`);
    });
}
