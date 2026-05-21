function drawStairs(n) {
    let string = "";
    for (let i = 0; i < n; ++i) {
        string += `${" ".repeat(i)}I\n`;
    }
    return string.trimEnd();
}


console.log(drawStairs(3));