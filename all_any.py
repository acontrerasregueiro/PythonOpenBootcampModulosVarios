#Ejemplo all y any. PALABRAS RESERVADAS
#Sirve para comprobar que todas (all) o algunas (any) de una
#lista se cumplan

listaA = [ 1== 1, 2==2, 3==4]
res = any(listaA) #devolvera true , ya que ALGUNA cumple la condificion
print(res)  

res = all(listaA) #devolvera FALSE , ya que TODAS DEBERIAN CUMPLIR LA CONDICION
print(res)  