function solve(seriesName, episodeDuration, breakDuration) {
    const lunchTime = breakDuration / 8;
    const relaxTime = breakDuration / 4;

    const timeForWatching = breakDuration - lunchTime - relaxTime;

    if (timeForWatching >= episodeDuration) {
        const freeTime = Math.ceil(timeForWatching - episodeDuration);
        console.log(`You have enough time to watch ${seriesName} and left with ${freeTime} minutes free time.`);
    } else {
        const neededTime = Math.ceil(episodeDuration - timeForWatching);
        console.log(`You don't have enough time to watch ${seriesName}, you need ${neededTime} more minutes.`);
    }
}
