function solve(password) {
    const truePassword = "s3cr3t!P@ssw0rd"
    let result = truePassword !== password ? "Wrong password!" : "Welcome"

    console.log(result)
    
}

//or 

function solve(password) {
    const truePassword = "s3cr3t!P@ssw0rd"
    if (truePassword !== password) 
        console.log("Wrong password!")
    else 
        console.log("Welcome")
}
