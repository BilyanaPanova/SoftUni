function attachEvents() {
    const baseURL = "http://localhost:3030/jsonstore/messenger"

    const textarea = document.querySelector("#messages")
    const inputAuthor = document.querySelector("[name='author']")
    const inputContent = document.querySelector("[name='content']")

    const sendButton = document.querySelector("#submit")
    const refreshButton = document.querySelector("#refresh")

    sendButton.addEventListener("click",() => {

        let author = inputAuthor.value
        let content = inputContent.value
        const text = {author,content}
        inputAuthor.value = ""
        inputContent.value = ""

        fetch(baseURL,{
            method: "POST",
            body: JSON.stringify(text)
        })
            .then(response => response.json())
            .then(response => {
                inputAuthor.value = ""
                inputContent.value = ""
            })
            .catch(error => console.error("Error: ",error))
    })

    refreshButton.addEventListener("click", () => {
        textarea.textContent = ""

        fetch(baseURL)
            .then(response => response.json())
            .then(messages => {
                Object.values(messages).forEach((message, index, arr) => {
                    if (index === arr.length - 1) {
                        textarea.textContent += `${message.author}: ${message.content}`;
                    } else {
                        textarea.textContent += `${message.author}: ${message.content}\n`;
                    }
                });
            })
            .catch(error => console.error("Error: ",error))
    })

}

attachEvents();
