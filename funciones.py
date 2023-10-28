#Funciones tradicionales:
#permiten reutilizar codigo, ahorrar lineas de codigo, dividir las diferentes tareas

"""
sintaxis: 
def nombre_funcion(parametro):
    bloqueo de codigo
    return (retorno uno o varios valores)

"""

#crear una funcion que calcule el promedio de dos notas
def promedio(nota1, nota2):
    resultado = (nota1 + nota2)/2
    return resultado
#invocar o llamar la funcion:
print(promedio(5,3))

#opcion 2:
def promedio(nota1, nota2):
    return (nota1 + nota2)/2

resultado = promedio(10,5)

print(resultado)

#funcion sin parametros, ni return
def deberes_estudiante():
    print("Asistir clases\n ser puntual en la entrega de trabajos \n presentar las pruebas de conocimiento \n Cuidar los recursos de la institucion" )

deberes_estudiante()

#funcion con un solo parametro:
def saludo(name):
    print(f"Hola {name}!!!")
saludo("pepito")

#Funcion con parametro con valor clave

def suma(a, b, c): #(b=10,a)
    return b+a+c

"""resutado1 = suma(12)
print(resutado1)"""

print(suma(13,56,32))

#parametro de longitud variable: *args

def multiplicar(*num):
    resultado3 = 0
    for n in num:
        resultado3 *= n
    print(resultado3)
multiplicar(1,2,3,4,5,6)

#crear una funcoon donde el usuario ingrese numeros enteros positivos a una lista y en otra nueva almacene solamente los numeros impares.

def separarNumeros(ListaNum=[]):
    ListaPares = []
    ListaImpares = []
    for n in range(0, len(ListaNum)):
        valor = ListaNum[n]
        if valor % 2 == 0:
            ListaPares.append(valor)
        else:
            ListaImpares.append(valor)
    return ListaPares, ListaImpares

ListadoNumeros = []
TamañoLista = int(input("Favor Ingresar la cantidad de numeros que desea: "))
for j in range(0, TamañoLista):
    numero = int(input("Favor Ingresar un numero: "))
    ListadoNumeros.append(numero)

print(separarNumeros(ListadoNumeros))