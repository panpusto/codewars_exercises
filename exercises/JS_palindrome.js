const checkPalindrome = (text) => {
    return text.split('').reverse().join('') === text;
}

console.log(checkPalindrome('owocowo'));
console.log(checkPalindrome('marek'));

// toLowerCase()