#Complejidad en tiempo: O(n log n + m log m + n·m)
#Complejidad en espacio: O(n + m)
def findContentChildren(g: list[int], s: list[int]) -> int:
        greed_ord = sorted(g, reverse=True)
        size_ord = sorted(s)
        usado = [False] * len(size_ord)
        count = 0
        for g in greed_ord:
            for j in range(len(size_ord)):
                if not usado[j] and size_ord[j] >= g:
                    usado[j] = True
                    count += 1
                    break
        return count

print(findContentChildren([1,2], [1,2,3] )) #poner aca el TEST CASE
    #[g = [1,2,3], s = [1,1] TEST CASE 1
    #[1,2], s = [1,2,3] TEST CASE 2