function calculateCommission(city, sales) {
    const commissionRates = {
        Sofia: [
            { min: 0, max: 500, rate: 0.05 },
            { min: 500, max: 1000, rate: 0.07 },
            { min: 1000, max: 10000, rate: 0.08 },
            { min: 10000, max: Infinity, rate: 0.12 }
        ],
        Varna: [
            { min: 0, max: 500, rate: 0.045 },
            { min: 500, max: 1000, rate: 0.075 },
            { min: 1000, max: 10000, rate: 0.1 },
            { min: 10000, max: Infinity, rate: 0.13 }
        ],
        Plovdiv: [
            { min: 0, max: 500, rate: 0.055 },
            { min: 500, max: 1000, rate: 0.08 },
            { min: 1000, max: 10000, rate: 0.12 },
            { min: 10000, max: Infinity, rate: 0.145 }
        ]
    };

    if (!commissionRates[city] || sales < 0) {
        console.log("error");
        return;
    }

    const rates = commissionRates[city];
    let commission = 0;

    for (const rate of rates) {
        if (sales > rate.min && sales <= rate.max) {
            commission = sales * rate.rate;
            break;
        }
    }

    if (commission > 0) {
        console.log(commission.toFixed(2));
    } else {
        console.log("error");
    }
}
