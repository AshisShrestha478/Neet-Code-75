class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums) # This will handle the duplicate numbers
        longest = 0 # This will keep record of longest recored value

        for i in numsSet:
            if (i-1) not in numsSet:
                current = 0 # This will keep reocrd of our sequence length
                while (i+current) in numsSet:
                    current += 1
                longest = max (longest, current) # This will keep our longest recorded seq in longest
        return longest
