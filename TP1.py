import sys
from os import system
arch = ""
cache = []
inexistentes = []

################# MODULOS ##################

def ingresar_texto():  # Guarda texto ingresado en una variable
    arch = ""
    system('cls')
    print("MODO INTERACTIVO\n\nIngrese el texto: \n")
    while True:
        frase = input("> ").lower()
        if frase == "@fin" : 
            print('\nHa finalizado el ingreso de texto.')
            break
        arch += frase + "\n "
    return arch


def levantar_texto(): # extrae texto de un archivo
    system('cls')
    opciones= ('1','2','')
    arch = ''
    while True:
        system('cls')
        nombre = input("MODO ARCHIVO\n\nIngrese el nombre del archivo: ")
        try:
            with open(nombre, 'r', encoding='utf-8') as texto:
                for linea in texto:
                    linea = linea.lower()
                    arch += linea
            break
        except FileNotFoundError:
            print('\nEl archivo no existe!')
            opc = input('\n1- INTENTAR OTRA VEZ\t2- SALIR\n\nSu opción: ')
            while opc not in opciones:
                opc = input('1- INTENTAR OTRA VEZ\t2- SALIR\n\nSu opción: ')
            if opc == '1': continue
            else: break

    return arch
    
      

def eliminar_tildes(archivo): # Elimina tildes y signos del texto ingresado
    a,b,c = 'áéíóúü','aeiouu',"!#$¡%&'()*+,─—-./:;<=>?@[]^_`{|}~'"
    arch_2 = archivo.translate(archivo.maketrans(a,b,c))
    arch_2 = arch_2.rstrip().split() #convierte en lista de palabras
    return arch_2

def buscar_faltantes(archivo): # Busca palabras faltantes en el diccionario y crea caché
    inexistentes= []
    for palabra in archivo:
        if palabra not in cache: # si la palabra está en el caché sigue con otra 
            coincidencia = False
            with open('spanish.lst', 'r', encoding='UTF-8') as diccionario:
                for palabra_dicc in diccionario:
                    palabra_dicc = palabra_dicc.rstrip()
                    if  palabra == palabra_dicc:
                        cache.append(palabra) # Agrega al cache las palabras encontradas.       
                        coincidencia = True
                        break
            if not coincidencia:
                if palabra not in inexistentes:
                    inexistentes.append(palabra)  
                
    return inexistentes 

def mostrar_resultado(inexistentes):
    c = len(inexistentes)
    if len(inexistentes) == 0: print("\nTodas las palabras están en el diccionario.")
    else : print(f"\nEl texto contiene {c} {'palabras' if c > 1 else 'palabra'} que no {'están' if c> 1 else 'está'} en el diccionario\n")        
    
    for i in inexistentes:
        print(i)   
    input("")              
############## PROGRAMA PRINCIPAL ############

while True:
    system('cls')
    opciones = ('1','2')
    opcion= input('''CORRECTOR DE TEXTO:\n
1- MODO INTERACTIVO\n 
2- MODO ARCHIVO\n
Elija una opción: ''')

    if opcion not in opciones:
        continue
    elif opcion == '1':
        arch = ingresar_texto()
        arch_2 = eliminar_tildes(arch)
        inexistentes = buscar_faltantes(arch_2)
        mostrar_resultado(inexistentes)

    else:
        arch = levantar_texto()
        if arch == '': continue
        arch_2 = (eliminar_tildes(arch))
        inexistentes = buscar_faltantes(arch_2)
        mostrar_resultado(inexistentes)
        
    







