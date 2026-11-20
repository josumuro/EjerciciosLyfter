# Investigación: SELECT con ORDER BY, LIMIT, GROUP BY y JOINs

Fuentes consultadas:
- Documentación oficial de PostgreSQL, página SELECT: https://www.postgresql.org/docs/current/sql-select.html


## Tabla 1. Cláusulas del SELECT

| Cláusula | Para qué sirve | Sintaxis | Hallazgos importantes |
|----------|----------------|----------|-----------------------|
| ORDER BY | Ordena las filas del resultado | `ORDER BY col [ASC \| DESC]` | ASC es el valor por defecto. Admite varias columnas separadas por coma. Sin ORDER BY el orden no está garantizado |
| LIMIT | Restringe cuántas filas se devuelven | `LIMIT n [OFFSET m]` | OFFSET salta m filas (paginación). Debe usarse con ORDER BY para obtener resultados reproducibles. SQL Server usa `TOP n` u `OFFSET ... FETCH` |
| GROUP BY | Agrupa filas con el mismo valor para calcular agregados | `GROUP BY col` con `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` | Toda columna del SELECT que no sea agregada debe aparecer en el GROUP BY. Los NULL forman un solo grupo. `HAVING` filtra grupos; `WHERE` filtra filas antes de agrupar |

## Tabla 2. Tipos de JOIN

| JOIN | Qué devuelve | Filas sin coincidencia | Equivalente en conjuntos |
|------|--------------|------------------------|--------------------------|
| INNER JOIN | Solo las filas que coinciden en ambas tablas | Se descartan | A ∩ B |
| LEFT JOIN | Todas las filas de la tabla izquierda más las coincidencias de la derecha | Las columnas de la derecha quedan en NULL | A (con datos de B si existen) |
| RIGHT JOIN | Todas las filas de la tabla derecha más las coincidencias de la izquierda | Las columnas de la izquierda quedan en NULL | B (con datos de A si existen) |

Otros tipos que lista la documentación: `FULL OUTER JOIN` (todas las filas de ambos lados) y `CROSS JOIN` (producto cartesiano).

## Tabla 3. Orden lógico de ejecución

| Paso | Cláusula | Función |
|------|----------|---------|
| 1 | FROM / JOIN | Selecciona y combina tablas |
| 2 | WHERE | Filtra filas |
| 3 | GROUP BY | Agrupa |
| 4 | HAVING | Filtra grupos |
| 5 | SELECT | Calcula las columnas de salida |
| 6 | ORDER BY | Ordena |
| 7 | LIMIT / OFFSET | Recorta |

## Ejemplo 

```sql
SELECT a.name, COUNT(b.id) AS libros
FROM authors a
LEFT JOIN books b ON b.author_id = a.id
GROUP BY a.id, a.name
ORDER BY libros DESC, a.name
LIMIT 3;
```
