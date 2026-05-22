function pairs(ar){
    let count = 0;
    for (let i = 0; i < ar.length;) {
        if (ar[i] + 1 === ar[i+1] || ar[i] - 1 === ar[i+1])
            count += 1;
        i += 2;
    }
    return count;
};


console.log(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]))