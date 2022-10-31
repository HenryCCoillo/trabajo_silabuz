from os import path
import json

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
    
    def listar_libros(self):
        with open("prueba.json",encoding="utf-8") as archivo:
            datos_libros = json.load(archivo)

            for i in datos_libros:
                diccionario_libro = datos_libros[i]
                nombre_libro_id =diccionario_libro["id"]
                nombre_libro_titulo = diccionario_libro["titulo"]
                nombre_libro_genero =diccionario_libro["genero"] 
                nombre_libro_isbn =diccionario_libro["isbn"] 
                nombre_libro_editorial =diccionario_libro["editorial"] 
                nombre_libro_autor =diccionario_libro["autor"] 
                print(f"\n-El Libro llamano {nombre_libro_titulo}, su genero es {nombre_libro_genero}, su codigo de isbn es {nombre_libro_isbn}, la editorial es {nombre_libro_editorial} y el autor es {nombre_libro_autor}\n")




###################################################################################################################################################

# libro = input("Escriba el archivo : ") 
# if libro:
#     if path.exists(libro):
#         libro = Libro(leer_libro=libro)
#         libro.leer_archivo()
#     else:
#         print("El archivo no existe")
# else:
#     print("Escriba el archivo")


libro = Libro()
libro.leer_archivo()