function isOfficeOpen(hour, day) {
    const workingDays = {
        Monday: true,
        Tuesday: true,
        Wednesday: true,
        Thursday: true,
        Friday: true,
        Saturday: true,
        Sunday: false
    };

    if (hour >= 10 && hour <= 18 && workingDays[day]) {
        console.log("open");
    } else {
        console.log("closed");
    }
}
