function censored(text,word) {
    const stars = "*".repeat(word.length)

    let newText = text.replaceAll(word,stars)

    console.log(newText)
}
