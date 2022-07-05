import os
import csv


def convertir():


    # Direccion del archivo a leer
    path_file_input = os.path.join(os.path.dirname(os.getcwd()), "Proyecto Python Inicial")
    print(path_file_input)
    # Nombre del archivo a leer
    name_input = "expectativas_inflacion.csv"

    # Direccion destino del nuevo dataset
    path_file_output = os.path.join(os.path.dirname(
        os.getcwd()), "Proyecto Python Inicial")

    # Nombre del archivo a escribir/crear
    name_output = "periodo_promedio_inflacion.csv"

    try:
        # Abro el archivo a leer y lo cargo  en una lista sin el encabezado
        with open(os.path.join(path_file_input, name_input), encoding='utf_8') as data:
            csvreader = csv.reader(data, delimiter=',')
            header, data_file_input = next(csvreader), list(csvreader)

        # sobre escribo el header
        new_header = ['Período', 'Incremento Índice Inflación']

        # Genero una lista de listas con las columnas necesarias usando listcomprehension
        new_data = [[line[0], line[2]]
                    for line in data_file_input]

        # Abro/creo y escribo el archivo con los nuevos datos
        try:
            with open(os.path.join(path_file_output, name_output), 'x', newline='',
                    encoding='utf_8') as new_dataset:
                csvwriter = csv.writer(new_dataset, delimiter=',')
                csvwriter.writerow(new_header)
                csvwriter.writerows(new_data)
        except:
            pass
    except FileNotFoundError:
        print('ERROR: No se ha encontrado el archivo.')
    else:
        print('Se ha creado el archivo correctamente.')
    return new_data