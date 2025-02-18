document.addEventListener('DOMContentLoaded', solve);

function solve() {
    document.getElementById('solutionCheck').addEventListener('submit', function(event) {
        event.preventDefault();  
    
        const inputs = document.querySelectorAll('table input');
    
        const grid = [];
        let currentRow = [];
        inputs.forEach((input, index) => {
            currentRow.push(parseInt(input.value));
            if ((index + 1) % 3 === 0) { 
                grid.push(currentRow);
                currentRow = [];
            }
        });
    
        const isValid = checkSudoku(grid);
    
        const table = document.querySelector('table');
        const checkMessage = document.getElementById('check');
    
        if (isValid) {
            table.style.border = '2px solid green';
            checkMessage.textContent = 'Success!';
        } else {
            table.style.border = '2px solid red';
            checkMessage.textContent = 'Keep trying ...';
        }
    });
    
    function checkSudoku(grid) {
        for (let row of grid) {
            if (!isValidRowOrColumn(row)) {
                return false;
            }
        }
    
        for (let col = 0; col < 3; col++) {
            const column = grid.map(row => row[col]);
            if (!isValidRowOrColumn(column)) {
                return false;
            }
        }
    
        return true;
    }
    
    function isValidRowOrColumn(arr) {
        const uniqueValues = new Set(arr);
        return uniqueValues.size === 3 && arr.every(value => value >= 1 && value <= 3);
    }
    
    document.querySelector('input[type="reset"]').addEventListener('click', function() {
        const inputs = document.querySelectorAll('table input');
        inputs.forEach(input => input.value = ''); 
        document.getElementById('check').textContent = ''; 
        document.querySelector('table').style.border = '';  
    });
    
}
