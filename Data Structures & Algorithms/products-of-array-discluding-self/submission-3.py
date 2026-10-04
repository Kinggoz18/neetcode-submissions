class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        prefix = [0] * numsLen
        surfix = [0] * numsLen

        x = numsLen - 1
        i = 0
        currPrefix = 1
        currSurfix = 1
        while (i < numsLen) and (x > -1):
            if i == 0 and x == numsLen - 1:
                prefix[i] = currPrefix
                surfix[x] = currSurfix
            elif 1 == 1 and x == numsLen - 2:
                currPrefix = nums[i - 1]
                currSurfix = nums[x + 1]
            elif i >= 2 and x < numsLen - 2:
                currPrefix = currPrefix * nums[i - 1]
                currSurfix *= nums[x + 1]

            prefix[i] = currPrefix
            surfix[x] = currSurfix
            x -= 1
            i += 1

        result = [0] * numsLen
        x = numsLen - 1
        i = 0
        for i in range(numsLen):
            result[i] = prefix[i] * surfix[i]

        return result
