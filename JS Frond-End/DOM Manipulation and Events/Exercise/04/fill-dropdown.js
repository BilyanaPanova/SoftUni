function solve() {
    document.querySelector("[type='submit']").addEventListener("click", (event) => {
        event.preventDefault();

        const inputText = document.querySelector("#newItemText").value;
        const inputValue = document.querySelector("#newItemValue").value;

        if (inputText && inputValue) {
            document.querySelector("#menu").insertAdjacentHTML(
                "beforeend",
                `<option value="${inputValue}">${inputText}</option>`
            );

            document.querySelector("#newItemText").value = "";
            document.querySelector("#newItemValue").value = "";
        }
    });
}


//or 

document.addEventListener('DOMContentLoaded', solve);

function solve() {

    let submit = document.querySelector("[type='submit']")
    let menu = document.querySelector("#menu")

    submit.addEventListener("click", (event) => {
        event.preventDefault();

        const inputText = document.querySelector("#newItemText")
        const inputValue = document.querySelector("#newItemValue")

        let newOption = document.createElement("option")
        newOption.textContent = inputText.value
        newOption.value = inputValue.value

        menu.appendChild(newOption)

        inputText.value = "";
        inputValue.value = "";
    })
}
