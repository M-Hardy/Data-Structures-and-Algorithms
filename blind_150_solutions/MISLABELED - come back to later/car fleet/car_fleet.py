class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        fleets = 0
        prev_turns = 0
        ordered_cars = sorted([(p, s) for p, s in zip(position, speed)])
        
        for p,s in ordered_cars[::-1]:
            # in pre-python3, float casting  
            # required to return float
            # in division operation
            num_turns = (float(target)-p)/s
            if num_turns > prev_turns:
                fleets += 1
                prev_turns = num_turns
        
        return fleets