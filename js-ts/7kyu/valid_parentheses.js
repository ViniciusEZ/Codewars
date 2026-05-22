function validParentheses(parenStr) {
    let count = 0;
    for (const paren of parenStr) {
        if (paren === "(")
            count += 1;
        else {
            if (count === 0 && paren === ")")
                return false;
            count -= 1;
        }
            
    }
    return count === 0;
}

console.log(validParentheses("(()))"));