class Solution:
    def missing_number(self, nums:list[int]) -> list[int]:
        num_hashTable = {}
        result = []

        for num in nums:
            num_hashTable[num] = 1
        
        for num in range(1, len(nums)+1):
            if num not in num_hashTable:
                result.append(num)
        
        return result
