function aquarium(length,width,height,percent) {
    let volume = length * width * height;
    let volumeLiters = volume / 1000;
    let occupiedSpace = percent / 100;
    let waterNeeded = volumeLiters * (1 - occupiedSpace);

    console.log(waterNeeded);
}
