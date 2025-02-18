function isValidDistance(arr) {

    let [x1, y1, x2, y2] = arr
    const distance = (x, y) => Math.sqrt(x * x + y * y);

    const distanceFromOrigin1 = distance(x1, y1);
    const distanceFromOrigin2 = distance(x2, y2);
    const distanceBetweenPoints = distance(x2 - x1, y2 - y1);
    
    const isDistance1Valid = Number.isInteger(distanceFromOrigin1);
    const isDistance2Valid = Number.isInteger(distanceFromOrigin2);
    const isDistance3Valid = Number.isInteger(distanceBetweenPoints);

    if (isDistance1Valid) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`);
    }
    
    if (isDistance2Valid) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`);
    } else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`);
    }


    if (isDistance3Valid) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}poin
