#Ejemplo de ejemplo multihilo con _thread y time

import _thread
import time

def main():
    pass

def horaActual(nombre_thread, tiempo_de_espera):
    
    count = 0
    
    while count < 3:
        time.sleep(tiempo_de_espera)
        print(f'hilo : {nombre_thread} - {time.ctime(time.time())}')
        count += 1

_thread.start_new_thread(horaActual,('Ejecutando thread uno',1)) 
_thread.start_new_thread(horaActual,('Ejecutando thread dos',4))

while True:
    time.sleep(1)

if __name__ == "__main__":
    main()