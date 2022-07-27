Proyecto para el curso de Python Inicial de Inove. Se procesarán archivos a elección del usuario

# Analisis de archivos csv de inflación y salarios en Argentina
### Integrantes
 - Lascours,  Nicolás
 - Knopoff, Iván
 
### Consideraciones generales
- Los archivos utilizados poseen una periodicidad que va desde:
    -Inflación: 2007 - 2021
    -Salarios: 2016 - 2021
- Por unicidad, se decidió que ambos archivos queden igualados en 2016 como año de inicio.

### Ejecución del programa
- Por consola se solicitarán datos para período de tiempo, año de inicio y de finalización del procesamiento, nombre de archivo de salida.
- Si no se ingresa ningún nombre, hay uno por default.
- El resultado final es un archivo csv con tres columnas:
    - Período (seleccionado por el usuario)
    - Índice de inflación promedio (en ese período)
    - Índice de salario promedio (en ese período)

### Origen de los datasets:
- Inflación: https://datos.gob.ar/is/dataset/sspm-expectativas-inflacion
- Salarios: https://datos.gob.ar/dataset/sspm-indice-salarios-base-octubre-2016/archivo/sspm_149.1
