/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function(nums, target) {
    
    differences = new Map();

    for (let i=0; i < nums.length; i++) {
        if (differences.has(target-nums[i])) return [i, differences.get(target-nums[i])];
        differences.set(nums[i], i)
    }
    return null;
};