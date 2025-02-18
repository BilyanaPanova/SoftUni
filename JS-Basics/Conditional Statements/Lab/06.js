function checkSpeed(speed) {
    if (speed <= 10) {
        console.log("slow");
    } else if (speed <= 50) {
        console.log("average");
    } else if (speed <= 150) {
        console.log("fast");
    } else if (speed <= 1000) {
        console.log("ultra fast");
    } else {
        console.log("extremely fast");
    }
}

// or

function checkSpeed(speed) {
    console.log(
        speed <= 10 ? "slow" :
        speed <= 50 ? "average" :
        speed <= 150 ? "fast" :
        speed <= 1000 ? "ultra fast" :
        "extremely fast"
    );
}
