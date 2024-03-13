class TimeMap(object):

    def __init__(self):
        self.store = {} #key : [(timestamp, value), ...]
                

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

        
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        if (not key in self.store) or (self.store[key][0][0] > timestamp):
            return ""

        l = 0
        r = len(self.store[key]) - 1
        values = self.store[key]
        
        while l <= r:
            r_ts, r_val = values[r]
            if r_ts <= timestamp:
                return r_val

            m = (l + r) // 2
            m_ts, m_val = values[m]
            if m_ts == timestamp:
                return m_val
        
            if m_ts > timestamp:
                r = m - 1
            
            if m_ts < timestamp:
                if l + 1 == r:
                    return values[l][1]
                l = m   
                       
        return ""
    
    def get2(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        res = ""
        values = self.store.get(key, [])
        l = 0
        r = len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            
            if values[m][0] > timestamp:
                r = m - 1
            
            if values[m][0] < timestamp:
                res = values[m][1]
                l = m + 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)