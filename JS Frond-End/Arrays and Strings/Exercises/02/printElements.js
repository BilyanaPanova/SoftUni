function printElements(arr,step) {
    let result = []

    arr.forEach((element,index) => {
        if (index % step == 0) result.push(element)
        });

    return result
}
