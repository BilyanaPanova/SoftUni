const baseURL = 'http://localhost:3030/jsonstore/advanced/articles';

async function loadArticles() {
    const mainSection = document.getElementById('main');
    mainSection.innerHTML = '';

    try {

        const response = await fetch(`${baseURL}/list`);
        const articlesList = await response.json();

        for (const article of articlesList) {
            const articleElement = createArticleElement(article);
            mainSection.appendChild(articleElement);
        }
    } catch (error) {
        console.error('Error loading articles:', error);
    }
}

function createArticleElement(article) {
    const accordionDiv = document.createElement('div');
    accordionDiv.className = 'accordion';

    accordionDiv.innerHTML = `
        <div class="head">
            <span>${article.title}</span>
            <button class="button" id="${article._id}">More</button>
        </div>
        <div class="extra" style="display: none;">
            <p></p>
        </div>
    `;

    const button = accordionDiv.querySelector('button');
    button.addEventListener('click', () => toggleArticleContent(accordionDiv, article._id, button));

    return accordionDiv;
}

async function toggleArticleContent(accordionDiv, articleId, button) {
    const extraDiv = accordionDiv.querySelector('.extra');
    const paragraph = extraDiv.querySelector('p');

    if (button.textContent === 'More') {
       
        try {
            const response = await fetch(`${baseURL}/details/${articleId}`);
            const articleDetails = await response.json();

            paragraph.textContent = articleDetails.content;
            extraDiv.style.display = 'block';
            button.textContent = 'Less';
        } catch (error) {
            console.error('Error loading article content:', error);
        }
    } else {

        extraDiv.style.display = 'none';
        button.textContent = 'More';
    }
}


loadArticles();
