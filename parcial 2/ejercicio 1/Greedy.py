#Complejidad en tiempo: O(n log n + m log m
#Complejidad en espacio: O(1)
#El algoritmo es greedy porque en cada paso asigna la galleta más pequeña que pueda satisfacer al niño menos exigente disponible. 
#Esta decisión local evita desperdiciar galletas grandes y permite maximizar el número total de niños satisfechos.
def findContentChildren(g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        n = len(g)
        m = len(s)
        while i < n and j < m:
            if s[j] >= g[i]:
                count += 1 
                i += 1
                j += 1
            else:
                j += 1
        return count

print(findContentChildren([1,2], [1,2,3] )) #poner aca el TEST CASE
    #[g = [1,2,3], s = [1,1] TEST CASE 1
    #[1,2], s = [1,2,3] TEST CASE 2