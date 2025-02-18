function countStringOccurrences (text, string) {
    const textArr = text.split(" ");
    const count = textArr.filter(item => item === string).length;
    console.log(count);
}
