class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        i = 0
        
        while i < len(intervals):
            j = i + 1
            
            while j < len(intervals):
                
                a = intervals[i]
                b = intervals[j]
                
                if a[1] >= b[0] and b[1] >= a[0]:
                    
                    nuevo_inicio = min(a[0], b[0])
                    nuevo_fin = max(a[1], b[1])
                    
                    intervals[i] = [nuevo_inicio, nuevo_fin]
                    intervals.pop(j)
                    
                    i = -1
                    break
                
                else:
                    j += 1
            
            i += 1
        
        return intervals