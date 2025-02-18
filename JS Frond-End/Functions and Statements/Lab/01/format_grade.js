function formatGrade(grade) {
    const gradeAndDescription = {
        5.50:`Excellent (${grade.toFixed(2)})`,
        4.50:`Very good (${grade.toFixed(2)})`,
        3.50:`Good (${grade.toFixed(2)})`,
        3:`Poor (${grade.toFixed(2)})`,
        2: `Fail (2)`
    }

    for (const key of Object.keys(gradeAndDescription).sort((a, b) => b - a)) {
        if (grade >= key) {
            console.log(gradeAndDescription[key]);
            break;
        }
    }
}
