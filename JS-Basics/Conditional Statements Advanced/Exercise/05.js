function vacationBudget(budget, season) {
    let destination = '';
    let place = '';
    let moneySpend = 0;

    if (budget <= 100) {
        destination = "Bulgaria";
      
        moneySpend = season === "summer" 
          ? budget * 0.3 : budget * 0.7;
      
        place = season === "summer" 
          ? "Camp" : "Hotel";
      
    } else if (budget <= 1000) {
        destination = "Balkans";
      
        moneySpend = season === "summer" 
          ? budget * 0.4 : budget * 0.8;
      
        place = season === "summer" 
          ? "Camp" : "Hotel";
      
    } else if (budget > 1000) {
        destination = "Europe";
        moneySpend = budget * 0.9;
        place = "Hotel";
    }

    console.log(`Somewhere in ${destination}`);
    console.log(`${place} - ${moneySpend.toFixed(2)}`);
}
