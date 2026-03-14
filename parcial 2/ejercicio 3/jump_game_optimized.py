from typing import List

def canJump(nums: List[int]) -> bool:
    """
    Solución optimizada: un solo recorrido manteniendo el alcance máximo.
    
    Tiempo: O(n)  -- un solo recorrido del array.
    Espacio: O(1) -- uso constante de memoria (solo variables auxiliares).
    
    Args:
        nums: lista de enteros donde nums[i] representa el salto máximo desde la posición i.
    
    Returns:
        True si se puede alcanzar el último índice, False en caso contrario.
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
