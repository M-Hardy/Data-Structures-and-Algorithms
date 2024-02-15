class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        i_stack = []

        for i in range(len(temperatures)):
            if i > 0:
                temperature = temperatures[i]
                while i_stack and temperature > temperatures[i_stack[-1]]:
                    day = i_stack.pop()
                    num_days = i - day
                    res[day] = num_days

            i_stack.append(i)

        return res