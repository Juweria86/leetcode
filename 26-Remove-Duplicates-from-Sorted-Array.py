lass Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[k] = nums[right]
                k += 1
        return k
