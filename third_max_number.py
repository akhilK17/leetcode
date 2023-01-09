class Solution:
    def thirdmaxno(self, nums:list[nums]) -> int:
        third_max = min(nums)
        first_max = max(nums)
        second_max = third_max

        for i in range(len(nums)):
            if nums[i] > second_max and nums[i] < first_max:
                third_max = second_max
                second_max = nums[i]
            if nums[i] > third_max and nums[i] < second_max:
                third_max = nums[i]
                
        if second_max != third_max:
            return third_max
        else:
            return first_max

