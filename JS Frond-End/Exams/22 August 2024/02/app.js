window.addEventListener("load", solve);

function solve() {

   

    const laptopModel = document.querySelector("#laptop-model")
    const storageSpace = document.querySelector("#storage")
    const price = document.querySelector("#price")

    const checkList = document.querySelector("#check-list")

    const addButton = document.querySelector("#add-btn")
    const clearButton = document.querySelector(".btn.clear")

    addButton.addEventListener("click", clickedAdd)
    clearButton.addEventListener("click", clear)

    function clickedAdd() {
      let newLi = document.createElement("li");
      newLi.className = "laptop-item";
    
      if (!laptopModel.value || !storageSpace.value || !price.value) {
        return;
      }
    
      newLi.innerHTML = `
        <article>
          <p>${laptopModel.value}</p>
          <p>Memory: ${storageSpace.value} TB</p>
          <p>Price: ${price.value}$</p>
        </article>
        <button class="btn edit">edit</button>
        <button class="btn ok">ok</button>
      `;
    
      checkList.appendChild(newLi);
      const values = [laptopModel.value,storageSpace.value,price.value]
      laptopModel.value = "";
      storageSpace.value = "";
      price.value = "";
      addButton.disabled = true;
    
      const editButton = newLi.querySelector(".btn.edit");
      const okButton = newLi.querySelector(".btn.ok");
    
      editButton.addEventListener("click", () => {
    
        laptopModel.value = values[0];
        storageSpace.value = values[1];
        price.value = values[2];
    
        checkList.removeChild(newLi);
        addButton.disabled = false;
      });
    
      okButton.addEventListener("click", () => {
        const laptopList = document.querySelector("#laptops-list");
    
        const li = document.createElement("li");
        li.className = "laptop-item"
        li.innerHTML = newLi.querySelector("article").outerHTML;
    
        laptopList.appendChild(li);
        checkList.removeChild(newLi);
        addButton.disabled = false;
      });
    }
 
    function clear () {
      location.reload()
    }

    
}
