##### TP1 ######

import sys
from os import system
arch = ""
cache, inexistentes, nuevas, archivo_final= [],[],[],[]

################# MODULOS ##################

def ingresar_texto():  # Guarda texto ingresado en una variable
    arch = ""
    system('cls')
    print("MODO INTERACTIVO\n\nIngrese el texto: \n")
    while True:
        frase = input(">")
        if frase == "@fin" : 
            print('\nHa finalizado el ingreso de texto.')
            break
        arch+= frase + "\n"
    return arch

def levantar_texto(nombre_arch): # extrae texto de un archivo
    system('cls')
    print('MODO ARCHIVO\n')
    arch = ''
    opciones= ('1','2','')
    while True:  
        try:
            with open(nombre_arch, 'r', encoding='utf-8') as texto:
                for linea in texto:
                    arch += linea
            break
        except FileNotFoundError:
            print('El archivo no existe!')
            opc = input('\n1- INTENTAR CON OTRO NOMBRE DE ARCHIVO\n\n2- SALIR\n\nSu opción: ')
            while opc not in opciones:
                opc = input('1- INTENTAR CON OTRO NOMBRE DE ARCHIVO\n\n2- SALIR\n\nSu opción: ')
            if opc == '1': 
                system('cls')
                nombre_arch = input("MODO ARCHIVO\n\nIngrese el nombre del archivo: ")
            else: break
    return arch
    
def eliminar_tildes(archivo): # Elimina tildes y signos del texto ingresado
    a,b,c = 'áéíóúü','aeiouu',"!#$¡%&'()*+,─—-./:;<=>?@[]^_`{|}~'"
    arch_2 = archivo.lower().translate(archivo.maketrans(a,b,c))
    arch_2 = arch_2.rstrip().split() #convierte en lista de palabras
    return arch_2

def buscar_faltantes(archivo): # Busca palabras faltantes en el diccionario y crea caché
    inexistentes,cache = [], []
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
                if palabra not in inexistentes: # agrega palabra solo si no existe ya en la lista
                    inexistentes.append(palabra)       
    return inexistentes 

def mostrar_resultado(inexistentes): 
    c = len(inexistentes)
    if len(inexistentes) == 0: print("\nTodas las palabras están en el diccionario.")
    else : print(f"\nEl texto contiene {c} {'palabras' if c > 1 else 'palabra'} que no {'están' if c> 1 else 'está'} en el diccionario.") 
    input('\nPresione *ENTER*')

def menu_inexistentes(inexistentes,arch): # menú para decidir sobre que hacer con las palabras que no están en el archivo 
    nuevas=[]
    opciones=('1','2','3')
    for palabra in inexistentes:
        system('cls')
        print(f'\nLa palabra * {palabra} * no está en el diccionario')
        print('\n1- AGREGAR AL DICCIONARIO\n2- CORREGIR PALABRA\n3- IGNORAR Y SEGUIR\n')
        opc = input('Su opción: ')
        while opc not in opciones:
            opc = input('\nPor favor ingrese una opcion válida.\nSu opción: ')
        if opc == '1':
            with open('spanish.lst', 'a', encoding='UTF-8') as diccionario:
                diccionario.write('\n' + palabra)
        elif opc == '2':
            nueva_palabra = input('\nEscriba nuevamente la palabra: ')
            arch = arch.replace(palabra,nueva_palabra)
    return arch

############## PROGRAMA PRINCIPAL ####################
 
n = len(sys.argv)# cantidad de argumentos pasada desde consola

if n == 1:
    arch = ingresar_texto()  
    arch_2 = eliminar_tildes(arch)
    inexistentes = buscar_faltantes(arch_2)
    if len(inexistentes)!=0:
        mostrar_resultado(inexistentes)
        archivo_final = menu_inexistentes(inexistentes,arch)

    print('\n', archivo_final)
    print('Todas las palabras están en el diccionario.')
    input()
  
else:
    arch = levantar_texto(sys.argv[1])
    if arch != '': 
        arch_2 = (eliminar_tildes(arch))
        inexistentes = buscar_faltantes(arch_2)
        if len(inexistentes)>0:
            mostrar_resultado(inexistentes)
            archivo_final = menu_inexistentes(inexistentes,arch)
    print('\n', archivo_final)
    print('Todas las palabras están en el diccionario.')
    input()
            
     
