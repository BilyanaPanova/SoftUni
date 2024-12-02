function addItem() {
    let parent = document.querySelector("#items");
    let textToAdd = document.querySelector("#newItemText");

    let newLi = document.createElement("li")
    newLi.textContent = textToAdd.value

    let newA = document.createElement("a")
    newA.textContent = "[Delete]"
    newA.href = "#"

    newA.addEventListener("click", function (event) {
        event.preventDefault();
        newLi.remove();      
    });

    newLi.appendChild(newA)
    parent.appendChild(newLi)

    textToAdd.value = ""
}
