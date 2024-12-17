function foodDelivery(chickenMenus,fishMenus,vegetarianMenus) {
    let chickenPrice = 10.35;
    let fishPrice = 12.40;
    let vegetarianPrice = 8.15;
    let deliveryPrice = 2.50;

    let totalMenuPrice = (chickenMenus * chickenPrice) + (fishMenus * fishPrice) + (vegetarianMenus * vegetarianPrice);
    let dessertPrice = totalMenuPrice * 0.2;
    let totalOrderPrice = totalMenuPrice + dessertPrice + deliveryPrice;

    console.log(totalOrderPrice);
}
