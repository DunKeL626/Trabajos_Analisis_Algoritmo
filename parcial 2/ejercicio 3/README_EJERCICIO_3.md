# Jump Game (LeetCode)

Problema tomado de LeetCode.

---

## Enunciado

Dado un arreglo de enteros `nums`, estás inicialmente posicionado en el **primer índice** del arreglo. Cada elemento en el arreglo representa tu **longitud máxima de salto** en esa posición.

Devolver `true` si puedes alcanzar el último índice, o `false` en caso contrario.

---

## Ejemplo(s)

**Ejemplo 1**

Entrada:

```
nums = [2, 3, 1, 1, 4]
```

Salida:

```
true
```

Explicación: Salta 1 paso desde el índice 0 al 1, luego 3 pasos al último índice.

**Ejemplo 2**

Entrada:

```
nums = [3, 2, 1, 0, 4]
```

Salida:

```
false
```

Explicación: Siempre llegarás al índice 3 sin importar qué. Su longitud máxima de salto es 0, lo que hace imposible alcanzar el último índice.

---

## Restricciones

* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 10^5`

---

## Solución: Optimizada (Greedy - un recorrido)

### Idea

Recorrer el arreglo una sola vez manteniendo el **alcance máximo** que podemos lograr:

* Mantener una variable `reach` que representa la posición más lejana alcanzable.
* En cada posición `i`, verificar si podemos llegar a ella (`i <= reach`).
* Actualizar `reach` con el máximo entre el alcance actual y `i + nums[i]`.
* Si en algún momento `reach >= última posición`, retornar `true`.
* Si encontramos una posición `i` que no podemos alcanzar (`i > reach`), retornar `false`.

### Implementación

```python
from typing import List

def canJump(nums: List[int]) -> bool:
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
```

### Complejidad

* **Tiempo:** O(n) → un solo recorrido del arreglo.
* **Espacio:** O(1) → memoria constante (solo variables auxiliares).

### Cuándo usarla

✔ Solución óptima para entradas grandes.
✔ Estándar en entrevistas y programación competitiva.
✔ Enfoque greedy eficiente.

---

## Análisis y patrones utilizados

Este ejercicio utiliza el patrón:

### 🔹 **Greedy - Alcance máximo**

Mantener el alcance máximo posible en cada paso, tomando decisiones localmente óptimas que llevan a la solución global.

Este patrón aparece frecuentemente en:

* problemas de saltos y alcance
* optimización de rutas
* problemas de cobertura
* scheduling y asignación de recursos

---

## Estrategia Greedy

La clave del algoritmo greedy es:

1. **Decisión local:** En cada posición, calcular el alcance máximo posible desde ahí.
2. **Optimización global:** Si en algún momento el alcance cubre el final, ya tenemos la respuesta.
3. **Detección temprana:** Si encontramos una posición inalcanzable, retornamos inmediatamente.

**¿Por qué funciona?**

No necesitamos conocer el camino exacto, solo si es **posible** llegar. Si en algún momento nuestro alcance máximo cubre el último índice, sabemos que existe al menos un camino válido.

---

## Casos de prueba

```python
canJump([2, 3, 1, 1, 4])  # True - alcanzable
canJump([3, 2, 1, 0, 4])  # False - bloqueado en índice 3
canJump([0])              # True - ya estamos en el final
canJump([2, 0, 0])        # True - salto inicial suficiente
canJump([1, 1, 1, 1])     # True - todos alcanzables
canJump([0, 2, 3])        # False - bloqueado en inicio
```
