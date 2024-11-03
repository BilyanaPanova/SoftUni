function findWord(word, text) {
    const lowerCaseText = text.toLowerCase().split(" ");

    if (lowerCaseText.includes(word)) {
        console.log(word);

    } else {
        console.log(`${word} not found!`);
    }
}
