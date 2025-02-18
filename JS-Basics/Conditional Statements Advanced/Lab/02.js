function checkDay(day) {
    const workingDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    const weekendDays = ["Saturday", "Sunday"];

    if (workingDays.includes(day)) {
        console.log("Working day");
    } else if (weekendDays.includes(day)) {
        console.log("Weekend");
    } else {
        console.log("Error");
    }
}

// or

function checkDay(day) {
    const days = {
        Monday: "Working day",
        Tuesday: "Working day",
        Wednesday: "Working day",
        Thursday: "Working day",
        Friday: "Working day",
        Saturday: "Weekend",
        Sunday: "Weekend"
    };

    console.log(days[day] || "Error");
}
