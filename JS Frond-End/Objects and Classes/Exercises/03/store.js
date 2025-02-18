function store(products,order) {
    let allproducts = products.concat(order)
    let stock = {}

    for (let i=0;i < allproducts.length;i+=2) {
        let product = allproducts[i];
        let quantity = +allproducts[i + 1];

        if (product in stock) {
            stock[product] += quantity;
        } else {
            stock[product] = quantity;
        }
    }
    
    Object.keys(stock).forEach(element => { console.log(`${element} -> ${stock[element]}`)});
}
