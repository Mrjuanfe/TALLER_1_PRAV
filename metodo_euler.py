import funciones_copy

def metodo_euler(funcion_derivada, x0, y0, h, num_pasos):
    resultados = [(x0, y0)]
    x = x0
    y = y0
    
    for _ in range(num_pasos):
        y += h * funcion_derivada(x, y)
        x += h
        resultados.append((x, y))
        
    return resultados

# Definición de la función derivada dy/dx = x
def funcion_derivada(x, y):
    return eval(function_str)

##Programa principal 

# Parámetros iniciales
primer_valor= funciones_copy.pedir_numerofloat('Ingrese el valor inicial de x (x0): ')

segundo_valor= funciones_copy.pedir_numerofloat('Ingrese el valor inicial de y y0: ')

paso= funciones_copy.pedir_numerofloat('Ingrese el tamaño del paso (h): ')

numero_pasos= funciones_copy.pedir_numeroint('Ingrese el numero de pasos (n): ') 

function_str = input("Ingresa una función en términos de 'x' y 'y': ")

##Tabulacion 

print('Iteraciones\t    x\t          y\n ---------------------------------------------------------')

# Resolución de la ecuación diferencial usando el método de Euler

resultados =metodo_euler(funcion_derivada, primer_valor, segundo_valor, paso, numero_pasos)

iteraciones = 1


# Imprimir los resultados
for x, y in resultados:
    print(f"{iteraciones}\t   \t x = {x:.2f},    \t y = {y:.4f}")
    
    iteraciones = iteraciones + 1
    
    