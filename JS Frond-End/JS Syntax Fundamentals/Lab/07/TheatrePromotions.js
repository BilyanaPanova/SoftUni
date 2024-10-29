function ticketPrice (day,age) {
    let price = "Error!"
    if (day == "Weekday") {
        if (age in [...Array(19).keys()]) {
            price = 12
        } else if (age in [...Array(65).keys()]) {
            price = 18
        } else if (age in [...Array(123).keys()]) {
            price = 12
        }

    } else if (day == "Weekend") {
        if (age in [...Array(19).keys()]) {
            price = 15
        } else if (age in [...Array(65).keys()]) {
            price = 20
        } else if (age in [...Array(123).keys()]) {
            price = 15
        }
    } else if (day == "Holiday") {
        if (age in [...Array(19).keys()]) {
            price = 5 
        } else if (age in [...Array(65).keys()]) {
            price = 12
        } else if (age in [...Array(123).keys()]) {
            price = 10
        }
    }
    const output = typeof price === "string" ? `${price}`: `${price}$`
    console.log(`${output}`)
}
