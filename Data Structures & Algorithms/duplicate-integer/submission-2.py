class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        has_duplicates = len(nums) != len(unique_nums)
        if has_duplicates:
            return True
        return False