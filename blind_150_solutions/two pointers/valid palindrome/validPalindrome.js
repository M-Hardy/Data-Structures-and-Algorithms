/**
 * @param {string} s
 * @return {boolean}
 */


const isPalindrome = function(s) {

    let l = 0;
    let r = s.length - 1;

    while (l < r) {
        while (l < r && !s[l].toLowerCase().match(/^[0-9a-z]$/)) {
            ++l;
        }

        while (r > l && !s[r].toLowerCase().match(/^[0-9a-z]$/)) {
            --r;
        }

        if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;

        ++l;
        --r;
    }
    return true;
};