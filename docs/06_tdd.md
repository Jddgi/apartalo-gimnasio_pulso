# 6. Pruebas de aceptación y TDD
> Ejercicio 6 · Tema 8 · 🎩 desarrollador

## 6.2 Mis ciclos de TDD

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) | Qué aprendí |
|---|---|---|---|---|
| 1 |ROJO: prueba de cancelacion con menos de 3 horas |VERDE: cancelacion cuenta clase tomada |REFACTOR: documentar regla de cancelacion |Aprendí a crear una prueba antes de implementar la funcionalidad y a mejorar el código sin cambiar su comportamiento. |
| 2 | | | | |
| 3 | | | | |

## 6.5 Suites
Se marcaron todas las pruebas con las suites correspondientes:

@pytest.mark.unitaria para las pruebas unitarias.
@pytest.mark.aceptacion para las pruebas de aceptación.
Las pruebas fueron organizadas siguiendo la configuración definida en pytest.ini.

## 6.6 Cobertura de caminos

- **Función:** procesar_cancelacion(horas_anticipacion, no_se_presento=False)
- **Caminos** (cada `return` y cada `raise`):1 raise ValueError cuando las horas son negativas, 2 return cuando el usuario no se presenta (multa de $50), 3 return cuando cancela con 3 horas o más de anticipación, 4 return cuando cancela con menos de 3 horas de anticipación.
- **Caminos que recorren mis pruebas:** 1 Cancelación con menos de 3 horas → prueba test_cancelacion_menos_de_3_horas(), 2 Cancelación con exactamente 3 horas → prueba test_cancelacion_con_3_horas(), 3 No presentación → prueba test_no_show(), 4 Horas negativas → prueba agregada para verificar ValueError.
- **Cobertura:** Caminos totales: 4
Caminos recorridos por las pruebas: 4
Cobertura = 4 / 4 × 100 = 100 %
- **Pruebas que agregué para completar:** Se agregó una prueba para verificar que la función lance ValueError cuando se recibe un número negativo de horas de anticipación, ya que inicialmente ese camino no estaba cubierto por las pruebas.

## 6.7 Regresión

- **Defecto** (encontrado o provocado): Se provocó un defecto modificando la condición de la función procesar_cancelacion() de: if horas_anticipacion >= 3: a if horas_anticipacion > 3:
Esto ocasionaba que una cancelación realizada exactamente con 3 horas de anticipación fuera tratada incorrectamente como una cancelación tardía.
- **Prueba que lo detecta:** @pytest.mark.unitaria
def test_cancelacion_con_3_horas():

    resultado = procesar_cancelacion(3)

    assert resultado["clase_devuelta"] is True
- **Qué pasaba y cómo lo corregí:** Al modificar el operador >= por >, la función dejó de considerar correctamente el valor límite de 3 horas. Como resultado, una cancelación realizada exactamente con 3 horas de anticipación ya no devolvía la clase al socio, incumpliendo la regla de negocio R2. La prueba unitaria detectó inmediatamente el error. Para corregirlo, se restauró la condición original:
