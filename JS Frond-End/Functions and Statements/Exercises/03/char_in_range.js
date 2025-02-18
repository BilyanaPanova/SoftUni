function charInRange(char1, char2) {
    let asciiChars = [char1.charCodeAt(0), char2.charCodeAt(0)];
    
    let [start,end] = asciiChars.sort((a,b)=> a-b)

    for (let i = start + 1; i < end; i++) {
        process.stdout.write(String.fromCharCode(i) + " ");
    }
}
