/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */


// compare sorted strings, O(nlogn) time complexity; 
// simpler solution to implement than map comparison 
// because map comparison has to be implemented 
// yourself 
const isAnagram = function(s, t) {
    const sortedS = s.split('').sort().join('');
    const sortedT = t.split('').sort().join('');
    return sortedS === sortedT;
}



// string map comparison solution, O(n) time complexity
const isAnagram2 = function(s, t) {

    if (s.length !== t.length) return false

    sMap = new Map();
    tMap = new Map();

    for (let i = 0; i < s.length; i++) {
        sMap.set(s[i], (sMap.get(s[i]) ?? 0) + 1);
        tMap.set(t[i], (tMap.get(t[i]) ?? 0) + 1);
    }

    // have to implement map comparison myself because 
    // there is no built-in map comparison in js
    for (const [sChar, sCount] of sMap) {
        let tCount = tMap.get(sChar);
        if (tCount !== sCount || tCount === undefined && !tMap.has(sChar)) {
            return false;
        }
    }
    return true;    
};