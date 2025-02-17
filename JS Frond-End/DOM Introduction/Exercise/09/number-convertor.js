function solve() {
    let inputField = Number(document.getElementById("input").value);
    let resultField = document.getElementById("result");
    let conversionType = document.getElementById("selectMenuTo").value
    
   
    if (conversionType == "binary") {
        resultField.value = inputField.toString(2)
    } else if (conversionType == "hexadecimal") {
        resultField.value = inputField.toString(16).toUpperCase(); // Convert to uppercase hexadecimal
    } 
    
}
