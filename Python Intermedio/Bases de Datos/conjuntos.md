
```
All  = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Even = {2, 4, 6, 8, 10}
Odd  = {1, 3, 5, 7, 9}
```



## Operaciones

| # | Operación | Procedimiento | Resultado |
|---|-----------|---------------|-----------|
| 1 | Even ∪ Odd | Todos los elementos de ambos conjuntos, sin repetir | {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} |
| 2 | Even ∩ Odd | Elementos presentes en ambos. No comparten ninguno | ∅ (conjunto vacío) |
| 3 | All − Odd | Elementos de All que no están en Odd | {2, 4, 6, 8, 10} |
| 4 | C(Even) | All − Even | {1, 3, 5, 7, 9} |
| 5 | C(Odd − All) | Primero Odd − All = ∅ (todo impar está en All). Luego C(∅) = All − ∅ | {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} |

