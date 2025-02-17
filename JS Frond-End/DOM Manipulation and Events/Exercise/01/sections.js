document.addEventListener('DOMContentLoaded', solve);

function solve() {
   let clickButton = document.querySelector("input[type='submit']");
   let content = document.querySelector("#content");
   let textArray = document.querySelector("input[type='text']").value.split(", ");

   clickButton.addEventListener('click', function (event) {
     
      event.preventDefault();

      textArray.forEach(element => {
         let createDiv = document.createElement("div");
         let createParagraph = document.createElement("p");

         createParagraph.textContent = element;
         createParagraph.style.display = "none"

         createDiv.appendChild(createParagraph);

         createDiv.addEventListener('click', (e) => {
            e.target.querySelector('p').style.display = 'block';
        });

         content.appendChild(createDiv);
         
      });
   });
}
