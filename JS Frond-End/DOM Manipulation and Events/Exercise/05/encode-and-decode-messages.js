document.addEventListener('DOMContentLoaded', solve);
function solve() {
    const messageArea = document.querySelector("#encode > textarea");
    const decodeArea = document.querySelector("#decode > textarea");

    document.body.addEventListener("click", (event) => {
        event.preventDefault();

        switch (event.target.textContent.trim()) {
            case "Encode and send it":

                const encodedMessage = messageArea.value
                    .split("")
                    .map(char => String.fromCharCode(char.charCodeAt() + 1))
                    .join('');

                decodeArea.value = encodedMessage;
                messageArea.value = "";
                break;

            case "Decode and read it":
                decodeArea.value =  decodeArea.value
                .split("")
                .map(char => String.fromCharCode(char.charCodeAt() - 1))
                .join('');
                break;
        }
    });
}


//or


document.addEventListener('DOMContentLoaded', solve);

function solve() {
    let messageArea = document.querySelector("#encode > textarea")
    let decodeArea = document.querySelector("#decode > textarea")
    const encodeButton = document.querySelector("#encode > button")
    const decodeButton = document.querySelector("#decode > button")
    
    

    encodeButton.addEventListener("click",(event) => {
        event.preventDefault();
        let decodeMessage = messageArea.value.split("")
        .map(char => String.fromCharCode(char.charCodeAt() + 1))
        .join('');
        decodeArea.value = decodeMessage
        messageArea.value = ""
    });

    decodeButton.addEventListener("click", (event) => {
        event.preventDefault();
        decodeArea.value = decodeArea.value.split("")
        .map(char => String.fromCharCode(char.charCodeAt() - 1))
        .join('');
    })
}
