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

# Parámetros iniciales
primer_valor= funciones_copy.pedir_numerofloat('ingrese un numero para x0: ')
segundo_valor= funciones_copy.pedir_numerofloat('ingrese un numero para y0: ')
paso= funciones_copy.pedir_numerofloat('ingrese el tamaño del paso (h): ')
numero_pasos= funciones_copy.pedir_numeroint('ingrese el numero de pasos (n): ') 
function_str = input("Ingresa una función en términos de 'x' y 'y': ")
# Resolución de la ecuación diferencial usando el método de Euler
resultados =metodo_euler(funcion_derivada, primer_valor, segundo_valor, paso, numero_pasos)

# Imprimir los resultados
for x, y in resultados:
    print(f"x = {x:.2f}, y = {y:.4f}")
