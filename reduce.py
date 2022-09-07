#Ejemplo reduce 
#reduce(funcion,lista)
#ejecuta de forma recursiva una funcion sobre la lista
#hasta que la lista se quede con un solo elemento


from functools import reduce 
def suma(a,b):
    print(f'a = {a}, b = {b}')
    return a + b  

resultado = reduce(suma,[1,2,3,4,5,6,7,8,9,10]) 
#mostrara la suma de todos los elementos
print(resultado)

resultado = reduce(lambda a,b:a+b,[1,2,3,4,5,6,7,8,9,10])  
print(resultado)