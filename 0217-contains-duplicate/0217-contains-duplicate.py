class Solution(object):
    def containsDuplicate(self, nums):
        unique_nums = set(nums)
        
        if len(nums) != len(unique_nums):
            return True
        else:
            return False