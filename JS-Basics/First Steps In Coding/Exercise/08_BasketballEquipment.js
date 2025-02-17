function basketballExpenses(annualFee) {
    let shoesPrice = annualFee * 0.6;
    let outfitPrice = shoesPrice * 0.8;
    let ballPrice = outfitPrice / 4;
    let accessoriesPrice = ballPrice / 5;

    let totalExpenses = annualFee + shoesPrice + outfitPrice + ballPrice + accessoriesPrice;

    console.log(totalExpenses);
}
