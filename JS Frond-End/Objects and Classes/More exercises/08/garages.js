function storeCarsInGarages(arr) {
    let garages = {};

    arr.forEach(entry => {
        let [garageNumber, carInfo] = entry.split(" - ");
        garageNumber = Number(garageNumber); 

        let carDetails = {};
        carInfo.split(", ").forEach(detail => {
            let [key, value] = detail.split(": ");
            carDetails[key] = value;
        });

        if (!garages[garageNumber]) {
            garages[garageNumber] = [];
        }

        garages[garageNumber].push(carDetails);
    });

    Object.keys(garages).sort((a, b) => a - b).forEach(garageNumber => {
        console.log(`Garage № ${garageNumber}`);
        garages[garageNumber].forEach(car => {
            let carInfoStr = Object.entries(car)
                .map(([key, value]) => `${key} - ${value}`)
                .join(", ");
            console.log(`--- ${carInfoStr}`);
        });
    });
}
