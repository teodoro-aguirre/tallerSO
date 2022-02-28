import threading, time

d1 = 0
d2 = 0
resultados = []

def operacionAritmetica(nombre, operacion, segundos):
    global resultados, d1, d2
    
    while d1 == 0 or d2 == 0:
        time.sleep(segundos)
        
    # suma
    if operacion == 1:
        resultados.append(d1 + d2)
    # resta
    elif operacion == 2:
        resultados.append(d1 - d2)
    # multiplicacion
    elif operacion == 3:
        resultados.append(d1 * d2)
    # division
    elif operacion == 4:
        resultados.append(d1 / d2)
    print("El hilo: " + nombre + " depositó")
    
hiloSuma = threading.Thread(target = operacionAritmetica, args = ("Sumador",1, 3))
hiloResta = threading.Thread(target = operacionAritmetica, args = ("Restador",2, 8))
hiloMultiplicacion = threading.Thread(target = operacionAritmetica, args = ("Multiplicacion",3, 10))
hiloDivision = threading.Thread(target = operacionAritmetica, args = ("Divisor",4, 15))

hiloSuma.start()
hiloResta.start()
hiloDivision.start()
hiloMultiplicacion.start()

print("Este es el hilo principal")
d1 = int(input("Escribe el primer numero: "))
d2 = int(input("Escribe el segundo numero: "))

while len(resultados) < 4:
    print("Resultados incompletos")
    print(resultados)
    time.sleep(1)
    
print("Resultados completos")
print(resultados)
