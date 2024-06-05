import random
import Lib_Colab
import Constantes

def generar_operaciones(difcult):
    operacion = []
    operacion = Lib_Colab.list_random(0, Constantes.RANGO_MAXIXO_OPERACIONAL * difcult, Constantes.CANTIDAD_OPERACIONES)
    op = random.randint(1, difcult)
    resultado = 0
    if op == 1:
        for i in range(0, len(operacion)):
            resultado = resultado + operacion[i]
        op = "+"
    elif op == 2:
        resultado = operacion[0]
        for i in range(1, len(operacion)):
            resultado = resultado - operacion[i]
        op = "-"
    elif op == 3:
        resultado = operacion[0]
        for i in range(1, len(operacion)):
            resultado = resultado * operacion[i]
        op = "x"
    operacion.append(resultado)
    operacion.append(op)
    return operacion

def posibles_resultados(respeta, difcult):
    resultado = []
    resultado = Lib_Colab.list_random(0, Constantes.RANGO_MAXIXO_OPERACIONAL * difcult, Constantes.CANTIDAD_OPERACIONES)
    resultado.append(respeta)
    random.shuffle(resultado)
    return resultado
    
def imprimir_operacion(operacion, opciones):
    tamano = len(operacion)
    for i in range(0, tamano - 2):
        if i != 0:
            print(operacion[tamano - 1])
            
        print(operacion[i])
        
    print(f"Posibles Respuestas:")
    for i in range(0, tamano - 1):
        print(f"{i + 1}.    {opciones[i]}")
    
def respueta_usiario(operacion, opciones):
    eleccion = Lib_Colab.vali_num("Ingresa la opcion que corresponda a tu eleccion: ", 1, len(opciones))
    if opciones[eleccion - 1] == operacion[len(operacion) - 2]:
        print("Felicidades, respondiste correctamente")
        
    else:
        print(f"Lastima has respondido mal, la respueta correcta es {operacion[len(operacion) - 2]}")