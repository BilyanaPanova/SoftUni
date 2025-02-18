document.addEventListener('DOMContentLoaded', solve);

function solve() {
   const products = document.querySelectorAll('.product');
   const textarea = document.querySelector('textarea'); 
   const checkoutButton = document.querySelector('.checkout'); 

   let cart = new Map(); 

  
   products.forEach(product => {
       const addButton = product.querySelector('.add-product');
       addButton.addEventListener('click', () => {
           const name = product.querySelector('.product-title').textContent;
           const price = parseFloat(product.querySelector('.product-line-price').textContent).toFixed(2); 

           if (!cart.has(name)) {
               cart.set(name, { price: parseFloat(price), quantity: 0 });
           }
           cart.get(name).quantity++;
   
           textarea.textContent += `Added ${name} for ${price} to the cart.\n`;
       });
   });

   checkoutButton.addEventListener('click', () => {

       let totalPrice = 0;
       const productList = [];

       cart.forEach((info, name) => {
           productList.push(name); 
           totalPrice += info.price * info.quantity; 
       });

       textarea.textContent += `You bought ${productList.join(', ')} for ${totalPrice.toFixed(2)}.\n`;

       document.querySelectorAll('button').forEach(button => button.disabled = true);
   });
}
