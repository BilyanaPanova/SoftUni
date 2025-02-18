function carRegister(arr) {
    let parking = []

    arr.forEach(element => { 
        let [act,carNumber] = element.split(", ")
        if (act === "IN" && !parking.includes(carNumber)) {
            parking.push(carNumber)
        }
        else if (act === "OUT") {
            parking = parking.filter((number) => number !== carNumber)
        }
        
    })

    if (parking.length > 0) {
        parking.sort().forEach(carNumber => {
            console.log(carNumber);
        });
    } else {
        console.log("Parking Lot is Empty");
    }
}

//or 

function parkingLotManagement(input) {
    let parking = new Set();

    input.forEach(entry => {
        let [direction, carNumber] = entry.split(", ");
        if (direction === "IN") {
            parking.add(carNumber);
        } else if (direction === "OUT") {
            parking.delete(carNumber);
        }
    });

    if (parking.size > 0) {
        [...parking]
            .sort()
            .forEach(carNumber => console.log(carNumber));
    } else {
        console.log("Parking Lot is Empty");
    }
}
