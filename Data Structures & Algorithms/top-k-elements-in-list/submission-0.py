class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyRec = defaultdict(int)
        # Count the frequency of each number
        for num in nums:
            frequencyRec[num] += 1

        result = list(
            dict(sorted(frequencyRec.items(), key=lambda item: item[1], reverse=True)).keys()
        )

        return result[0:k]
