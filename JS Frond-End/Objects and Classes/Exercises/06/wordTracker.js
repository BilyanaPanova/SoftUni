function wordTracker(arr) {

    let keys = arr[0].split(" ").reduce((acc, empl) => {
        acc[empl] = 0;
        return acc;
    }, {});
    
    for (let i = 1;i < arr.length; i++) {
        if (arr[i] in keys) {
            keys[arr[i]] += 1 
        }
    }

    const sortable = Object.fromEntries(
        Object.entries(keys).sort(([,a],[,b]) => b - a)
    );
    Object.keys(sortable).forEach(element => {
        console.log(`${element} - ${sortable[element]}`)
    });
    
}
