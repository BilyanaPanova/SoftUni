function t(arr) {
    let townsArray = arr.map(element => {
        let [town, latitude, longitude] = element.split(" | ");
        return {
            town: town,
            latitude: (+latitude).toFixed(2),
            longitude: (+longitude).toFixed(2)
        };
    });

    townsArray.forEach(townObj => {
        console.log(`{ town: '${townObj.town}', latitude: '${townObj.latitude}', longitude: '${townObj.longitude}' }`);
    });

}

//or 

function towns(arr) {
    arr.forEach(element => { let [town,latitude,longitude] = element.split(" | ")
        console.log(`{ town: '${town}', latitude: '${Number(latitude).toFixed(2)}', longitude: '${(+longitude).toFixed(2)}' }`)
        
    });
}
