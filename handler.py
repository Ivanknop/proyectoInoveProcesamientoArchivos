import csv
import os
import pathlib
import converter_inflacion
import converter_salarios


def procesar(a_dic_file):
    '''
    Recibe un diccionario para procesar la información solicitada desde el main
    '''

    file_inflacion = converter_inflacion.convertir()
    inicio_inflacion = posicion_en_archivo(file_inflacion, a_dic_file['inicio'])
    fin_inflacion = posicion_en_archivo(file_inflacion, a_dic_file['fin']+1)

    file_salarios = converter_salarios.convertir()
    inicio_salarios = posicion_en_archivo(file_salarios, a_dic_file['inicio'])
    fin_salarios = posicion_en_archivo(file_salarios, a_dic_file['fin']+1)

    cantidad_meses = a_dic_file['periodicidad']
    periodos = armar_periodo(cantidad_meses, a_dic_file['inicio'],
                             a_dic_file['fin']+1)

    promedios_inflacion = calcular_promedios_inflacion(file_inflacion, inicio_inflacion,
                                             fin_inflacion, cantidad_meses)
    salarios_promediados = calcular_promedios_salarios(file_salarios, inicio_salarios,
                                              fin_salarios, cantidad_meses)

    crear_archivo(periodos, promedios_inflacion, salarios_promediados, a_dic_file['salida'])


def crear_archivo(periodos, promedios_inflacion, salarios_promediados,
                  nombre_salida):
    '''
        Crea el archivo de salida
    '''
    # Direccion destino del nuevo dataset
    path_file_output = pathlib.Path(__file__).parent.absolute()

    # sobreescribo el header
    new_header = ['Período', 'Índice de Inflación Acumulado', 'Índice de Salarios']
    # Abro/creo y escribo el archivo con los nuevos datos
    try:
        with open(os.path.join(path_file_output, nombre_salida), 'w', newline='',
                                              encoding='utf_8') as new_dataset:
            csvwriter = csv.writer(new_dataset, delimiter=',')
            csvwriter.writerow(new_header)
            for line in range(len(periodos)):
                csvwriter.writerow([periodos[line], promedios_inflacion[line],
                                   salarios_promediados[line]])
    except:
        print('ERROR: No se ha podido realizar el archivo.')
    else:
        print('Se ha creado el archivo correctamente.')


def posicion_en_archivo(file, anio):
    '''
    Recibe una lista y un año y devuelve la posición donde inicia ese año en el la lista
    '''
    pos = 0
    while int(file[pos][0].split(sep='-')[0]) < int(anio):
        pos += 1
    return pos


def armar_periodo(periodo, ini, fin):
    '''
    Esteblece el rango temporal seleccionado. Recibe año de inicio, de finalización y período de meses
    '''
    meses = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep',
            'oct', 'nov', 'dic']
    new_list = []
    for y in range(ini, fin):
        for m in range(0, 12, periodo):
            date = f' {str(y)}  {meses[m]} - {meses[m+periodo-1]}'
            new_list.append(date)
    return new_list


def calcular_promedios_inflacion(lista, ini, fin, periodo):
    '''
    Recibe la lista del archivo, las posiciones inicial y final y el período y retorna la información procesada
    '''
    lista_promediada = []
    acumulado = float(lista[ini][1])
    promedio = 0
    count = 0
    for i in range(ini, fin+1):
        promedio = promedio + float(lista[i][1])
        count += 1
        if count == periodo:
            acumulado += promedio/periodo
            lista_promediada.append(acumulado)
            promedio = 0
            count = 0
    return lista_promediada

def calcular_promedios_salarios(lista, ini, fin, periodo):
    '''
    Recibe la lista del archivo, las posiciones inicial y final y el período y retorna la información procesada
    '''
    lista_promediada = []
    promedio = 0
    count = 0
    for i in range(ini, fin+1):
        promedio = promedio + float(lista[i][1])
        count += 1
        if count == periodo:
            lista_promediada.append(promedio/periodo)
            promedio = 0
            count = 0
    return lista_promediada
