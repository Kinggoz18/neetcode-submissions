class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False

        records = dict()
        for x in range(len(nums)):
            if records.get(nums[x]):
                return True
            else:
                records[nums[x]] = x+1

        return False
