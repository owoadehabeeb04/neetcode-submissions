class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArray = [0] * len(nums)
        print(outputArray)
        for i, num1 in enumerate(nums):
            product = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    product = product * num2
                    print(product)
            outputArray[i] = product
            # product = 1
            print(outputArray)
        return outputArray

