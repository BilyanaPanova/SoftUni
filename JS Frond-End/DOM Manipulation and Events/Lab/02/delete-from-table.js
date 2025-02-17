function deleteByEmail() {
    let emailToFind = document.querySelector("[type='text']").value.trim();
    let rows = document.querySelectorAll("tbody > tr")
    let result = document.querySelector("#result")

    let isFound = false

    rows.forEach(element => {
        if (element.children[1].textContent.trim() === emailToFind) {
            element.remove()
            isFound = true
        }
    });

    result.textContent = isFound ? "Deleted." : "Not found.";
}
