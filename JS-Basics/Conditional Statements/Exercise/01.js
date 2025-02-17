function solve(firstTime,secondTime,thurdTime) {
    const totalTime = firstTime + secondTime + thurdTime

    let minutes = Math.floor(totalTime / 60)
    let seconds = totalTime % 60

    let result = `${minutes}:${String(seconds).padStart(2,"0")}`
    console.log(result)
}
