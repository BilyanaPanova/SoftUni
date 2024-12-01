function solve() {
   const searchInput = document.getElementById("searchField");
   const searchText = searchInput.value.trim().toLowerCase(); 
   const tableRows = document.querySelectorAll("tbody tr"); 

   tableRows.forEach(row => row.classList.remove("select"));

   if (searchText === "") {
       return; 
   }

   tableRows.forEach(row => {
       const cells = Array.from(row.querySelectorAll("td")); 
       const matchFound = cells.some(cell => cell.textContent.toLowerCase().includes(searchText));

       if (matchFound) {
           row.classList.add("select"); 
       }
   });

   searchInput.value = "";
}

