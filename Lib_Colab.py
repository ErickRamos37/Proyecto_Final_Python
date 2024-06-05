import random

# Genera una lista con numero random 
def list_random(rango_inicial, rango_final, tamano):
    lista = []
    i = 0
    for i in range(tamano):
        numero_aleatorio = random.randint(rango_inicial, rango_final)
        while numero_aleatorio in lista:
            numero_aleatorio = random.randint(rango_inicial, rango_final)
        lista.append(numero_aleatorio)
    return lista

# Valida numero enteros
def vali_num(msg, ri, rf):
    while True:
        try:
            num = int(input(msg))
            if num < ri:
                raise ValueError
            elif num > rf:
                raise ValueError
        except ValueError:
            print(f"Erro: Ingresa un valor entero positivo del {ri} al {rf}")
            continue

        return num
        break