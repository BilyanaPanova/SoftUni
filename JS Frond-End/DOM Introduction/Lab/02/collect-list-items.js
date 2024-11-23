function extractText() {
    let ulElement = document.getElementById("items")
    let elements = Array.from(ulElement.children)
    let string = elements.map(item => item.textContent).join('\n');

    let textarea = document.getElementById("result") 
    textarea.textContent = string

}
