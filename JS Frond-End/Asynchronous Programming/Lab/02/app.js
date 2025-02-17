function solve() {
    let currentStop = {
        next: 'depot', 
        name: ''     
    };

    const infoBox = document.querySelector('.info');
    const departButton = document.getElementById('depart');
    const arriveButton = document.getElementById('arrive');

    async function depart() {
        try {
           
            const response = await fetch(`http://localhost:3030/jsonstore/bus/schedule/${currentStop.next}`);
            if (!response.ok) {
                throw new Error('Error fetching data');
            }
            const data = await response.json();

            currentStop.name = data.name;
            currentStop.next = data.next;

            infoBox.textContent = `Next stop ${currentStop.name}`;
            departButton.disabled = true;
            arriveButton.disabled = false;
        } catch (error) {
            handleError();
        }
    }

    function arrive() {
        infoBox.textContent = `Arriving at ${currentStop.name}`;

        departButton.disabled = false;
        arriveButton.disabled = true;
    }

    function handleError() {
        infoBox.textContent = 'Error';
        departButton.disabled = true;
        arriveButton.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
