class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        
        return s_map == t_map

    def isAnagram2(self, s, t):
        return ''.join(sorted(s)) == ''.join(sorted(t))