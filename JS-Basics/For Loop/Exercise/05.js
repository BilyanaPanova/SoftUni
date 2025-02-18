function calculateRemainingSalary(input) {
    const n = input[0];
    let salary = input[1]; 

    const penalties = {
        "Facebook": 150,
        "Instagram": 100,
        "Reddit": 50
    };

    for (let i = 2; i < input.length; i++) {
        const site = input[i];
        if (penalties[site]) {
            salary -= penalties[site];
        }
        if (salary <= 0) {
            console.log("You have lost your salary.");
            return;
        }
    }

    console.log(salary);
}
