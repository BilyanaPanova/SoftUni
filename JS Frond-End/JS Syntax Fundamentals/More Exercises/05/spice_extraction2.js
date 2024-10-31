function calculateSpiceExtraction(startingYield) {
    if (startingYield < 100) {
        console.log(0);
        console.log(0);

    }
    else {
        let days = Math.floor((startingYield - 100) / 10) + 1;
        let totalSpice = (days * (2 * startingYield - (days - 1) * 10) / 2) - days * 26;

        if (totalSpice >= 26) {
            totalSpice -= 26;
        }

        console.log(days);
        console.log(totalSpice);}
}
