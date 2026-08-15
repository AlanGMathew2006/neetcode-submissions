class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initialize a hash set
        numSet = set(nums)
        longest = 0

        # Iterate through numSet
        for num in numSet:
            #Check for the first # in the sequence by checking its left
            if (num - 1) not in numSet:
                length = 1
                # check the #'s after the first if they exist in a orderly sequence
                while (num + length) in numSet:
                    length += 1
                # Update longest using max
                longest = max(length, longest)
        return longest
