function addItem() {
    let parent = document.querySelector("#items");
    let textToAdd = document.querySelector("#newItemText");

    let newLi = document.createElement("li")
    newLi.textContent = textToAdd.value

    parent.appendChild(newLi)
    textToAdd.value = ""
}
