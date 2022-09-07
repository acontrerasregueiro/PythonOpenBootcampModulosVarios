#Ejemplo map
#map aplica una funcion a todos los elementos de un iterable (listas y duplas)
#map(funcion,lista)

def cuadrado(x):
    return x * x  

resultado = map(cuadrado,[1,2,3,4,5,6,7,8,9,10])
print(list(resultado))

resultado = map(lambda x:x*x,[1,2,3,4,5,6,7,8,9,10]) 
print(list(resultado))