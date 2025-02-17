function solve(budget,filmExtras,priceOfClothing) {
    budget *= 0.9
    budget -= filmExtras > 150 ? (filmExtras * priceOfClothing) * 0.9 : filmExtras * priceOfClothing

    let result = budget < 0 
    ? `Not enough money!\nWingard needs ${Math.abs(budget).toFixed(2)} leva more.`
    : `Action!\nWingard starts filming with ${budget.toFixed(2)} leva left.`

    console.log(result)
}
