function login(arr) {
    
    let username = arr[0]

    for (let i = 1;i < arr.length; i++) {
        let currPassword = arr[i].split("").reverse().join("")

        if (currPassword == username) {
            console.log(`User ${username} logged in.`)
            return
        }
        else if (i < 4){
            console.log(`Incorrect password. Try again.`)
        }

        else  console.log(`User ${username} blocked!`)

    }
}
