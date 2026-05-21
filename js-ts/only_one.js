function onlyOne() {
    return [...arguments].filter(Boolean).length === 1;
}

console.log(onlyOne(true, false, false, true));     