const baseURL = 'http://localhost:3030/jsonstore/advanced/profiles';

async function lockedProfile() {
    const main = document.getElementById('main');
    main.innerHTML = ''; 

    try {
        const response = await fetch(baseURL);
        const data = await response.json();

        Object.values(data).forEach((user, index) => {
            const profileElement = createProfileElement(user, index + 1);
            main.appendChild(profileElement);
        });
    } catch (error) {
        console.error('Error fetching profiles:', error);
    }
}

function createProfileElement(user, userIndex) {
    const profileDiv = document.createElement('div');
    profileDiv.className = 'profile';

    profileDiv.innerHTML = `
        <img src="./iconProfile2.png" class="userIcon" />
        <label>Lock</label>
        <input type="radio" name="user${userIndex}Locked" value="lock" checked>
        <label>Unlock</label>
        <input type="radio" name="user${userIndex}Locked" value="unlock"><br>
        <hr>
        <label>Username</label>
        <input type="text" name="user${userIndex}Username" value="${user.username}" disabled readonly />
        <div class="hiddenFields" style="display: none;">
            <hr>
            <label>Email:</label>
            <input type="email" name="user${userIndex}Email" value="${user.email}" disabled readonly />
            <label>Age:</label>
            <input type="number" name="user${userIndex}Age" value="${user.age}" disabled readonly />
        </div>
        <button>Show more</button>
    `;

    const lockRadio = profileDiv.querySelector(`input[name="user${userIndex}Locked"][value="lock"]`);
    const unlockRadio = profileDiv.querySelector(`input[name="user${userIndex}Locked"][value="unlock"]`);
    const hiddenFields = profileDiv.querySelector('.hiddenFields');
    const toggleButton = profileDiv.querySelector('button');

    toggleButton.addEventListener('click', () => {
        if (unlockRadio.checked) {
            if (hiddenFields.style.display === 'none') {
                hiddenFields.style.display = 'block';
                toggleButton.textContent = 'Hide it';
            } else {
                hiddenFields.style.display = 'none';
                toggleButton.textContent = 'Show more';
            }
        }
    });

    return profileDiv;
}

lockedProfile();
