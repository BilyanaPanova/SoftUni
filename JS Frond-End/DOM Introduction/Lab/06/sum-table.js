function sumTable() {
    let allPriceCells = document.querySelectorAll("tbody tr td:nth-child(2)");

    let total = Array.from(allPriceCells)
        .map(cell => Number(cell.innerText)) 
        .reduce((sum, price) => sum + price, 0); 


    document.getElementById("sum").textContent = total.toFixed(2);
}


//or

function sumTable() {
    let allPrices = document.querySelectorAll("tbody tr td")

    allPrices = Array(Number(allPrices[1].innerText),Number(allPrices[3].innerText),Number(allPrices[5].innerText))

    total = allPrices.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    
    let totalElement = document.getElementById("sum")
    totalElement.textContent = total
}
