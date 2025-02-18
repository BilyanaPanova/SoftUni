function solve() {
    let restorants = document.querySelector("#inputs textarea").value
    restorants = JSON.parse(restorants)
    console.log(restorants)
    let restInfo = {}

    restorants.forEach(element => {
        let [currRName,employees] = element.split(" - ")
        if (! (currRName in restInfo)) {
            restInfo[currRName] = []
        }
        employees.split(", ").forEach(employee => {
            
            let [name, salary] = employee.split(" ");
            salary = Number(salary);
        
            restInfo[currRName].push({ "Name": name, "Salary": salary });
        });
        let avgSalary = restInfo[currRName].reduce((sum, emp) => sum + emp.Salary, 0) / restInfo[currRName].length;
        restInfo[currRName]["Avg"] = Number(avgSalary.toFixed(2))

    });

    let bestRestaurant = Object.keys(restInfo).sort((a, b) => {
        return restInfo[b].Avg - restInfo[a].Avg;
    })[0];

    let bestSalary = restInfo[bestRestaurant].sort((a, b) => b.Salary - a.Salary)[0]["Salary"]

    let bestRestaurantText = `Name: ${bestRestaurant} Average Salary: ${restInfo[bestRestaurant]["Avg"].toFixed(2)} Best Salary: ${bestSalary.toFixed(2)}`

    let employeesText = ''
    restInfo[bestRestaurant].forEach(employee => {
        employeesText += `Name: ${employee.Name} With Salary: ${employee.Salary}` + " ";
    });

    let bestRestaurantQuery = document.querySelector("#bestRestaurant > p")
    let workers = document.querySelector("#workers > p")
    bestRestaurantQuery.textContent = bestRestaurantText
    workers.textContent = employeesText
}
