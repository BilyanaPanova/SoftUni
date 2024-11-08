function addAndSubtract(a, b, c) {
    function sum(a,b) {
        return a + b;
    }

    function subtract(result,c) {
        return result - c
    }

    
    result = subtract(sum(a,b),c)

    return result;
}
