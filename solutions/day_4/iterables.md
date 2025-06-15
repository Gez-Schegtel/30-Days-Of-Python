---
title: "Iterables en Python"
author: "Juannie & DeepSeek"
date: "09/03/2025"
geometry: margin=1in
colorlinks: true
header-includes:
	- \usepackage{fvextra}
	- \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
	- \usepackage{graphicx}
	- \setkeys{Gin}{width=0.75\textwidth}
	- \usepackage{float}
	- \floatplacement{figure}{H}
---

En Python, los **índices y slices** (rebanadas) permiten acceder a elementos individuales o subconjuntos de una lista, cadena o cualquier iterable. Aquí te explico todas las combinaciones posibles:

---

### **Sintaxis General**
```python
iterable[inicio : fin : paso]
```
- **`inicio`**: Índice donde comienza el slice (incluido).
- **`fin`**: Índice donde termina el slice (excluido).
- **`paso`**: Intervalo entre elementos (opcional, por defecto es `1`).

---

### **Combinaciones Comunes**
#### 1. **`[n]`**: Acceder al elemento en la posición `n`.
   ```python
   lista = [0, 1, 2, 3, 4, 5]
   print(lista[2])  # 2
   ```

#### 2. **`[inicio:]`**: Desde `inicio` hasta el final.
   ```python
   lista[2:]  # [2, 3, 4, 5]
   ```

#### 3. **`[:fin]`**: Desde el inicio hasta `fin` (sin incluir).
   ```python
   lista[:3]  # [0, 1, 2]
   ```

#### 4. **`[inicio:fin]`**: Desde `inicio` hasta `fin` (sin incluir).
   ```python
   lista[1:4]  # [1, 2, 3]
   ```

#### 5. **`[::paso]`**: Toda la lista con un paso.
   ```python
   lista[::2]   # [0, 2, 4] (cada 2 elementos)
   lista[::-1]  # [5, 4, 3, 2, 1, 0] (invierte la lista)
   ```

#### 6. **`[inicio:fin:paso]`**: Desde `inicio` hasta `fin` con un paso.
   ```python
   lista[1:5:2]  # [1, 3]
   ```

---

### **Índices Negativos**
Los índices negativos cuentan desde el final hacia el inicio:
- `-1`: Último elemento.
- `-2`: Penúltimo elemento, etc.

**Ejemplos**:
```python
lista = [0, 1, 2, 3, 4, 5]

print(lista[-1])    # 5 (último elemento)
print(lista[-3:])   # [3, 4, 5] (últimos 3 elementos)
print(lista[:-2])   # [0, 1, 2, 3] (excluye los últimos 2)
```

---

### **Casos Especiales**
#### 1. **Índices fuera de rango**:
   Python no lanza error, simplemente ajusta los límites.
   ```python
   lista[2:100]  # [2, 3, 4, 5]
   ```

#### 2. **`inicio > fin`**:
   Si el paso es positivo, devuelve una lista vacía.
   ```python
   lista[4:2]  # []
   ```

#### 3. **Paso negativo**:
   Recorre la lista en orden inverso.
   ```python
   lista[5:2:-1]  # [5, 4, 3]
   ```

---

### **Ejemplos Prácticos**
```python
texto = "Python"

# Últimos 3 caracteres
print(texto[-3:])  # 'hon'

# Cada segundo carácter
print(texto[::2])  # 'Pto'

# Invertir una cadena
print(texto[::-1])  # 'nohtyP'
```

---

### **Resumen de Combinaciones**
| Sintaxis         | Ejemplo (lista = [0,1,2,3,4,5]) | Resultado       |
|------------------|----------------------------------|-----------------|
| `[n]`            | `lista[2]`                       | `2`             |
| `[inicio:]`      | `lista[2:]`                      | `[2,3,4,5]`     |
| `[:fin]`         | `lista[:3]`                      | `[0,1,2]`       |
| `[inicio:fin]`   | `lista[1:4]`                     | `[1,2,3]`       |
| `[::paso]`       | `lista[::2]`                     | `[0,2,4]`       |
| `[inicio::paso]` | `lista[1::2]`                    | `[1,3,5]`       |
| `[inicio:fin:-1]`| `lista[5:2:-1]`                  | `[5,4,3]`       |
| `[::-1]`         | `lista[::-1]`                    | `[5,4,3,2,1,0]` |
