function findUniq(arr) {
    const counts = {}

    for (const num of arr) {
        counts[num] = counts[num] ? counts[num] + 1 : 1;
    }
    return Number(Object.keys(counts).find(key => counts[key] === 1));
}

console.log(findUniq([ 0, 0, 0.55, 0, 0 ]));
