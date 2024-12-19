function solve(excursionPrice,...toys) {

    const allPrices = {
        puzzelPrice:2.60,
        dollPrice:3, 
        teddybearPrice: 4.10,
        minionPrice: 8.20,
        truckPrice :2}

    let totalCost = 0
    let totalToys = 0

    toys.forEach((toy,index) => {
        totalToys += toy
        totalCost += toy * Object.values(allPrices)[index]
    });

    if (totalToys >= 50) {
        totalCost *= 0.75
    }

    totalCost *= 0.9

    let result = totalCost >= excursionPrice ? 
    `Yes! ${(totalCost-excursionPrice).toFixed(2)} lv left.` : `Not enough money! ${(excursionPrice - totalCost).toFixed(2)} lv needed.`

    console.log(result)
}

//or 

function toyShop(...input) {

    let tripPrice = parseFloat(input[0]);
    let puzzles = parseInt(input[1]);
    let dolls = parseInt(input[2]);
    let bears = parseInt(input[3]);
    let minions = parseInt(input[4]);
    let trucks = parseInt(input[5]);

    const puzzlePrice = 2.60;
    const dollPrice = 3.00;
    const bearPrice = 4.10;
    const minionPrice = 8.20;
    const truckPrice = 2.00;

    let totalToys = puzzles + dolls + bears + minions + trucks;
    let totalPrice = 
        puzzles * puzzlePrice + 
        dolls * dollPrice + 
        bears * bearPrice + 
        minions * minionPrice + 
        trucks * truckPrice;

    if (totalToys >= 50) {
        totalPrice *= 0.75; 
    }

    totalPrice *= 0.90; 

    let difference = totalPrice - tripPrice;

    if (difference >= 0) {
        console.log(`Yes! ${difference.toFixed(2)} lv left.`);
    } else {
        console.log(`Not enough money! ${Math.abs(difference).toFixed(2)} lv needed.`);
    }
}
