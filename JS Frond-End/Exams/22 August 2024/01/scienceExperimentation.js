function solve(arr) {

    let n = parseInt(arr[0]); 
    let chemicals = {};

    for (let i = 1; i <= n; i++) {
        let [name, quantity] = arr[i].split(' # ');
        chemicals[name] = { quantity: parseInt(quantity), formula: null };
    }

    for (let i = n + 1; i < arr.length; i++) {
        let command = arr[i].trim();
        
        if (command === 'End') {
            break;
        }

        let parts = command.split(' # ');
        let action = parts[0];

        if (action === 'Mix') {
            let name1 = parts[1], name2 = parts[2], amount = parseInt(parts[3]);
            if (chemicals[name1] && chemicals[name2]) {
                if (chemicals[name1].quantity >= amount && chemicals[name2].quantity >= amount) {
                    chemicals[name1].quantity -= amount;
                    chemicals[name2].quantity -= amount;
                    console.log(`${name1} and ${name2} have been mixed. ${amount} units of each were used.`);
                } else {
                    console.log(`Insufficient quantity of ${name1}/${name2} to mix.`);
                }
            }
        }
        else if (action === 'Replenish') {
            let name = parts[1], amount = parseInt(parts[2]);
            if (chemicals[name]) {
                let newQuantity = chemicals[name].quantity + amount;
                if (newQuantity > 500) {
                    let addedAmount = 500 - chemicals[name].quantity;
                    chemicals[name].quantity = 500;
                    console.log(`${name} quantity increased by ${addedAmount} units, reaching maximum capacity of 500 units!`);
                } else {
                    chemicals[name].quantity = newQuantity;
                    console.log(`${name} quantity increased by ${amount} units!`);
                }
            } else {
                console.log(`The Chemical ${name} is not available in the lab.`);
            }
        }
        else if (action === 'Add Formula') {
            let name = parts[1], formula = parts[2];
            if (chemicals[name]) {
                chemicals[name].formula = formula;
                console.log(`${name} has been assigned the formula ${formula}.`);
            } else {
                console.log(`The Chemical ${name} is not available in the lab.`);
            }
        }
    }

    for (let name in chemicals) {
        let { quantity, formula } = chemicals[name];
        if (formula) {
            console.log(`Chemical: ${name}, Quantity: ${quantity}, Formula: ${formula}`);
        } else {
            console.log(`Chemical: ${name}, Quantity: ${quantity}`);
        }
    }
}
