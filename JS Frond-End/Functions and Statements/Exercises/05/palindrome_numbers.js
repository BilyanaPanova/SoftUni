function palindromeNumbers(arr) {
    function isValid(number) {
        const strNumber = String(number);
        const reversedNumber = strNumber.split('').reverse().join('');
        return strNumber === reversedNumber;
    }

    arr.forEach(num => {
        console.log(isValid(num));
    });
}
