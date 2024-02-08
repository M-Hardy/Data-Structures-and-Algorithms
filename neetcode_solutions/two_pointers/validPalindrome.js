/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

    s = s.toLowerCase();
    let start = 0;
    let end = s.length - 1;

    while (start < end) {
        while (!s[start].match(/^[0-9a-z]$/)) {
            ++start;
            if (start >= end) return true;
        }

        while (!s[end].match(/^[0-9a-z]$/)) {
            --end;
            if (end <= start) return true;
        }

        if (s[start] !== s[end]) return false;

        ++start;
        --end;
    }
    return true;
};