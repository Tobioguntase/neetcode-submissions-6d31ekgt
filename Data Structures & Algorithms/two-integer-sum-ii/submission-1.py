class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, end = 0, len(numbers) - 1

        while front < end:
            sum1 = numbers[front] + numbers[end]
            if target == sum1:
                return [front + 1, end + 1]
            elif sum1 < target:
                front += 1
            else:    
                end -= 1
    
        return []