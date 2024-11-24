function solve() {

  let text = document.getElementById("text").value
  let namingConvention = document.getElementById("naming-convention").value
  let result = "Error!"

  switch (namingConvention) {
    case "Camel Case":
      result = text.toLowerCase().split(" ").reduce((s, c) => s
      + (c.charAt(0).toUpperCase() + c.slice(1)));
      break;
  
    case "Pascal Case":
      result = text.toLowerCase().split(" ").reduce((s, c) => s
      + (c.charAt(0).toUpperCase() + c.slice(1)),"");
      break;
  } 

  let spanResult = document.getElementById("result")
  spanResult.textContent = result

}

//or 

function solve() {
  const text = document.getElementById("text").value.trim();
  const namingConvention = document.getElementById("naming-convention").value;

  let result;

  switch (namingConvention) {
    case "Camel Case":
      result = text
        .toLowerCase()
        .split(" ")
        .map((word, index) => 
          index === 0 ? word : word.charAt(0).toUpperCase() + word.slice(1)
        )
        .join("");
      break;

    case "Pascal Case":
      result = text
        .toLowerCase()
        .split(" ")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join("");
      break;

    default:
      result = "Error!";
      break;
  }

  document.getElementById("result").textContent = result;
}
