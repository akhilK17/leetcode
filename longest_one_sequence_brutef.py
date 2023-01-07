class Solution:
    def longestSequeneofOne(self, nums:list[int]) -> int:
        longest_sequence = 0
        for left in range(len(nums)):
            nums_zeros = 0
            for right in range(left, len(nums)):
                if nums_zeros == 2:
                    break
                if nums_zeros == 0:
                    nums_zeros += 1
                if nums_zeros <= 1:
                    longest_sequence = max(longest_sequence, right - left + 1)
        
        return longest_sequence
        