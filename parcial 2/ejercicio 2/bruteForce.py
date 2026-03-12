# Complejidad tiempo: O(2^n * n^2)
# Complejidad espacio: O(n)

def no_se_solapan(a, b):
    return a[1] <= b[0] or b[1] <= a[0]

def max_intervalos_brute(intervalos):
    n = len(intervalos)
    mejor = [0]

    def rec(i, elegidos):
        if i == n:
            for x in range(len(elegidos)):
                for y in range(x + 1, len(elegidos)):
                    if not no_se_solapan(elegidos[x], elegidos[y]):
                        return
            mejor[0] = max(mejor[0], len(elegidos))
            return
        rec(i + 1, elegidos)
        rec(i + 1, elegidos + [intervalos[i]])
    rec(0, [])
    return mejor[0]

def eraseOverlapIntervals(intervals):
    max_no_overlap = max_intervalos_brute(intervals)
    return len(intervals) - max_no_overlap

if __name__ == "__main__":
    intervals = [(1,2),(2,3),(3,4),(1,3)]
    resultado = eraseOverlapIntervals(intervals)
    print("Intervalos:", intervals)
    print("Mínimo a eliminar:", resultado)