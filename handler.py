import csv
import os
from funciones import convertir_archivos, calcular_anio, armar_periodo


# Direccion destino del nuevo dataset
path_file_output = os.path.join(os.path.dirname(os.getcwd()), "Proyecto Python Inicial")

# Nombre del archivo a escribir/crear
name_output = "periodo_promedio_salarios_inflacion.csv"

def procesar(a_dic):
    file = convertir_archivos(a_dic['archivo'])
    inicio = calcular_anio(file,a_dic['inicio'])
    fin = calcular_anio(file,a_dic['fin'])
    promedios_inflación = []
    for i in range(inicio,fin+1,a_dic['periodicidad']):
        total=0
        for j in range(i,i+3):
            total += float(file[j][1])
        promedios_inflación.append(total/3)

    
    periodos = armar_periodo(a_dic['periodicidad'],a_dic['inicio'],a_dic['fin']+1)

    # sobre escribo el header
    new_header = ['Período', 'Índice de Inflación', 'Índice de Salarios']
  
    # Abro/creo y escribo el archivo con los nuevos datos
    try:
         with open(os.path.join(path_file_output, name_output), 'w', newline='',
            encoding='utf_8') as new_dataset:
            csvwriter = csv.writer(new_dataset, delimiter=',')
            csvwriter.writerow(new_header)
            for i in range(len(periodos)):
                for j in range(len(promedios_inflación)):
                    csvwriter.writerow([periodos[j], promedios_inflación[j]])
    except:
        print('ERROR: No se ha podido realizar el archivo.')
    else:
        print('Se ha creado el archivo correctamente.')

if __name__ == '__main__':
    new_dic = {'archivo': 'inflacion', 'periodicidad':3, 'inicio': 2010,'fin':2020, 'salida': 'name'}
    procesar(new_dic)