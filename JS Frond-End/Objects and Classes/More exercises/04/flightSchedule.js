function flightInfo(arr) {
    let changed = {}

    let flights = arr[0].reduce((acc,element) => {
        let [key,...value] = element.split(" ")
        acc[key] = value.join(" ")
        return acc 
    },{})
    const act = arr[2][0]

    arr[1].forEach(element => {
        let [key,value] = element.split(" ")
        if (value == "Cancelled" && key in flights){
            let index = Object.keys(flights).indexOf(key)
            changed[index] = flights[key];
            delete flights[key]
        }

        
    });
    
    if (act == "Cancelled") {
        Object.keys(changed).sort().forEach(element => {
            console.log(`{ Destination: '${changed[element]}', Status: 'Cancelled' }`)
        });
    }
    else {
        Object.keys(flights).forEach(element => {
            console.log(`{ Destination: '${flights[element]}', Status: 'Ready to fly' }`)
        });
    }

}

//or 

function manageFlights(arr) {
    let flights = {};

    arr[0].forEach(flight => {
        let [flightNumber, ...destin] = flight.split(" ");
        let destination = destin.join(" ")
        flights[flightNumber] = { destination, status: 'Ready to fly' };
    });

    arr[1].forEach(update => {
        let [flightNumber, newStatus] = update.split(" ");
        if (flights[flightNumber]) {
            flights[flightNumber].status = newStatus;
        }
    });

    let statusToCheck = arr[2][0];

    if (statusToCheck === "Cancelled") {
        Object.keys(flights).forEach(flightNumber => {
            if (flights[flightNumber].status === "Cancelled") {
                console.log(`{ Destination: '${flights[flightNumber].destination}', Status: 'Cancelled' }`);
            }
        });
    } else {
        Object.keys(flights).forEach(flightNumber => {
            if (flights[flightNumber].status === "Ready to fly") {
                console.log(`{ Destination: '${flights[flightNumber].destination}', Status: 'Ready to fly' }`);
                }
            });
        }
}
