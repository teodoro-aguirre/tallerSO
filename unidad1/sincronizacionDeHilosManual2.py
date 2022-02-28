import threading, time

d1 = 0
d2 = 0
resultados = [0 for i in range(4)]
SUMA = 0
RESTA = 1
MULTIPLICACION = 2
DIVISION = 3
SIN_VALOR = 0

def operacionAritmetica(nombre, operacion, segundos):
    global resultados, d1, d2, SUMA, RESTA, MULTIPLICACION, DIVISION
    
    while d1 == 0 or d2 == 0:
        time.sleep(segundos)
        
    # suma
    if operacion == 1:
        resultados[SUMA] = d1 + d2
    # resta
    elif operacion == 2:
        resultados[RESTA] = d1 - d2
    # multiplicacion
    elif operacion == 3:
        while resultados[SUMA] == SIN_VALOR or resultados[RESTA] == SIN_VALOR:
            print("Resultados incompletos(Suma, Resta)")
            time.sleep(1)
        resultados[MULTIPLICACION] = resultados[SUMA] * resultados[RESTA]
    # division
    elif operacion == 4:
        while resultados[SUMA] == SIN_VALOR or resultados[RESTA] == SIN_VALOR:
            print("Resultados incompletos(Suma, Resta)")
            time.sleep(1)
        resultados[DIVISION] = resultados[SUMA] / resultados[RESTA]
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

while resultados[SUMA] == SIN_VALOR or resultados[RESTA] == SIN_VALOR or resultados[MULTIPLICACION] == SIN_VALOR or resultados[DIVISION] == SIN_VALOR:
    print("Resultados incompletos")
    print(resultados)
    time.sleep(1)
    
print("Resultados completos")
print(resultados)
