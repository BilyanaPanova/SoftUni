function loadingBar(percentage) {
    let progress = '%'.repeat(percentage / 10); 
    let dots = '.'.repeat(10 - (percentage / 10)); 
    let loadingBar = progress + dots; 
    
    if (percentage === 100) {
        console.log("100% Complete!");
        console.log(loadingBar);
    } else {
        console.log(`${percentage}% [${loadingBar}]`);
        console.log("Still loading...");
    }
}
