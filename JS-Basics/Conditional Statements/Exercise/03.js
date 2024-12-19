function add15MinutesToGivenTime(hours, minutes) {
    
    let date = new Date();
    date.setHours(hours);
    date.setMinutes(minutes);

    date.setMinutes(date.getMinutes() + 15);

    let updatedHours = date.getHours();
    let updatedMinutes = date.getMinutes();

    let formattedMinutes = updatedMinutes.toString().padStart(2, '0');

    console.log(`${updatedHours}:${formattedMinutes}`);
}

//or 

function add15Minutes(hours, minutes) {
    minutes += 15;

    if (minutes >= 60) {
        minutes -= 60;
        hours += 1;
    }

    if (hours >= 24) {
        hours -= 24;
    }

    let formattedMinutes = minutes.toString().padStart(2, '0');

    console.log(`${hours}:${formattedMinutes}`);
}
