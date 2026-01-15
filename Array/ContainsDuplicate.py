class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(set(nums)) != len(nums)

        # since set(nums) will remove all the duplicate values and if there was
        # a duplicate the len will be less than the original and it will return 
        # true else false other way u can do it is:

        # check = set()
        # for i in nums:
        #     check.add(i) 
        
        # if len(check) == len(nums):
        #     return False

        # return True
