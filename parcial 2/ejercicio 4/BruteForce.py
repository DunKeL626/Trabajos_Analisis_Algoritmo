# Complejidad tiempo: O(n)
# Complejidad espacio: O(n)
class Solution:
    def maxProfit(self, prices):
        memo = {}
        return self.dfs(prices, 0, False, memo)

    def dfs(self, prices, i, holding, memo):
        if i == len(prices):
            return 0

        if (i, holding) in memo:
            return memo[(i, holding)]

        # opción 1: no hacer nada
        res = self.dfs(prices, i + 1, holding, memo)

        if holding:
            # vender
            res = max(res, prices[i] + self.dfs(prices, i + 1, False, memo))
        else:
            # comprar
            res = max(res, -prices[i] + self.dfs(prices, i + 1, True, memo))

        memo[(i, holding)] = res
        return res
