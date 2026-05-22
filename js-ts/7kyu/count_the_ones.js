function hammingWeight(x){
    let count = 0;

    while (x) {
        x &= (x -1);
        count += 1;
    }
    return count;
}


const num = 54;
console.log(num.toString(2));

console.log(hammingWeight(num));