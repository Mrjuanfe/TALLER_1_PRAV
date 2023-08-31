##Funcion para la constante 
def konstante (mensaje):
    k =int(input(mensaje))
    return k

def mensage (mensaje):
    """
    esta funcion me ingresa un texto y lo returna; el parametro es un strin 
    el control es para solo letras en el string
    """
    
    posicion = 0
    a = True
    sentence_1 = input (mensaje)
 
    while posicion<len(sentence_1):

        
        caracter = sentence_1[posicion]

        #pregunto si es solo letras
        if not sentence_1.isalpha () or not sentence_1.isspace ():
            a = False
            return sentence_1
            posicion+= 1
        
        
        else:
            print("ingrese una frase con letras de la [A ala Z]")
"fin primerafuncion"

while True:
    
    opcion = str(input('Ingresa c para cifrar o d para decifrar:  '))
    
    if opcion.lower()=='c':
        k = konstante("Ingrese la la constante que desea: ")
        

 
##Convertir a letras a codigo ASCII

        resultado = mensage("Ingrese la frase a codificar: ")

        codificado = []


        for letra in resultado:
            codificado.append(ord(letra))
    
        print("El mesaje '{}' se convierte en '{}' ".format(resultado, codificado))

##Cifrado 
        letras_separadas = []
        x = 0

        for i in codificado:
            print(x)
            C = codificado [0+x] + ( k % 27 )
            print(C)
            letras_separadas.append(C)
            x = x + 1


        print('El Cifrado es :', letras_separadas)
    
        caracteres = [chr(letra_separada) for letra_separada in letras_separadas ]

        print(caracteres)

        palabra_codificada = "".join(caracteres)

        print(palabra_codificada)
        break

    elif opcion.lower()=='d':

##Decifrado 

        k = konstante("Ingrese la la constante que desea: ")

 
##Convertir a letras a codigo ASCII

        resultado = mensage("Ingrese la frase a codificar: ")

        codificado = []


        for letra in resultado:
            codificado.append(ord(letra))
            
        print("El mesaje '{}' se convierte en '{}' ".format(resultado, codificado))

        ##Decifrado 
        letras_separadas = []
        x = 0


        for i in codificado:
            print(x)
            C = codificado [0+x] - ( k % 27 )
            if C<65:
                k_negativo = k % 27
                k_negativo = -k_negativo
                print(k_negativo)
                if k_negativo<0:
                    k_negativo = k_negativo % 27
                    print(k_negativo)
                    print(C)
                C= 64 + k_negativo
                print(C)
            print(C)
            letras_separadas.append(C)
            x = x + 1


        print('El decifrado es :', letras_separadas)
            
        caracteres = [chr(letra_separada) for letra_separada in letras_separadas ]

        print(caracteres)

        palabra_codificada = "".join(caracteres)

        print(palabra_codificada)
        break
        
    else: 
        print('Por favor ingresa la letra c o d, intentalo de nuevo: ')