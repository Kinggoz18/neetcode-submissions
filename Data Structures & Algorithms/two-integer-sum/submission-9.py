class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = [0, 1]
        records = dict()
        # record each target - nums[i] in a dictionary as kets
        for i in range(len(nums)):
            if target - nums[i] not in records:
                records[target - nums[i]] = i
            elif target - nums[i] in records and (target - nums[i] + nums[i]) == target:
                return list((records[target - nums[i]], i))

        # find the first indexes that sum up to target
        for key in records:
            if target - key in records and records[target - key] != records[key]:
                return list((records[key], records[target - key]))

        return solution


# 2 edge cases:
# 1. Since dictionaries cannot store duplicated keys. Don't just skip it, check if it's equals to the target first. - elif on line 9. E.g: [5,5] or [5,0,5]
# 2. Since the indexes are stored as values and we're checking if the target - the key is in the record. We need to guard against checking its own key - handled after the 'and' on line 14. E.g: [1,3,4,2] 
