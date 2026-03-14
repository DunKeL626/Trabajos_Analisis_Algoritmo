# Parcial 2 - Análisis de Algoritmos

## 1. Assign Cookies (Greedy)

**Complejidad en tiempo:** O(n log n + m log m)  
**Complejidad en espacio:** O(1)

El algoritmo es greedy porque en cada paso asigna la galleta más pequeña que pueda satisfacer al niño menos exigente disponible.  
Esta decisión local evita desperdiciar galletas grandes y permite maximizar el número total de niños satisfechos.

```python
#Complejidad en tiempo: O(n log n + m log m)
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


print(findContentChildren([1,2], [1,2,3]))  # TEST CASE
# [g = [1,2,3], s = [1,1]] TEST CASE 1
# [g = [1,2], s = [1,2,3]] TEST CASE 2
```

---

## 2. Non-overlapping Intervals (Greedy)

**Complejidad en tiempo:** O(n log n)  
**Complejidad en espacio:** O(1)

El algoritmo es greedy porque en cada paso elige el intervalo que termina más temprano, lo cual es una decisión local óptima que conduce a una solución global óptima sin necesidad de explorar todas las combinaciones posibles.

```python
# Complejidad tiempo: O(n log n)
# Complejidad espacio: O(1)

def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        j = 0
        count = 0

        for i in range(1, len(intervals)):
            inicio = intervals[i][0] # empiezo desde el segundo intervalo
            final = intervals[j][1]  # final del primer intervalo

            if final <= inicio:
                j = i
            else:
                count += 1

        return count


print(eraseOverlapIntervals([(1,2),(2,3),(3,4),(1,3)]))  # TEST CASE
```

---

## 3. Jump Game

**Complejidad en tiempo:** O(n)  
**Complejidad en espacio:** O(1)

El algoritmo utiliza una estrategia greedy manteniendo el **máximo alcance posible** mientras se recorre el arreglo.  
En cada posición se verifica si aún es alcanzable y se actualiza la distancia máxima que se puede llegar.  
Si en algún punto el índice actual supera el alcance máximo, significa que no se puede continuar.

```python
from typing import List

def canJump(nums: List[int]) -> bool:
    """
    Solución optimizada: un solo recorrido manteniendo el alcance máximo.
    
    Tiempo: O(n)  -- un solo recorrido del array.
    Espacio: O(1) -- uso constante de memoria (solo variables auxiliares).
    """

    n = len(nums)
    if n <= 1:
        return True

    reach = 0  # máxima posición alcanzable
    last_index = n - 1

    for i, jump in enumerate(nums):
        if i > reach:  # no podemos llegar a la posición i
            return False

        reach = max(reach, i + jump)

        if reach >= last_index:  # ya podemos llegar al final
            return True

    return False


if __name__ == "__main__":

    assert canJump([2, 3, 1, 1, 4]) == True, "Ejemplo 1 falló"
    assert canJump([3, 2, 1, 0, 4]) == False, "Ejemplo 2 falló"
    assert canJump([0]) == True, "Un solo elemento -> True"
    assert canJump([2, 0, 0]) == True, "Alcanzable con salto inicial"
    assert canJump([1, 1, 1, 1]) == True, "Todos alcanzables"
    assert canJump([0, 2, 3]) == False, "Bloqueado en inicio"

    print("All optimized tests passed.")
```

---

## 4. Best Time to Buy and Sell Stock II

**Complejidad en tiempo:** O(n)  
**Complejidad en espacio:** O(1)

El algoritmo recorre el arreglo una sola vez y suma todas las diferencias positivas entre días consecutivos para maximizar la ganancia total.

```python
# Complejidad tiempo: O(n)
# Complejidad espacio: O(1)

class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
```

---

## 5. Merge Intervals

Este algoritmo combina intervalos que se superponen para producir un conjunto final de intervalos no solapados.

```python
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
```

---
