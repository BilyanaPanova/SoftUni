function solve() {
      const searchBox = document.getElementById('searchText');
      const searchText = searchBox.value.toLowerCase();
      const towns = document.querySelectorAll('#towns li');
      const result = document.getElementById('result');
  
      let matches = 0;
  
      towns.forEach(town => {
      
          town.style.fontWeight = ''; 
          town.style.textDecoration = ''; 
          town.style.opacity = ''; 
      });
  
      towns.forEach(town => {
          if (town.textContent.toLowerCase().includes(searchText)) {
         
              town.style.fontWeight = 'bold'; 
              town.style.textDecoration = 'underline'; 
              town.style.opacity = '1'; 
              matches++;
          }
      });
  
      result.textContent = `${matches} matches found`;

  
}
