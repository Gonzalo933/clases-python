# Las tuplas en python son secuencias de objetos
# Es decir, secuencias de numeros, strings, booleans, etc...
# Se pueden mezclar varios tipos de elementos en ellas.
# Las tuplas no son modificables!!
# Estan representadas por parentesis

tupla_de_numeros = (1, 5, 8, 67, 65, 100, 600, 500)

tupla_de_datos = ("Pepe", 5, 5, 1993)

# Para acceder a elementos de las tuplas usamos corchetes indicando dentro la posición.
# Los elementos empiezan en la posicion 0
print(f"El elemento en la posicion 3 es el: {tupla_de_numeros[3]}")


# Tambien se puede accerder a las tuplas con indices negativos
# Esto nos indica que comenzamos a contar los indices desde atras
# -1 es el último elemento
print(f"El elemento en la penultima posicion (pos -2) es el: {tupla_de_numeros[-2]}")
# Otra forma de acceder a los datos de las tuplas es con los llamados "slices"
# Esto es util si queremos mas de un dato y la sintaxis es
# TUPLA[POS_INICIO:POS_FINAL:SALTOS]
# POS_INICIO se incluye
# POS_FINAL no se incluye
# Ejemplos
print(f"Elementos del 2 al 4: {tupla_de_numeros[2:4]}")
print(f"Todos los elementos desde el segundo: {tupla_de_numeros[2:]}")
print(f"Todos los elementos hasta el 5: {tupla_de_numeros[:5]}")
print(f"Todos los elementos hasta el penultimo: {tupla_de_numeros[:-1]}")
print(f"Todos los elementos saltando de dos en dos: {tupla_de_numeros[::2]}")
print(f"La tupla ordenada al reves: {tupla_de_numeros[::-1]}")

print(f"Numero de elementos {len(tupla_de_numeros)}")
print(f"Esta el numero 5 en la tupla? {5 in tupla_de_numeros}")
# Las tuplas no se pueden modificar pero se pueden hacer operaciones que crean nuevas
print(
    f"Añadir a la tupla los dos primeros numeros de si misma {tupla_de_numeros + tupla_de_numeros[:2]}"
)

print(f"Repetir (1,2) 10 veces {(1,2)*10}")
print(f"Maximo elemento de la tupla: {max(tupla_de_numeros)}")
import pdb

pdb.set_trace()

