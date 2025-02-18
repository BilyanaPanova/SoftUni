function meeting(arr) {
    let weekdays = {}

    arr.forEach(element => {
        let [day,name] = element.split(" ")
        if (day in weekdays) console.log(`Conflict on ${day}!`);
        else {
            weekdays[day] = name 
            console.log(`Scheduled for ${day}`)
        }
    });

    for (const [key, value] of Object.entries(weekdays)) {
        console.log(`${key} -> ${value}`);
      }
}
