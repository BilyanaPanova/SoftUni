function flowerShop(flowerType, flowerCount, budget) {
    let pricePerFlower = 0;

    switch (flowerType) {
        case "Roses":
            pricePerFlower = 5;
            break;
        case "Dahlias":
            pricePerFlower = 3.80;
            break;
        case "Tulips":
            pricePerFlower = 2.80;
            break;
        case "Narcissus":
            pricePerFlower = 3;
            break;
        case "Gladiolus":
            pricePerFlower = 2.50;
            break;
    }

    let totalPrice = pricePerFlower * flowerCount;

    if (flowerType === "Roses" && flowerCount > 80) {
        totalPrice *= 0.90;
    } else if (flowerType === "Dahlias" && flowerCount > 90) {
        totalPrice *= 0.85;
    } else if (flowerType === "Tulips" && flowerCount > 80) {
        totalPrice *= 0.85;
    } else if (flowerType === "Narcissus" && flowerCount < 120) {
        totalPrice *= 1.15;
    } else if (flowerType === "Gladiolus" && flowerCount < 80) {
        totalPrice *= 1.20;
    }

    if (budget >= totalPrice) {
        let moneyLeft = (budget - totalPrice).toFixed(2);
        console.log(`Hey, you have a great garden with ${flowerCount} ${flowerType} and ${moneyLeft} leva left.`);
    } else {
        let moneyNeeded = (totalPrice - budget).toFixed(2);
        console.log(`Not enough money, you need ${moneyNeeded} leva more.`);
    }
}
