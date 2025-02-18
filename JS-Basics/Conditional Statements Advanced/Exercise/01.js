function cinemaIncome(projectionType, rows, columns) {
    const prices = {
        "Premiere": 12.00,
        "Normal": 7.50,
        "Discount": 5.00
    };

    const totalSeats = rows * columns;

    const totalIncome = totalSeats * prices[projectionType];

    console.log(`${totalIncome.toFixed(2)} leva`);

}
