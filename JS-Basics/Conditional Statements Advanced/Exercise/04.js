function fishingTrip(budget, season, countFishman) {
    let priceShip = 0;
    let discount = 0;

    if (season === "Spring") {
        priceShip = 3000;
    } else if (season === "Summer" || season === "Autumn") {
        priceShip = 4200;
    } else if (season === "Winter") {
        priceShip = 2600;
    }

    if (countFishman <= 6) {
        discount += 0.1;
    } else if (countFishman >= 7 && countFishman <= 11) {
        discount += 0.15;
    } else if (countFishman >= 12) {
        discount += 0.25;
    }

    let total = priceShip - (priceShip * discount);

    if (season !== "Autumn" && countFishman % 2 === 0) {
        total *= 0.95;
    }

    let leftMoney = Math.abs(budget - total).toFixed(2);


    if (budget >= total) {
        console.log(`Yes! You have ${leftMoney} leva left.`);
    } else {
        console.log(`Not enough money! You need ${leftMoney} leva.`);
    }
}
