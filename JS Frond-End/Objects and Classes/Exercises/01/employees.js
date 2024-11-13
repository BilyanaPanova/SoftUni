function employeesInformation(arrNames) {
    let objEmployees = arrNames.reduce((acc, empl) => {
        acc[empl] = empl.length;
        return acc;
    }, {});

    for (let [name,value] of Object.entries(objEmployees)) {
    console.log(`Name: ${name} -- Personal Number: ${value}`)
    }

}
