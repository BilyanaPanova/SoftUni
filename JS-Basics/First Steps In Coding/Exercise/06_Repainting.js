function calculateRenovationCost(nylonNeeded,paintNeeded,thinnerNeeded,hours) {    

    let nylonPricePerSqM = 1.50;
    let paintPricePerLiter = 14.50;
    let thinnerPricePerLiter = 5.00;
    let bagPrice = 0.40;

    let totalNylon = (nylonNeeded + 2) * nylonPricePerSqM;       
    let totalPaint = (paintNeeded * 1.1) * paintPricePerLiter;  
    let totalThinner = thinnerNeeded * thinnerPricePerLiter;

    let materialsCost = totalNylon + totalPaint + totalThinner + bagPrice;

    let workersCost = (materialsCost * 0.3) * hours;

    let totalCost = materialsCost + workersCost;

    console.log(totalCost);
}
