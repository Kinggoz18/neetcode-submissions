class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        solutions = set()
        p1 = 0
        p2 = 1
        p3 = len(sortedNums) - 1
        print(sortedNums)

        while p1 < len(sortedNums) and p2 < p3:
            if (sortedNums[p1] + sortedNums[p2] + sortedNums[p3]) == 0 and (
                p1 != p2 and p2 != p3 and p3 != p1
            ):
                sortedSolution = tuple(sorted([sortedNums[p1], sortedNums[p2], sortedNums[p3]]))
                if sortedSolution not in solutions:
                    solutions.add(sortedSolution)
                p2 += 1
                p3 -= 1
            elif (sortedNums[p1] + sortedNums[p2] + sortedNums[p3]) < 0:
                p2 += 1
            else:
                p3 -= 1

            if p2 >= p3:
                p1 += 1
                p2 = p1 + 1
                p3 = len(sortedNums) - 1
        return list(solutions)
