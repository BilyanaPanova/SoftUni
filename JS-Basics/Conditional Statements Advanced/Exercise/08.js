function examArrival(hourExam, minuteExam, hourArrival, minuteArrival) {
    const examTime = new Date(0, 0, 0, hourExam, minuteExam);
    const arrivalTime = new Date(0, 0, 0, hourArrival, minuteArrival);

    const diffMilliseconds = arrivalTime - examTime;
    const diffMinutes = Math.abs(Math.floor(diffMilliseconds / (1000 * 60)));

    if (diffMilliseconds > 0) {
        console.log("Late");
        if (diffMinutes < 60) {
            console.log(`${diffMinutes} minutes after the start`);
        } else {
            const hours = Math.floor(diffMinutes / 60);
            const minutes = diffMinutes % 60;
            console.log(`${hours}:${minutes.toString().padStart(2, '0')} hours after the start`);
        }
    } else if (diffMilliseconds === 0 || diffMinutes <= 30) {
        console.log("On time");
        if (diffMinutes !== 0) {
            console.log(`${diffMinutes} minutes before the start`);
        }
    } else {
        console.log("Early");
        if (diffMinutes >= 60) {
            const hours = Math.floor(diffMinutes / 60);
            const minutes = diffMinutes % 60;
            console.log(`${hours}:${minutes.toString().padStart(2, '0')} hours before the start`);
        } else {
            console.log(`${diffMinutes} minutes before the start`);
        }
    }
}
