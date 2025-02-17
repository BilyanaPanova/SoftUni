function wordsUppercase(sequence) {
    const words = sequence.match(/\b\w+\b/g);
    const upperCaseWords = words.map(word => word.toUpperCase());
    console.log(upperCaseWords.join(", "));

    }
