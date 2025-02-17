function calculatePrice(dayStay, room, rating) {
    let nightStay = dayStay - 1;
    let priceAllNightStay = 0;

    if (room === "room for one person") {
        priceAllNightStay = nightStay * 18.00;
    } else if (room === "apartment") {
        priceAllNightStay = nightStay * 25.00;
        if (dayStay < 10) {
            priceAllNightStay *= 0.70;
        } else if (dayStay >= 10 && dayStay <= 15) {
            priceAllNightStay *= 0.65;
        } else if (dayStay > 15) {
            priceAllNightStay *= 0.50;
        }
    } else if (room === "president apartment") {
        priceAllNightStay = nightStay * 35.00;
        if (dayStay < 10) {
            priceAllNightStay *= 0.90;
        } else if (dayStay >= 10 && dayStay <= 15) {
            priceAllNightStay *= 0.85;
        } else if (dayStay > 15) {
            priceAllNightStay *= 0.80;
        }
    }

    if (rating === "positive") {
        priceAllNightStay *= 1.25;
    } else if (rating === "negative") {
        priceAllNightStay *= 0.90;
    }

    console.log(priceAllNightStay.toFixed(2));
}
