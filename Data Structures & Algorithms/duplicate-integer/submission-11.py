class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        records = dict()
        for x in range(len(nums)):
            if nums[x] not in records:
                records[nums[x]] = x + 1
            else:
                return True

        return False
