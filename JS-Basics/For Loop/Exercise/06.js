function calculateActorPoints(input) {
    const actorName = input[0]; 
    let points = parseFloat(input[1]); 
    const numJudges = parseInt(input[2]); 
    const judgesData = input.slice(3); 

    for (let i = 0; i < numJudges; i++) {
        const judgeName = judgesData[i * 2]; 
        const judgePoints = parseFloat(judgesData[i * 2 + 1]); 

        points += (judgeName.length * judgePoints) / 2;

        if (points > 1250.5) {
            console.log(`Congratulations, ${actorName} got a nominee for leading role with ${points.toFixed(1)}!`);
            return;
        }
    }

    const neededPoints = (1250.5 - points).toFixed(1);
    console.log(`Sorry, ${actorName} you need ${neededPoints} more!`);
}
