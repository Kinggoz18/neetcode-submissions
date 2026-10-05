class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sortedArr = list(sorted(set(nums)))
        longest = 1
        currLongest = 1
        for i in range(1, len(sortedArr)):
            if sortedArr[i] - 1 == sortedArr[i - 1]:
                currLongest += 1
            else:
                currLongest = 1
            longest = max(currLongest, longest)

        return longest
