document.addEventListener('DOMContentLoaded', solve);

function solve() {
  const generateButton = document.querySelector("#input > input");
  const buyButton = document.querySelector("#shop > input");
  const table = document.querySelector("tbody");
  const output = document.querySelector("#shop > textarea");

  generateButton.addEventListener("click", (event) => {
    event.preventDefault();

    const input = document.querySelector("#input > textarea");
    const furnitureArray = [...JSON.parse(input.value)];

    for (const furniture of furnitureArray) {
      const newRow = document.createElement("tr");
  
      const furnitureData = [
          { content: `<img src="${furniture.img}" />`, type: "html" }, 
          { content: furniture.name, type: "text" },
          { content: furniture.price, type: "text" },
          { content: furniture.decFactor, type: "text" }, 
          { content: `<input type="checkbox">`, type: "html" }, 
      ];
  
      furnitureData.forEach(data => {
          const cell = document.createElement("td");
          if (data.type === "html") {
              cell.innerHTML = data.content;
          } else {
              const p = document.createElement("p");
              p.textContent = data.content;
              cell.appendChild(p);
          }
          newRow.appendChild(cell);
      });
  
      table.appendChild(newRow);
  }

    input.value = "";
  });

  buyButton.addEventListener("click", (event) => {
    event.preventDefault();
    const selectedFurniture = [];
    let totalPrice = 0;
    let totalFactor = 0;
    let count = 0;

    const rows = table.querySelectorAll("tr");

    for (const row of rows) {
      const checkbox = row.querySelector("input[type='checkbox']");
      if (checkbox && checkbox.checked) {
        const name = row.querySelector("td:nth-child(2) p").textContent;
        const price = parseFloat(row.querySelector("td:nth-child(3) p").textContent);
        const factor = parseFloat(row.querySelector("td:nth-child(4) p").textContent);

        selectedFurniture.push(name);
        totalPrice += price;
        totalFactor += factor;
        count++;
      }
    }

    const averageFactor = count > 0 ? totalFactor / count : 0;

    output.value = `Bought furniture: ${selectedFurniture.join(", ")}\n`;
    output.value += `Total price: ${totalPrice}\n`;
    output.value += `Average decoration factor: ${averageFactor}`;
  });
}
