class Solution(object):
    
    # Time complexity is O(n) - getting 
    # counts, assigning counts to count 
    # buckets,and iterating over count 
    # buckets are all linear operations
    # Space complexity is also O(n) for 
    # counts hashmap and buckets list
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counts = {}
        # end at len(nums) + 1 because max count 
        # is len(nums)
        count_buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num,count in counts.items():
            count_buckets[count].append(num)
        
        res = []
        # start at len(nums) because that is max 
        # count
        for i in range(len(nums),-1,-1):
            bucket = count_buckets[i]
            if bucket:
                for num in bucket:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res
