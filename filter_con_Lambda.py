#Ejemplo funcion filter con y sin lambda
#filter aplica una funcion a todos los elementos de una lista,
#si devuelve true guarda el valor , si no , no lo devuelve
from operator import truediv


numeros = [1,2,3,4,5,6,7,8,9,10]

#definimos una funcion que devuelva true si es par
def mifuncion(x):
    if x % 2 == 0:
        return True
    return False


resultado = filter(mifuncion,numeros)
print(list(resultado))

#con lambda
resultado = filter(lambda x:x%2 == 0, numeros)
print(list(resultado))



def funcion2(x):
    if(str(x).startswith('ped')):
        return True
    return False

#sin lambda
resultado = filter(funcion2, ['pedrito', 'adios', 'pedro'])
print(list(resultado))

#con lambda 
resultado = filter(lambda x:str(x).startswith('ped'), ['pedrito', 'adios', 'pedro'])
print(list(resultado))
 