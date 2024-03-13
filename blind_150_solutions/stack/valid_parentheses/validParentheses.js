/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {

    let stack = [];
    const bracketsMap = new Map([
        [')', '('],
        [']', '['],
        ['}', '{']
    ]);
    
    for (const bracket of s) {
        if (!bracketsMap.has(bracket)) {
            stack.push(bracket);
        } else if (!stack.length || bracketsMap.get(bracket) != stack.pop()) {
            return false;
        }
    }

    return !stack.length ? true : false;
};