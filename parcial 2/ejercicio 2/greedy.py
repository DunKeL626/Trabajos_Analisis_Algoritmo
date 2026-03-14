# Complejidad tiempo: O(n log n)
# Complejidad espacio: O(1)
#El algoritmo es greedy porque en cada paso elige el intervalo que termina más temprano, lo cual es una decisión local óptima que 
# conduce a una solución global óptima sin necesidad de explorar todas las combinaciones posibles.
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        j = 0
        count = 0
        for i in range(1, len(intervals)):
            inicio = intervals[i][0] #empiezo desde el segundo intervalo
            final = intervals[j][1] #final del primer intervalo
            if final <= inicio:
                j=i
            else:
                count+=1
        return count

print(eraseOverlapIntervals([(1,2),(2,3),(3,4),(1,3)])) #poner aca el TEST CASE