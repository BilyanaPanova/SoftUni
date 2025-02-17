function cleanCar(commands) {
    let cleanliness = 0;

    const commandMap = {
        'soap': value => value + 10,
        'water': value => value * 1.2,
        'vacuum cleaner': value => value * 1.25,
        'mud': value => value * 0.9
    };

    cleanliness = commands.reduce((acc, command) => commandMap[command](acc), cleanliness);

    console.log(`The car is ${cleanliness.toFixed(2)}% clean.`);
}
