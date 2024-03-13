/**
 * @param {number[]} nums
 * @return {boolean}
 */

// for-loop instead of forEach() used because
// you can't return a value within a forEach()
// callback
const containsDuplicate = function (nums) {
  const found = new Set();

  for (const num of nums) {
    if (found.has(num)) return true;
    found.add(num);
  }
  return false;
};
