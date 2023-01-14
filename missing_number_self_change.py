def findMissing (self, nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        # treat the value of nums as index:
        new_index = abs(nums[i]) - 1

        if nums[new_index] > 0:
            nums[new_index] *= -1
    
    result = []

    for j in range(len(nums)):
        if nums[j] > 0:
            result.append(j+1)

    return result