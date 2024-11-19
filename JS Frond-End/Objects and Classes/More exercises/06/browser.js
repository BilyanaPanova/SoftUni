function browser(info,arr) {
    arr.forEach(element => {
        let [status,page] = element.split(" ")
        if (status == "Close" && info["Open Tabs"].includes(page)) {
            let index = info["Open Tabs"].indexOf(page)
            info["Open Tabs"].splice(index,1)
            info["Recently Closed"].push(page)
            info["Browser Logs"].push(element)
        }
        else if (status == "Open") {
            info["Open Tabs"].push(page)
            info["Browser Logs"].push(element)
        }
        else if (status == "Clear") {
            info["Open Tabs"] = []
            info["Browser Logs"] = []
            info["Recently Closed"] = []
        }
        
    });
    
    console.log(`${info["Browser Name"]}\nOpen Tabs: ${info["Open Tabs"].join(", ")}\nRecently Closed: ${info["Recently Closed"].join(", ")}\nBrowser Logs: ${info["Browser Logs"].join(", ")}`)
 
}
