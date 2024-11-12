function createCats(catsArray) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    catsArray.forEach(catString => {
        const [name, age] = catString.split(" ");
        const cat = new Cat(name, parseInt(age));
        cat.meow();
    });
}
