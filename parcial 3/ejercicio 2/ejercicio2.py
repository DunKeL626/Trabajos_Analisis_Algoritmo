class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        canBreak = [False] * (n + 1)
        
        canBreak[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if canBreak[j] and s[j:i] in wordDict:
                    canBreak[i] = True
                    break
                    
        return canBreak[n]