class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        
        resultado = []
        
        for intervalo in intervals:
            
            if len(resultado) == 0:
                resultado.append(intervalo)
            
            else:
                ultimo = resultado[-1]
                
                if intervalo[0] <= ultimo[1]:
                    
                    if intervalo[1] > ultimo[1]:
                        ultimo[1] = intervalo[1]
                
                else:
                    resultado.append(intervalo)
        
        return resultado