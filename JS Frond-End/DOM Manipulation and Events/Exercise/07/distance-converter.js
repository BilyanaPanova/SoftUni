document.addEventListener('DOMContentLoaded', solve);

function solve() {
    document.getElementById('convert').addEventListener('click', function() {
        const inputDistance = parseFloat(document.getElementById('inputDistance').value);
        const inputUnits = document.getElementById('inputUnits').value;
        const outputUnits = document.getElementById('outputUnits').value;
        const outputDistanceField = document.getElementById('outputDistance');
    
        const toMeters = {
            'km': 1000,
            'm': 1,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34,
            'yrd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        };
    
        const fromMeters = {
            'km': 1 / 1000,
            'm': 1,
            'cm': 100,
            'mm': 1000,
            'mi': 1 / 1609.34,
            'yrd': 1 / 0.9144,
            'ft': 1 / 0.3048,
            'in': 1 / 0.0254
        };
    
        if (isNaN(inputDistance)) {
            outputDistanceField.value = "Please enter a valid number";
            return;
        }
    
        const meters = inputDistance * toMeters[inputUnits];
    
        const result = meters * fromMeters[outputUnits];
    
        outputDistanceField.value = result.toFixed(2); 
    });
    
}
