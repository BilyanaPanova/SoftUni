function revealWords(words, sequence) {
    words = words.split(", ")
    words.forEach(word => {
        const stars = '*'.repeat(word.length);
        sequence = sequence.replace(stars, word);
    });

    console.log(sequence);
}
