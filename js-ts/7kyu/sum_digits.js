function sumDigits(number) {
    let sum = 0;
    for (const n of number.toString()) {
        if (n >= '0' && n <= '9')
            sum += parseInt(n);
    }
    return sum;
}

console.log(sumDigits(-32));
