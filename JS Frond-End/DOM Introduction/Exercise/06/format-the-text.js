function solve() {
  let text = document.querySelector("#input").value.trim();
  let sentences = text.split(". ")
  let outputDiv = document.querySelector("#output");
  
  outputDiv.innerHTML = '';

  while (sentences.length > 0) {
  
      let currentSentences = sentences.splice(0, 3);
      let paragraph = `<p>${currentSentences.join(".")}</p>`;
      
      outputDiv.innerHTML += paragraph;
  }
}
