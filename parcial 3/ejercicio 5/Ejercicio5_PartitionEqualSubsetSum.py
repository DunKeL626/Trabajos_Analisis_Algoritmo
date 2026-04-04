# Estado DP: dp[j] representa si es posible obtener una suma exacta de j
# Recurrencia: dp[j] = dp[j] OR dp[j - num] (para cada num en nums)
# Complejidad: Tiempo O(n * target), Espacio O(target) donde target = sum(nums)/2

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # Si la suma total es impar, no se puede dividir en dos partes iguales
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # dp[j] = True si podemos obtener suma j
        dp = [False] * (target + 1)
        dp[0] = True  # suma 0 siempre es posible (subconjunto vacío)
        
        # Para cada número en el array
        for num in nums:
            # Recorrer en orden inverso para evitar usar el mismo elemento dos veces
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Ejemplo 1: [1, 5, 11, 5] -> suma = 22, target = 11
    # Subconjunto {1, 5, 5} = 11, {11} = 11
    print(sol.canPartition([1, 5, 11, 5]))  # Output: True
    
    # Ejemplo 2: [1, 2, 3, 5] -> suma = 11 (impar)
    print(sol.canPartition([1, 2, 3, 5]))  # Output: False
    
    # Ejemplo 3: [1, 2, 5] -> suma = 8, target = 4
    # No hay forma de obtener 4
    print(sol.canPartition([1, 2, 5]))  # Output: False
    
    # Ejemplo 4: [2, 2, 1, 1] -> suma = 6, target = 3
    # Subconjunto {2, 1} = 3, {2, 1} = 3
    print(sol.canPartition([2, 2, 1, 1]))  # Output: True
