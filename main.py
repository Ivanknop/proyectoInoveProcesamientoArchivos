
#import handler

def procesar_archivo(analisis):
    print('\nProcesando\n')
    print(f'Procesar {analisis["archivo"]}. Año inicio: {analisis["anio_inicio"]}. Periodicidad: {analisis["periodicidad"]}.Nombre de salida: {analisis["nombre"]}\n')
    print('*'*100)
    #handler.procesar(analisis)
    
def seleccionar_anio(analisis):
    anio = input('Escoja el año de inicio del análisis. \n (ATENCIÓN: índice proyectado de inflación desde 2007, índice de salarios desde 2016)\n ')
    try: 
        anio = int(anio)
    except:
        print('El año debe ser un número')
        seleccionar_anio(analisis)
    if (anio > 2022) or (anio <2007):
        print(f'El año debe estar entre 2007 y 2022. Año seleccionado: {anio}')
        seleccionar_anio(analisis)
    else:
        analisis['anio_inicio']=anio
    
def nombre_del_archivo(analisis):
    nombre = input('Introduzca el nombre de salida del nuevo archivo: ')
    validar_nombre = input(f'El nombre escogido es: {nombre}. \n Seleccione 1 para aceptar o 0 para cambiar: ')  
    if validar_nombre == '1':
        analisis['nombre']=nombre
    else:
        nombre_del_archivo(analisis)

def solicitar_periodicidad(analisis):
    periodicidad= (input('Escoja la periodicidad para el análisis: \n 1) Tres Meses\n 2) Seis Meses\n 3) Doce Meses\n '))
    if periodicidad == '1':
        analisis['periodicidad'] = 'Tres Meses'
    elif periodicidad == '2':
        analisis['periodicidad'] = 'Seis Meses'
    elif periodicidad == '3':
        analisis['periodicidad'] = 'Doce Meses'
    else:
        print('Opción no válida. \n Oprima 0 para reintentar o cualquier tecla para terminar\n ')
        if periodicidad =='0':
            solicitar_periodicidad(analisis)
        else:
            salir()

def salir():
    print('*'*100)
    print('\n')
    print('Gracias por utilizar nuestros servicios\n')
    print('*'*100)

def imprimir_inicio():
    print('*'*100)
    print('Bienvenido al sistema de análisis y procesamientos de archivos\nPor el momento solo tenemos disponibles "La inflación: período..." y "Índices de precios: período..."')
    print('*'*100)
    empezar()

def empezar():
    analisis={'archivo':'','periodicidad':'','anio_inicio':'','nombre':''}
    opcion = input('Seleccione:\n 1 para "Inflación"\n 2 para "Salarios"\n 3 para ambos\n 4 para salir\n\n Opción seleccionada: ')
    if opcion == '4':
        salir()
    elif opcion == '3':
        solicitar_periodicidad(analisis)
        seleccionar_anio(analisis)
        analisis['archivo']='ambos'
        nombre_del_archivo(analisis)
        procesar_archivo(analisis)
    elif opcion == '2':
        seleccionar_anio(analisis)           
        solicitar_periodicidad(analisis)
        analisis['archivo']='salarios'
        procesar_archivo(analisis)
    elif opcion == '1':      
        seleccionar_anio(analisis)
        solicitar_periodicidad(analisis)
        analisis['archivo']='inflacion'
        procesar_archivo(analisis)
    else:
        opcion = input('Opción no válida. Oprima 0 para reintentar o cualquier tecla para terminar\n ')
        if opcion == '0':
            empezar()
        else:
            salir()                
    
if __name__ == "__main__":
    imprimir_inicio()
    opcion = input('¿Desea realizar otro análisis? Seleccione 1 para sí o cualquier otra tecla para terminar. \n')
    if opcion == '1':
        empezar()
    else:
        salir()
