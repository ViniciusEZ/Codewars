function isNice(arr){
    if (arr.length === 0)
        return false; 
   for (const n of arr) {
        if (arr.includes(n -1) || arr.includes(n + 1))
            continue;
        return false;
   }
   return true;
}

console.log(isNice([]));