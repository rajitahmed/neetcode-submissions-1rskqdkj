class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_dict = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in i_dict:
                return [i_dict[j], i]
            i_dict[nums[i]] = i