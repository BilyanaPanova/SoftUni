function  cooking () {
    let number = Number(arguments[0])

    for (let i = 1 ; i < arguments.length; i++) {
        switch (arguments[i]) {
            case "chop" :
                number /= 2
                break
            case "dice" :
                number = Math.sqrt(number)
                break
            case "spice" :
                number++
                break
            case "bake" :
                number *= 3
                break
            case "fillet" :
                number =  (number * 0.8).toFixed(1)
                break
        }
        console.log(number)
    }

    
}
