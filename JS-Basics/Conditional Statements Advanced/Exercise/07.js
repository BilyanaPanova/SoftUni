function calculateStayCost(month, countNights) {
    let priceStudio = 0;
    let priceApartment = 0;
    let priceOfEntireStayInStudio = 0;
    let priceOfEntireStayInApartment = 0;

    if (month === "May" || month === "October") {
        priceStudio = 50;
        priceApartment = 65;
        if (countNights > 7 && countNights < 14) {
            priceStudio *= 0.95;
        } else if (countNights > 14) {
            priceStudio *= 0.70;
            priceApartment *= 0.9;
        }
    } else if (month === "June" || month === "September") {
        priceStudio = 75.2;
        priceApartment = 68.7;
        if (countNights > 14) {
            priceStudio *= 0.80;
            priceApartment *= 0.9;
        }
    } else if (month === "July" || month === "August") {
        priceStudio = 76;
        priceApartment = 77;
        if (countNights > 14) {
            priceApartment *= 0.9;
        }
    }

    priceOfEntireStayInStudio = countNights * priceStudio;
    priceOfEntireStayInApartment = countNights * priceApartment;

    console.log(`Apartment: ${priceOfEntireStayInApartment.toFixed(2)} lv.`);
    console.log(`Studio: ${priceOfEntireStayInStudio.toFixed(2)} lv.`);
}
