class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            required = target - num

            if required in seen:
                return [seen[required],i]
            
            seen[num] = i