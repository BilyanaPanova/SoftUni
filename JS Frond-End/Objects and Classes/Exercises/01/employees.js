function employeersInformation(arrNames) {
    let objEmployeers = arrNames.reduce((acc, empl) => {
        acc[empl] = empl.length;
        return acc;
    }, {});

    for (let [name,value] of Object.entries(objEmployeers)) {
    console.log(`Name: ${name} -- Personal Number: ${value}`)
    }

}
