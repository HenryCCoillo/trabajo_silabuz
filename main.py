from os import path


class Libro:
    def __init__(self,id = None ,titulo= None,genero= None,isbn= None,editorial= None,autor= None,leer_libro= None) -> None:
    # def __init__(self,leer_libro) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autor = autor
        self.__leer_libro = leer_libro
    def __del__(self):
        return None

    def leer_archivo(self):
        with open(self.__leer_libro,encoding="utf-8") as archivo:
            print(archivo.read())



libro = input("Escriba el archivo : ") 
if libro:
    if path.exists(libro):
        libro = Libro(leer_libro=libro)
        libro.leer_archivo()
    else:
        print("El archivo no existe")
else:
    print("Escriba el archivo")
print("dfd")
