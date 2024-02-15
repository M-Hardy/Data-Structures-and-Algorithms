class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for pile in piles:
                hours_for_pile = (pile // k) + (0 if pile % k == 0 else 1)
                hours += hours_for_pile
                if hours > h:
                    l = k + 1
                    break

            if hours <= h:
                r = k -1
                min_k = k

        return min_k