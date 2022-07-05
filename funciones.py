import converter_inflacion, converter_salarios 


def convertir_archivos(archivo):
    if archivo == 'inflacion':
        file = converter_inflacion.convertir()
    else:
        file = converter_salarios.convertir()
    return file

def calcular_anio(file,anio):
    pos = 0
    while int(file[pos][0].split(sep='-')[0]) != anio: 
        pos+=1
    return pos

def armar_periodo(periodo,ini,fin):
    meses = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
    new_list =[]
    for y in range(ini,fin):
        for m in range (0,12,periodo):
            date = f' {str(y)}  {meses[m]} - {meses[m+2]}'
            new_list.append(date)
    return new_list

