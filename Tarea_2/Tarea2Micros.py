'''
Este programa tiene como función comparar la eficiencia en tiempo
de un proceso en un hilo vs varios hilos.
Recibe el argumento N.
Genera un array del tamaño N, con enteros desde cero hasta N-1.
Calcula el cuadrado de cada número y lo imprime.
Este último paso se hace dos veces, primero con un hilo
y seguidamente con varios hilos.
'''

import threading
import time
import argparse
import itertools


# funcion que genera y retorna el array
def defArrayO(arraysize):
    ArrayO = [None]*arraysize
    for i in range(0, arraysize):
        ArrayO[i] = i
    return ArrayO


# recibe un array y el tipo de impresion de texto
def SingleThread(array):
    global ArrayResultadoSingle
    for i in range(0, len(array)):
        ArrayResultadoSingle.append(array[i]**2)


def MultiThread(array, z):
    # arrays es un array generado por defArray
    # z es el numero de Hilo. Para hacer la division correspondiente
    global ArrayResultadoMulti
    xcountHilo = round(len(array)/4)
    # El último hilo no se redondea
    if z == 4:
        upperLimit = len(array)
    else:
        upperLimit = xcountHilo*z
    for i in range(xcountHilo*(z-1), upperLimit):
        # ArrayResultadoMulti[i] = array[i]**2
        ArrayResultadoMulti.append(array[i]**2)


# __main__
parser = argparse.ArgumentParser()
# -f para guardar el output en un archivo.
parser.add_argument("-f", "--file",
                    help="Guarda la salida en un file. \
                    (Default: Escribir en consola)",
                    action="store_true")
parser.add_argument("-v", "--verbose",
                    help="Escribe todos los datos calculados",
                    action="store_true")
# argumento array para definir el tamaño del array
parser.add_argument("array_size", type=int, help="Tamaño del array")
args = parser.parse_args()
print_to_file = args.file
verbose = args.verbose

ArrayResultadoSingle = []
ArrayResultadoMulti = []

array_single = defArrayO(args.array_size)
xparamulti = array_single
# Initialize single thread
tiempo_ini = time.time()
t1 = threading.Thread(name="hilo_1", target=SingleThread,
                      args=(array_single, ))  # single thread
t1.start()
t1.join()
# End time for single thread
tiempo_fin = time.time()
tiempo_single = tiempo_fin - tiempo_ini

# Initialize multi thread
tiempo_ini = time.time()
t2 = threading.Thread(name="hilo_2", target=MultiThread,
                      args=(xparamulti, 1))  # Hilo 1
t3 = threading.Thread(name="hilo_3", target=MultiThread,
                      args=(xparamulti, 2))  # Hilo 2
t4 = threading.Thread(name="hilo_4", target=MultiThread,
                      args=(xparamulti, 3))  # Hilo 3
t5 = threading.Thread(name="hilo_5", target=MultiThread,
                      args=(xparamulti, 4))  # Hilo 4
t2.start()
t3.start()
t4.start()
t5.start()
# End time for multi thread
tiempo_fin = time.time()
tiempo_multi = tiempo_fin - tiempo_ini


if print_to_file:
    with open("output.txt", "w") as output_file:
        output_file.write("Tiempos:\n")
        output_file.write("Multi Array: " + str(tiempo_multi) + "\t\t"
                          + "Single Array:  " + str(tiempo_single) + "\n")
        if verbose:
            for multi, sing in itertools.zip_longest(ArrayResultadoMulti,
                                                     ArrayResultadoSingle):
                output_file.write(str(multi) + "\t\t\t\t\t\t"
                                  + str(sing) + "\n")
else:
    print("Tiempos:")
    print("Multi-thread: " + str(tiempo_multi) + "\t\t"
          + "Single-thread:  " + str(tiempo_single))
    if verbose:
        for multi, sing in itertools.zip_longest(ArrayResultadoMulti,
                                                 ArrayResultadoSingle):
            print(str(multi) + "\t\t\t\t\t\t" + str(sing))
