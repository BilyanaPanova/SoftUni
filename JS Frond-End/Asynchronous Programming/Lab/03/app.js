function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/forecaster';
    const locationInput = document.getElementById('location');
    const submitButton = document.getElementById('submit');
    const forecastDiv = document.getElementById('forecast');
    const currentDiv = document.getElementById('current');
    const upcomingDiv = document.getElementById('upcoming');

    const weatherSymbols = {
        Sunny: '&#x2600;', 
        'Partly sunny': '&#x26C5;', 
        Overcast: '&#x2601;', 
        Rain: '&#x2614;', 
        Degrees: '&#176;' 
    };

    submitButton.addEventListener('click', async () => {
        try {
            forecastDiv.style.display = 'block'; 
            currentDiv.innerHTML = ''; 
            upcomingDiv.innerHTML = '';

            const locationName = locationInput.value.trim();

            const locationsResponse = await fetch(`${baseUrl}/locations`);
            if (!locationsResponse.ok) {
                throw new Error('Failed to fetch locations');
            }
            const locations = await locationsResponse.json();

            const location = locations.find(loc => loc.name.toLowerCase() === locationName.toLowerCase());
            if (!location) {
                throw new Error('Location not found');
            }

            const locationCode = location.code;

            const todayResponse = await fetch(`${baseUrl}/today/${locationCode}`);
            if (!todayResponse.ok) {
                throw new Error('Failed to fetch current weather');
            }
            const todayData = await todayResponse.json();

            const upcomingResponse = await fetch(`${baseUrl}/upcoming/${locationCode}`);
            if (!upcomingResponse.ok) {
                throw new Error('Failed to fetch 3-day forecast');
            }
            const upcomingData = await upcomingResponse.json();

            renderCurrentConditions(todayData);
            renderUpcomingForecast(upcomingData);

        } catch (error) {
            renderError();
        }
    });

    function renderCurrentConditions(data) {
        const { name, forecast } = data;
        const { condition, high, low } = forecast;

        const labelDiv = document.createElement('div');
        labelDiv.className = 'label';
        labelDiv.textContent = 'Current conditions';

        const forecastsDiv = document.createElement('div');
        forecastsDiv.className = 'forecasts';

        const symbolSpan = document.createElement('span');
        symbolSpan.className = 'condition symbol';
        symbolSpan.innerHTML = weatherSymbols[condition];

        const conditionSpan = document.createElement('span');
        conditionSpan.className = 'condition';

        const locationSpan = document.createElement('span');
        locationSpan.className = 'forecast-data';
        locationSpan.textContent = name;

        const temperatureSpan = document.createElement('span');
        temperatureSpan.className = 'forecast-data';
        temperatureSpan.textContent = `${forecast.low}°/${forecast.high}°`

        const conditionTextSpan = document.createElement('span');
        conditionTextSpan.className = 'forecast-data';
        conditionTextSpan.textContent = condition;

        conditionSpan.append(locationSpan, temperatureSpan, conditionTextSpan);
        forecastsDiv.append(symbolSpan, conditionSpan);

        currentDiv.append(labelDiv, forecastsDiv);
    }

    function renderUpcomingForecast(data) {
        const labelDiv = document.createElement('div');
        labelDiv.className = 'label';
        labelDiv.textContent = 'Three-day forecast';

        const forecastInfoDiv = document.createElement('div');
        forecastInfoDiv.className = 'forecast-info';

        data.forecast.forEach(day => {
            const { condition, high, low } = day;

            const upcomingSpan = document.createElement('span');
            upcomingSpan.className = 'upcoming';

            const symbolSpan = document.createElement('span');
            symbolSpan.className = 'symbol';
            symbolSpan.innerHTML = weatherSymbols[condition];

            const temperatureSpan = document.createElement('span');
            temperatureSpan.className = 'forecast-data';
            temperatureSpan.textContent = `${low}°/${high}°`;

            const conditionSpan = document.createElement('span');
            conditionSpan.className = 'forecast-data';
            conditionSpan.textContent = condition;

            upcomingSpan.append(symbolSpan, temperatureSpan, conditionSpan);
            forecastInfoDiv.appendChild(upcomingSpan);
        });

        upcomingDiv.append(labelDiv, forecastInfoDiv);
    }

    function renderError() {
        forecastDiv.style.display = 'block';
        forecastDiv.innerHTML = '<div class="label">Error</div>';
    }
}

attachEvents();
