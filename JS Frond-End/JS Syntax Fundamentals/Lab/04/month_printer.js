function months (number) {
    let months_object = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

    if (months_object[number] !== undefined) {
        console.log(months_object[number]);
    } else {
        console.log("Error!");
    }
}
