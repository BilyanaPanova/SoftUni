document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const timeConverter = {
        days: (days) => ({
            days: days * 1,
            hours: days * 24,
            minutes: days * 24 * 60,
            seconds: days * 24 * 60 * 60,
        }),
        hours: (hours) => ({
            days: hours / 24,
            hours: hours * 1,
            minutes: hours * 60,
            seconds: hours * 60 * 60,
        }),
        minutes: (minutes) => ({
            days: minutes / (24 * 60),
            hours: minutes / 60,
            minutes: minutes * 1,
            seconds: minutes * 60,
        }),
        seconds: (seconds) => ({
            days: seconds / (24 * 60 * 60),
            hours: seconds / (60 * 60),
            minutes: seconds / 60,
            seconds: seconds * 1
        }),
    };

    const main = document.querySelector('main');

    main.addEventListener('submit', (event) => {
        event.preventDefault(); 
        const form = event.target; 
        const input = form.querySelector('input[type="number"]'); 
        const value = parseFloat(input.value);

        const unit = form.id;
        const convertedValues = timeConverter[unit](value);

        document.getElementById('days-input').value = convertedValues.days.toFixed(2);
        document.getElementById('hours-input').value = convertedValues.hours.toFixed(2);
        document.getElementById('minutes-input').value = convertedValues.minutes.toFixed(2);
        document.getElementById('seconds-input').value = convertedValues.seconds.toFixed(2);
    });
}
