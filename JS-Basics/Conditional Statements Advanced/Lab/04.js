function solve(age,gender) {
    let result = ""

    if (age >= 16 && gender === "m") {
        result = "Mr."
    }
    else if (age < 16 && gender === "f") {
        result = "Miss"
    }
    else if (age < 16 && gender === "m") {
        result = "Master"
    }
    else    {
        result = "Ms."
    }

    console.log(result)
}
