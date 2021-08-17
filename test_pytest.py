import Tarea_micros as tm
import random
# ERR1 x2: Los test debian de pasar, sus test de caso negativo fallan
# ERR2 x2: Los test de caso positivo no prueba que el array resultado sea el
# correcto
# NOTA: 87.87
''' Este test revisa los métodos del código de Tarea_micros.py
Se espera que los métodos de nombre terminado
en _true pasen, y los terminados en _false fallen.
Las funciones retornan 0 cuando pasan y
otro número cuando fallan
'''


# Se prueba la función multiple_op con un número
# entero aleatorio entre 0 y 9
# Se espera que pase
def test_multiple_op_true():
    num = random.randrange(10)  # Numero entre 0 y 9
    assert tm.multiple_op(num)[0] == 0, 'Error: Se esperaba un entero'


# Se prueba la función multiple_op con un string
# Se espera que falle
def test_multiple_op_false():
    assert tm.multiple_op('a')[0] == 0, 'E001: Se esperaba un entero'


# Se prueba la función verify_array_op con un array de
# números aleatorios entre 0 y 9
# se espera que pase
def test_verify_array_op_true():
    lista = []
    for i in range(3):
        lista.append(random.randrange(10))
    assert tm.verify_array_op(lista)[0] == 0, 'Error: No es lista de enteros'


# Se prueba la función verify_array_op con un array
# mixto entre strings y números
# se espera que falle
def test_verify_array_op_false():
    lista = ['a', 'b', 1]
    assert tm.verify_array_op(lista)[0] == 0, 'Error: No es lista de enteros'
