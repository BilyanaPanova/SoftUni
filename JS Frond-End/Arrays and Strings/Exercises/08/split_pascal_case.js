function splitPascalCase(pascalCaseString) {
    const words = pascalCaseString.match(/[A-Z][a-z]*/g);
    const result = words.join(', ');

    console.log(result);
}
