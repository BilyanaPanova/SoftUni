function roadRadar(speed,zone) {

    const areas = {"motorway":130,"interstate": 90,"city":50,"residential":20}
    
    if (speed <= areas[zone]) {
        console.log(`Driving ${speed} km/h in a ${areas[zone]} zone`)
    } else {
        const difference = speed - areas[zone]
        let status = null
        if (difference > 40) {
            status = "reckless driving"
        } else if (difference > 20) {
            status = "excessive speeding"
        } else {
            status = "speeding"
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${areas[zone]} - ${status}`)
    }
}
