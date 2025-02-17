function solve(numberOfPens,numberOfMarkers,liquid,discount) {
    const priceOnePen =  5.80
    const priceOneMarker =  7.20
    const priceOneLitterLiquid =  1.20

    const totalCost = ((numberOfPens * priceOnePen) + (numberOfMarkers * priceOneMarker) + (liquid * priceOneLitterLiquid)) * (1 - (discount/ 100))
    console.log(totalCost)
}
