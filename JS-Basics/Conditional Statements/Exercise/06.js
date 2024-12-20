function solve(record,distance,timeToSwimsOneMeter) {
    let totalTime = distance * timeToSwimsOneMeter
    let delay = Math.floor(distance / 15) * 12.5
    totalTime += delay
  

    let result = record <= totalTime 
    ? `No, he failed! He was ${(totalTime-record).toFixed(2)} seconds slower.` 
    : `Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`
    
    console.log(result)

}
