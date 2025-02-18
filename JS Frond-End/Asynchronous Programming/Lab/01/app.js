function getInfo() {
    const baseUrl = "http://localhost:3030/jsonstore/bus/businfo";
    const stopElement = document.getElementById("stopId");
    const stopNameElement = document.getElementById("stopName");
    const busesElement = document.getElementById("buses");

    const stopId = stopElement.value;
    fetch(`${baseUrl}/${stopId}`)
        .then(res => res.json())
        .then(data => {
            stopNameElement.textContent = data.name

            for (const bussId in data.buses) {
                const liElement = document.createElement("li");
                liElement.textContent = `Bus ${bussId} arrives in ${data.buses[bussId]} minutes`;
                busesElement.appendChild(liElement);
            }
        })
    .catch(() => {
        stopNameElement.textContent = "Error"
    })
}
