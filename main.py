
def procesar_archivo(analisis):
    print('\nProcesando\n')
    opcion = input('¿Desea realizar otro análisis? Seleccione 1 para sí o cualquier otra tecla para terminar. \n')
    if opcion == '1':
        empezar()
    else:
        salir()

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
    analisis={'archivo':'','periodicidad':''}
    opcion = input('Seleccione:\n 1 para "Inflación"\n 2 para "Salarios"\n 3 para ambos\n 4 para salir\n\n Opción seleccionada: ')
    if opcion == '4':
        salir()
    elif opcion == '3':
        solicitar_periodicidad(analisis)
        analisis['archivo']='ambos'
        procesar_archivo(analisis)
        print(f'Procesar {analisis["archivo"]}. Periodicidad: {analisis["periodicidad"]}\n')
        print('*'*100)
    elif opcion == '2':           
        solicitar_periodicidad(analisis)
        analisis['archivo']='salarios.csv'
        procesar_archivo(analisis)
        print(f'Procesar {analisis["archivo"]}. Periodicidad: {analisis["periodicidad"]}\n')
        print('*'*100)
    elif opcion == '1':           
        solicitar_periodicidad(analisis)
        analisis['archivo']='inflacion.csv'
        procesar_archivo(analisis)
        print(f'Procesar {analisis["archivo"]}. Periodicidad: {analisis["periodicidad"]}\n')
        print('*'*100)
    else:
        opcion = input('Opción no válida. Oprima 0 para reintentar o cualquier tecla para terminar\n ')
        if opcion == '0':
            empezar()
        else:
            salir()                
    
if __name__ == "__main__":
    imprimir_inicio()