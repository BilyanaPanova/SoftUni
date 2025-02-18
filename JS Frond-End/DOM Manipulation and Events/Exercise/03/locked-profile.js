document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const profiles = document.querySelectorAll('.profile');

    profiles.forEach(profile => {
        const lockInput = profile.querySelector('input[type="radio"][id$="Lock"]');
        const unlockInput = profile.querySelector('input[type="radio"][id$="Unlock"]');
        const hiddenFields = profile.querySelector('.hidden-fields');
        const button = profile.querySelector('button');

        button.addEventListener('click', () => {
            if (unlockInput.checked) {
                if (button.textContent === 'Show more') {
                    hiddenFields.style.display = 'block';
                    button.textContent = 'Hide it';
                } else {
                    hiddenFields.style.display = 'none';
                    button.textContent = 'Show more';
                }
            }
        });

        lockInput.addEventListener('change', () => {
            hiddenFields.style.display = 'none'; 
            button.textContent = 'Show more'; 
        });
    });
}
