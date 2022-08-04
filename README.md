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
- El programa muestra la evolución de las expectativas de inflación y del salario mínimo vital y móvil en los períodos 2016-2021, y la relación entre ambas. Se puede obtener una síntesis trimestral, semestral o anual del período de años escogido por el usuario.
- Por consola se solicitarán datos necesarios junto al nombre de salida del archivo; si no se ingresa ningún nombre, hay uno por default.
- Cada dato solicitado es validado pertinentemente, junto a la opción de terminar el programa oprimiendo "0".
- Una vez realizado esto, se invoca al "handler" que procede al procesamiento de la información.
- Si es la primera vez que se ejecuta, se crearán los archivos pre-procesados a partir de los dataset originales. Esto se realiza una única vez.
- Se procesa la información y el resultado final es un archivo csv con tres columnas:
    - Período (seleccionado por el usuario)
    - Índice de inflación promedio (en ese período)
    - Índice de salario promedio (en ese período)
![Diagrama de flujo](https://github.com/Ivanknop/proyectoInoveProcesamientoArchivos/blob/main/ejercicio%20inove.jpg)]

### Origen de los datasets:
- Expectativas de Inflación: https://datos.gob.ar/is/dataset/sspm-expectativas-inflacion
- Índice de salarios. Base octubre 2016. Valores mensuales: https://datos.gob.ar/dataset/sspm-indice-salarios-base-octubre-2016/archivo/sspm_149.1
