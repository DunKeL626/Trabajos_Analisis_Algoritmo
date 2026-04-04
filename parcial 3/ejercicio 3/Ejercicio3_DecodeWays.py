# Versión optimizada en espacio: solo necesitamos los últimos 2 valores
# Complejidad: Tiempo O(n), Espacio O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        
        # Variables para dp[i-2] y dp[i-1]
        prev2 = 1  # dp[0]
        prev1 = 1  # dp[1]
        
        for i in range(2, n + 1):
            current = 0
            
            # Tomar 1 dígito
            one_digit = int(s[i-1])
            if 1 <= one_digit <= 9:
                current += prev1
            
            # Tomar 2 dígitos
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                current += prev2
            
            # Actualizar para siguiente iteración
            prev2 = prev1
            prev1 = current
        
        return prev1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.numDecodings("12"))      # Output: 2
    print(sol.numDecodings("226"))     # Output: 3
    print(sol.numDecodings("06"))      # Output: 0
    print(sol.numDecodings("11106"))   # Output: 2
