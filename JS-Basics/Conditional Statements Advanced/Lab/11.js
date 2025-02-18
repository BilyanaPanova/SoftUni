function calculatePrice(product, day, quantity) {
    const weekdayPrices = {
        banana: 2.50,
        apple: 1.20,
        orange: 0.85,
        grapefruit: 1.45,
        kiwi: 2.70,
        pineapple: 5.50,
        grapes: 3.85
    };

    const weekendPrices = {
        banana: 2.70,
        apple: 1.25,
        orange: 0.90,
        grapefruit: 1.60,
        kiwi: 3.00,
        pineapple: 5.60,
        grapes: 4.20
    };

    const weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    const weekends = ["Saturday", "Sunday"];

    let pricePerUnit;

    if (weekdays.includes(day)) {
        pricePerUnit = weekdayPrices[product];
    } else if (weekends.includes(day)) {
        pricePerUnit = weekendPrices[product];
    } else {
        console.log("error");
        return;
    }

    if (pricePerUnit !== undefined) {
        const totalPrice = (pricePerUnit * quantity).toFixed(2);
        console.log(totalPrice);
    } else {
        console.log("error");
    }
}
