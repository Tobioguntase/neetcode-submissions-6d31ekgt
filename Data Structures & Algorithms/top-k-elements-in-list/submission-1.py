class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for i in nums:
            if i in numCount:
                numCount[i] += 1
            else:
                numCount[i] = 1 

        sortedNumCount = {k: v for k, v in sorted(numCount.items(), key=lambda item: item[1])}
        return list(sortedNumCount.keys())[-k:]
        