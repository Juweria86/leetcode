from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}  # Initialize an empty dictionary to store numbers and their indices

        for i, n in enumerate(nums):  # Iterate through the list with index and number
            difference = target - n  # Calculate the difference needed to reach the target
            if difference in prev:  # Check if this difference was seen before
                return [prev[difference], i]  # If yes, return the indices
            prev[n] = i  # Otherwise, store the current number and its index in the dictionary
        return  # If no solution is found (though problem guarantees there is one)

