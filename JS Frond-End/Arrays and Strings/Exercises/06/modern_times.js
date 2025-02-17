function extractSpecialWords(input) {
    const words = input.split(' ');

    const specialWords = words.filter(word => {
        if (word.startsWith('#')) {
            const cleanWord = word.slice(1); 
            return /^[a-zA-Z]+$/.test(cleanWord); 
        }
    });

    specialWords.forEach(word => {
        console.log(word.slice(1));
    });
}
