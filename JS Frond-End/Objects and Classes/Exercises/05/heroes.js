function registerHeroes(input) {
    let heroes = [];

    input.forEach(line => {
        let [name, level, items] = line.split(" / ");
        level = Number(level);
        heroes.push({ name, level, items });
    });

    heroes.sort((a, b) => a.level - b.level);

    heroes.forEach(hero => {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items}`);
    });
}

//or 

function heroesRegister(arr) {
    let heroesBook = []
    
    arr.forEach(element => { 
        let [name,level,items] = element.split(" / ")
        heroesBook.push({"Name":name,"Level":+level,"Items":items})
    });
    let hero = Object.groupBy(heroesBook,(hero) => hero.Level)
    Object.keys(heroesBook).reverse().forEach(element => { 
        let hero = heroesBook[element]["Name"]
        let level = heroesBook[element]["Level"]
        let items = heroesBook[element]["Items"]
        console.log(`Hero: ${hero}\nlevel => ${level}\nItems => ${items}`)
    });
}
