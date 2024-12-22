function calculateClimberPercentages(input) {
    const groupCount = parseInt(input[0]); // Брой групи
    const groups = input.slice(1).map(Number); // Преобразуване на броя на хората във всяка група към числа

    // Променливи за броя катерачи на всеки връх
    let musala = 0;
    let montBlanc = 0;
    let kilimanjaro = 0;
    let k2 = 0;
    let everest = 0;

    const totalClimbers = groups.reduce((sum, climbers) => sum + climbers, 0);

    for (const climbers of groups) {
        if (climbers <= 5) {
            musala += climbers;
        } else if (climbers <= 12) {
            montBlanc += climbers;
        } else if (climbers <= 25) {
            kilimanjaro += climbers;
        } else if (climbers <= 40) {
            k2 += climbers;
        } else {
            everest += climbers;
        }
    }

    const percentages = [
        (musala / totalClimbers) * 100,
        (montBlanc / totalClimbers) * 100,
        (kilimanjaro / totalClimbers) * 100,
        (k2 / totalClimbers) * 100,
        (everest / totalClimbers) * 100,
    ];
  
    percentages.forEach(percentage => {
        console.log(`${percentage.toFixed(2)}%`);
    });
}
