function countConsonants(str) {
    const setStr = new Set(str.toLowerCase());
    let count = 0;
    for (const l of setStr) {
        if (!"aeiou".includes(l) && l >= 'a' && l <= 'z')
            count += 1;
    }
    return count;
}

console.log(countConsonants("aeiou"));