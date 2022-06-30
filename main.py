
def procesar_archivo(analisis):
    print('\nProcesando\n')


def solicitar_periodicidad():
    periodicidad= (input('Escoja la periodicidad para el análisis: \n 1) Tres Meses\n 2) Seis Meses\n 3) Doce Meses\n '))
    if periodicidad == '1':
        periodicidad = 'Tres Meses'
    elif periodicidad == '2':
        periodicidad = 'Seis Meses'
    elif periodicidad == '3':
        periodicidad = 'Doce Meses'
    else:
        print('Opción no válida. \n Oprima 0 para reintentar o cualquier tecla para terminar\n ')
        if periodicidad =='0':
            solicitar_periodicidad()
        else:
            salir()
    return periodicidad

def salir():
    print('*'*100)
    print('\n')
    print('Gracias por utilizar nuestros servicios\n')
    print('*'*100)

def empezar(analisis):
    print('*'*100)
    print('Bienvenido al sistema de análisis y procesamientos de archivos\nPor el momento solo tenemos disponibles "La inflación: período..." y "Índices de precios: período..."')
    opcion = input('Seleccione:\n 1 para "Inflación"\n 2 para "Salarios"\n 3 para ambos\n 4 para salir\n\n Opción seleccionada: ')
    if opcion == '4':
        salir()
    elif opcion == '3':
        analisis['periodicidad']=periodicidad = solicitar_periodicidad()
        analisis['archivo']='ambos'
        procesar_archivo(analisis)
        print(f'Procesar {analisis["archivo"]}. Periodicidad: {analisis["periodicidad"]}\n')
        print('*'*100)
    elif opcion == '2':           
        analisis['periodicidad']=periodicidad = solicitar_periodicidad()
        analisis['archivo']='salarios.csv'
        procesar_archivo(analisis)
        print(f'Procesar {analisis["archivo"]}. Periodicidad: {analisis["periodicidad"]}\n')
        print('*'*100)
    elif opcion == '1':           
        analisis['periodicidad']=periodicidad = solicitar_periodicidad()
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
    analisis={'archivo':'','periodicidad':''}
    empezar(analisis)