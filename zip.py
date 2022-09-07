#Ejemplo zip
#zip se utiliza para agregar iterables en una tupla y 
#devuelve el resultado final, es decir combina listas y tuplas
#devuelve en una lista las parejas como TUPLAS 

cursos = ['Java', 'Python', 'Git']
asistentes = [15,20,9]

demo = zip(cursos,asistentes)
print(list(demo))