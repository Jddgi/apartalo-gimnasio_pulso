-- Ejercicio 8 · Consultas sobre la fotografía de tu tablero.
-- La tabla se la llama `tablero`. Para ver sus columnas, corre primero:
--     python metricas/cargar_tablero.py metricas/tablero.tsv
-- Termina cada consulta con punto y coma (;). Las líneas que empiezan con -- son comentarios.

-- a) Puntos comprometidos en el Sprint 1
SELECT SUM(puntos) AS puntos_comprometidos 
FROM tablero 
WHERE sprint = 'Sprint 1';

-- b) Puntos entregados (estado = 'Liberación')
SELECT SUM(puntos) AS puntos_entregados 
FROM tablero 
WHERE sprint = 'Sprint 1' AND estado = 'Liberación';

-- c) Porcentaje de cumplimiento (entregados ÷ comprometidos)
SELECT (CAST(SUM(CASE WHEN estado = 'Liberación' THEN puntos ELSE 0 END) AS REAL) / SUM(puntos)) * 100 AS porcentaje_cumplimiento 
FROM tablero 
WHERE sprint = 'Sprint 1';

-- d) Tiempo de ciclo promedio en días (de inicio a terminado) de las historias entregadas
--     Pista: julianday(terminado) - julianday(inicio)
SELECT AVG(julianday(terminado) - julianday(inicio)) AS tiempo_ciclo_promedio 
FROM tablero 
WHERE estado = 'Liberación' AND inicio IS NOT NULL AND terminado IS NOT NULL;

-- e) Subconjunto: historias con prioridad 'Must', con sus puntos y su estado
SELECT titulo, puntos, estado 
FROM tablero 
WHERE prioridad = 'Must';
