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
            if target - key in records and records[target - key] != records[key] :
                return list((records[key], records[target - key]))

        return solution
