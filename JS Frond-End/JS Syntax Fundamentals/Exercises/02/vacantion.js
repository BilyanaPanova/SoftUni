function calculatePrice(group,type,day) {

    let total = null

    switch (type) {
        case "Students": 

            switch (day) {
                case "Friday":
                    total = 8.45
                    break;
                case "Saturday":
                    total = 9.80
                    break
                case "Sunday":
                    total = 10.46
                    break
            }

            total *= group

            if (group >= 30) total *= 0.85
            break

        case "Business": 

            if (group >= 100) group -= 10

            switch (day) {
                case "Friday":
                    total = 10.90
                    break;
                case "Saturday":
                    total = 15.60
                    break
                case "Sunday":
                    total = 16
                    break
            }

            total *= group
            break
        case "Regular": 

            switch (day) {
                case "Friday":
                    total = 15
                    break;
                case "Saturday":
                    total = 20
                    break
                case "Sunday":
                    total = 22.50
                    break
                }

            total *= group

            if (group >= 10 && group <= 20) total *= 0.95
            break
    }

    console.log(`Total price: ${total.toFixed(2)}`)

}
