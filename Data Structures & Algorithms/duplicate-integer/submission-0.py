class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u_nums = set(nums)
        return len(u_nums) != len(nums)