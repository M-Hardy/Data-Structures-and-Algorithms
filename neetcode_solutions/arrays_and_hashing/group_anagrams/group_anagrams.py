class Solution(object):
    
    # Time complexity is O(m*n*26), where
    # m is number of input strings, n is 
    # average length of input strings, and 
    # 26 is length of count sort array for
    # string chars
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagram_map = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                bucket = ord(c) - ord('a')
                counts[bucket] += 1
        
            # python keys cannot be lists (dict 
            # keys must be immutable)
            counts = tuple(counts) 
            if counts in anagram_map:
                anagram_map[counts].append(s)
            else:
                anagram_map[counts] = [s]
            
        return anagram_map.values()
    
    
    # Time complexity is O(m*nlogn), where m 
    # is number of input strings and n is the 
    # average length of the input strings
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagram_map = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]
            
        return anagram_map.values()