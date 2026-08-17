class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // create a set for nums
        const numsSet = new Set()
        //    looping through the numbers
        for (const number of nums) {

            if (numsSet.has(number)) return true

            numsSet.add(number)
        }
        return false

    }
}