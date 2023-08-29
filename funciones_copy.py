def Letra_Mayuscula(nombre):
    '''
    Convierte el string en letras mayusculas
    
    '''
    str(nombre)
    return nombre.upper()

def Letra_Minuscula(nombre):
    '''
    Convierte el strin en letras minusculas
    '''
    str(nombre)
    return nombre.lower()

def Quitar_Espacios(nombre):
    '''
    quita los espacios entre el string
    '''
    str(nombre)
    Name_pegado=nombre.replace(' ','')
    return Name_pegado

def Primer_nomnre(nombre):
    '''
    Separa la primera letra del nombre
    '''
    str(nombre)
    x=nombre.split()
    return x[0]

def pedir_numerofloat(mensaje):
    x=float(input(mensaje))
    return x


def pedir_numeroint(mensaje):
    x=int(input(mensaje))
    return x



def metodo_euler(funcion, x0, y0, h, num_pasos):
    resultados= [(x0, y0)]
    x=x0
    y=y0
    for i in range(num_pasos):
        F = funcion(x, y)
        x= x+h
        y= y+h * F
    return resultados    

 
    
    
    
   
    

         
        
        
    

