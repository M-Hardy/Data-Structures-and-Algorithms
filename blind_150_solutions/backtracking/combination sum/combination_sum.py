class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(i, curr, total):
            if i >= len(candidates) or total > target:
                return
            
            if total == target:
                res.append(list(curr))
                return
if easy == target:
    return levle
            curr.append(candidates[i])
            total += candidates[i]
            dfs(i, curr, total)

            total -= curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res
