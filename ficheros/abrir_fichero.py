# Para abrir un fichero usamos la función open.
# El primer argumento es el nombre del fichero, y el segundo el modo.
# Debemos acordarnos de cerrarlo despues de usarlo o de usar un "context manager"
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists


def lee_y_muestra():
    # Abrimos fichero en modo lectura
    f = open("numeros.txt", "r")
    for linea in f:
        print(linea)
    f.close()
