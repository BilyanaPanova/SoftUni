function solve(budget, videoCards, processors, ramSticks) {
    const videoCardPrice = 250;
    const videoCardsCost = videoCards * videoCardPrice;

    const processorPrice = videoCardsCost * 0.35;
    const processorsCost = processors * processorPrice;
    
    const ramPrice = videoCardsCost * 0.10;
    const ramCost = ramSticks * ramPrice;

    let totalCost = videoCardsCost + processorsCost + ramCost;

    if (videoCards > processors) {
        totalCost *= 0.85;
    }

    const difference = budget - totalCost;
    const result = difference >= 0
        ? `You have ${difference.toFixed(2)} leva left!`
        : `Not enough money! You need ${Math.abs(difference).toFixed(2)} leva more!`;

    console.log(result);
}
