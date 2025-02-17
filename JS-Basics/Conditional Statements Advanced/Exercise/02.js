function summerOutfit(degrees, timeOfDay) {
    let outfit = "";
    let shoes = "";

    if (degrees >= 10 && degrees <= 18) {
        if (timeOfDay === "Morning") {
            outfit = "Sweatshirt";
            shoes = "Sneakers";
        } else {
            outfit = "Shirt";
            shoes = "Moccasins";
        }
    } else if (degrees > 18 && degrees <= 24) {
        if (timeOfDay === "Morning") {
            outfit = "Shirt";
            shoes = "Moccasins";
        } else if (timeOfDay === "Afternoon") {
            outfit = "T-Shirt";
            shoes = "Sandals";
        } else {
            outfit = "Shirt";
            shoes = "Moccasins";
        }
    } else if (degrees >= 25) {
        if (timeOfDay === "Morning") {
            outfit = "T-Shirt";
            shoes = "Sandals";
        } else if (timeOfDay === "Afternoon") {
            outfit = "Swim Suit";
            shoes = "Barefoot";
        } else {
            outfit = "Shirt";
            shoes = "Moccasins";
        }
    }

    console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`);
}
