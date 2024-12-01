function extract(content) {
    const targetElement = document.getElementById("content");
    
    const matches = targetElement.textContent.match(/\(([^)]+)\)/g);
    let result =  matches.map(text => text.slice(1, -1)).join(';  ')
    
    return result
}
