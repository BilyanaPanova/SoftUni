function calculateTennisStats(input) {
    const tournamentCount = parseInt(input[0]); 
    const startingPoints = parseInt(input[1]);
    const results = input.slice(2); 

    let totalPoints = startingPoints; 
    let pointsEarned = 0;
    let wins = 0; 

    for (const result of results) {
        if (result === "W") {
            pointsEarned += 2000;
            wins++;
        } else if (result === "F") {
            pointsEarned += 1200;
        } else if (result === "SF") {
            pointsEarned += 720;
        }
    }

    totalPoints += pointsEarned; 
    const averagePoints = Math.floor(pointsEarned / tournamentCount);
    const winPercentage = (wins / tournamentCount * 100).toFixed(2); 

    console.log(`Final points: ${totalPoints}`);
    console.log(`Average points: ${averagePoints}`);
    console.log(`${winPercentage}%`);
}
