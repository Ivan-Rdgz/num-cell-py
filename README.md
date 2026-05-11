# num-cell-py

Este proyecto consiste en una librería de Python diseñada para la detección y el conteo automático de células en imágenes microscópicas mediante técnicas de preprocesamiento y segmentación de imágenes.

El proceso general (`main.py`) incluye:
1. **Conversión a escala de grises:** Preparación de la imagen.
2. **Filtro pasa bajas (Frecuencia):** Suavizado de la imagen para reducir ruido usando la Transformada de Fourier.
3. **Corrección Gamma:** Ajuste de intensidad y contraste.
4. **Umbralización:** Binarización de la imagen para separar las células del fondo.
5. **Segmentación y limpieza:** Uso de convoluciones para limpiar la máscara binaria.
6. **Componentes conectados:** Detección, filtrado por área y conteo de las células.

## Estructura del Proyecto

* `main.py`: Script principal que ejecuta el flujo completo de visión sobre una imagen de prueba.
* `cell_counter/`: Paquete principal del proyecto.
  * `data.py`: Módulo para cargar las diferentes imágenes de prueba (sangre, cebolla, ADN, etc.).
  * `preprocesar.py`: Funciones de preprocesamiento (Filtro pasa bajas en dominio de la frecuencia, intensidad gamma, filtro Sobel).
  * `segmentacion.py`: Funciones para umbralizar, limpiar la imagen segmentada y contar los componentes conectados.
* `data/`: Carpeta que contiene las imágenes de muestra.

## Requisitos

Las dependencias principales del proyecto son:
* `opencv-python` (cv2)
* `numpy`
* `scipy`
* `matplotlib` (para visualización)

## Instalación y uso

El proyecto está estructurado como paquete de Python, permitiendo usar sus funciones de procesamiento en cualquier otro script.

1. Instalar la librería.
    ```bash
   pip install git+https://github.com/Ivan-Rdgz/num-cell-py.git
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install opencv-python numpy scipy matplotlib
   ```
3. Importar la librería y matplotlib.pyplot para la visualización
   ```bash
   import cell_counter
   import matplotlib.pyplot as plt
   ```
4. Aplicar la funcion `cell_counter` a cualquier imagen de `data`
   ```bash
   img = cell_counter.data.blood()
   ```
 **Para cambiar de imágenes:** Sustituir la línea `img = cell_counter.data.blood()` por la función correspondiente a la imagen que desees. Todas las funciones de carga están definidas en el archivo `cell_counter/data.py` y las opciones disponibles son: `blood()`, `chlorella()`, `animal()`, `onion_1()` a `onion_7()`, `monocytes()`, `stem()`, `tissue()`, `dna()`, y `human()`.

5. Definir el conteo y la imagen con `count_cells` 
   ```bash
   conteo, img = cell_counter.count_cells(img)
   ```

6. Plotear 
   ```bash
   plt.figure(1)
   plt.imshow(img)
   plt.show()
   ```

   Esto procesará la imagen por defecto (células sanguíneas) y mostrará una ventana con los resultados del conteo y las células resaltadas en un rectangulo.

### Ejemplo de uso 
   ```bash
   import cell_counter
   import matplotlib.pyplot as plt

   img = cell_counter.data.blood()
   conteo, img = cell_counter.count_cells(img)

   plt.figure(1)
   plt.imshow(img)
   plt.show()

   ```

## Resultados
![Resultado del conteo de células de cebolla](/ejemplo_resultado.png)

## Autores
* Aaron Padilla Pizaña
* Daniela Rangel Quiroz 
* Iván de Jesús Rodríguez Flores 
* Rubén Uriel Sandoval de la Rosa 

 
