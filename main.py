import handler


def procesar_archivo(analisis):
    print('\nProcesando\n')
    handler.procesar(analisis)
    print ('\n')
    opcion = input('¿Desea realizar otro análisis? Seleccione 1 para sí o cualquier otra tecla para terminar. \n')
    if opcion == '1':
        empezar()
    else:
        salir()

def solicitar_periodicidad(analisis):
    periodicidad= (input('Escoja la periodicidad para el análisis: \n 1) Tres Meses\n 2) Seis Meses\n 3) Doce Meses\n '))
    if periodicidad == '1':
        analisis['periodicidad'] = 3
    elif periodicidad == '2':
        analisis['periodicidad'] = 6
    elif periodicidad == '3':
        analisis['periodicidad'] = 12
    else:
        print('Opción no válida. \n Oprima 0 para reintentar o cualquier tecla para terminar\n ')
        if periodicidad =='0':
            solicitar_periodicidad(analisis)
        else:
            salir()

def seleccionar_anio(analisis):
    anio = input('Escoja el año de inicio del análisis. Hasta 2020 inclusive\n ')
    try: 
        anio = int(anio)
    except:
        print('El año debe ser un número')
        seleccionar_anio(analisis)
    if (anio > 2021) or (anio <2016):
        print(f'El año debe estar entre 2016 y 2021. Año seleccionado: {anio}')
        seleccionar_anio(analisis)
    else:
        analisis['inicio']=anio
    anio_fin = input('Escoja el año de finalización del análisis. Hasta 2021 inclusive\n ')
    try: 
        anio_fin = int(anio_fin)
    except:
        print('El año debe ser un número')
        seleccionar_anio(analisis)
    if ((anio_fin > 2021) or (anio_fin <2016)) | (anio_fin < anio):
        print(f'El año debe estar entre 2008 y 2021. Y no puede ser menor al año de inicio.\n')
        seleccionar_anio(analisis)
    else:
        analisis['fin']=anio_fin

def nombre_de_salida_del_archivo(analisis):
    nombre = input('Introduzca el nombre de salida del nuevo archivo: ')
    if nombre =='':
        nombre ='archivo_procesado'
    validar_nombre = input(f'El nombre escogido es: {nombre}. \n Seleccione 1 para aceptar o 0 para cambiar: ')  
    if validar_nombre == '1':
        analisis['salida']=f'{nombre}.csv'
    else:
        nombre_de_salida_del_archivo(analisis)

def salir():
    print('*'*100)
    print('\n')
    print('Gracias por utilizar nuestros servicios\n')
    print('*'*100)

def imprimir_inicio():
    print('*'*100)
    print('Bienvenido al sistema de análisis y procesamientos de archivos de inflación y SMVM en Argentina. Período 2016-2021) \n')
    print('*'*100)
    empezar()

def empezar():
    analisis={'periodicidad':'','inicio':-1,'fin':-1,'salida':''}
    solicitar_periodicidad(analisis)
    seleccionar_anio(analisis)
    nombre_de_salida_del_archivo(analisis)
    print (analisis)
    procesar_archivo(analisis)
            
if __name__ == "__main__":
    imprimir_inicio()