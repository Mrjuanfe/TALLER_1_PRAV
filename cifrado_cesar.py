##Funcion para la constante 
def konstante (mensaje):
    k =int(input(mensaje))
    return k

        
            
def mensage (mensaje):
    """
    esta funcion me ingresa un texto y melo returna; el parametro es un strin 
    el control es para solo letras en el string
    """
    a = True

    while (a):

        sentence_1 = input (mensaje)
        sentence = sentence_1.split ()  # se separa el string en palabras y los lleva  auna lista
        sentence = "".join(sentence)  #esta linea toma esa lista y la une

        #pregunto si es solo letras
        if (sentence.isalpha ()):
            a = False                #termina mi ciclo
            return sentence_1
        
        else:
            print("ingrese una frase con letras de la [A ala Z]")


while True:
    
    opcion = str(input('Ingresa c para cifrar o d para decifrar:  '))
    
    if opcion.lower()=='c':
        k = konstante("Ingrese la la constante que desea: ")
        

 
##Convertir a letras a codigo ASCII

        resultado = mensage("Ingrese la frase a codificar: ")
        resultado=resultado.upper() #convertimos la variable mayuscula porque estamos trabjando con los numeros Ascii del 65 al 90
        

        codificado = []


        for letra in resultado:
            codificado.append(ord(letra))
    

##Cifrado 
        letras_separadas = []
        x = 0 #adentro del for la variable  x la creamos para indicarle posicion dentro de la ecuacuaion

        for posicion in codificado: 
        
            C = codificado [0+x] + ( k % 27 )
            
            letras_separadas.append(C)
            x = x + 1


        print('El Cifrado es :', letras_separadas)
    
        caracteres = [chr(letra_separada) for letra_separada in letras_separadas ] # convierte el nuevo valor ascii a caracter equivalente

        print(caracteres)

        palabra_codificada = "".join(caracteres)

        print(palabra_codificada)
        break

    elif opcion.lower()=='d':

##Decifrado 

        k = konstante("Ingrese la la constante que desea: ")

 
##Convertir a letras a codigo ASCII

        resultado = mensage("Ingrese la frase a codificar: ")
        resultado=resultado.upper() #convertimos la variable mayuscula porque estamos trabjando con los numeros Ascii del 65 al 90

        codificado = []


        for letra in resultado:
            codificado.append(ord(letra))
            
        print("El mesaje '{}' se convierte en '{}' ".format(resultado, codificado))

        ##Decifrado 
        letras_separadas = []
        x = 0


        for i in codificado:
           
            C = codificado [0+x] - ( k % 27 )
            if C<65:                    # Verifica si la resta esta por debajo del rango con el que trabajamos
                k_negativo = k % 27
                k_negativo = -k_negativo 
                
                if k_negativo<0:
                    k_negativo = k_negativo % 27 #Vuelve a realizar el modulo ya que nuestra operacion principal el resultado fue negativo
                  
                    
                C= 64 + k_negativo  #convierte al numero cifrado en cesar equivalente a la nueva clave
                
            
            letras_separadas.append(C)  #anadimos a la lista cada valor en la lista
            x = x + 1


            
        caracteres = [chr(letra_separada) for letra_separada in letras_separadas ]

        palabra_codificada = "".join(caracteres)

        print('La palabra Decifrada es: ',palabra_codificada)
        break
        
    else: 
        print('Por favor ingresa la letra c o d, intentalo de nuevo: ')