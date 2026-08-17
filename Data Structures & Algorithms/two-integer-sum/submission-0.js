class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // loop through the nums 
        const mapNumbers = new Map()
        for (let i = 0; i < nums.length; i++) {

           const number = nums[i]
           const theComplement = target - number
           const tehTargetIndex = mapNumbers.get(theComplement)
           const theTragetTrue = mapNumbers.has(theComplement)
           if (theTragetTrue) {
            return [i, tehTargetIndex]
           }
            mapNumbers.set(number, i)
        }
        return [-1, -1]
    }
}
