class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        first = {}
        second = {}

        for i in range(0,len(s)):
            first[s[i]] = first.get(s[i],0) + 1
            second[t[i]] = second.get(t[i],0) + 1
        
        return first == second