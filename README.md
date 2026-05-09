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

1. Clonar el repositorio.
    ```bash
   git clone https://github.com/Ivan-Rdgz/num-cell-py.git
   ```
2. Instalar las dependencias necesarias:
   ```bash
   pip install opencv-python numpy scipy matplotlib
   ```
3. Ejecutar el script principal:
   ```bash
   python main.py
   ```
   Esto procesará la imagen por defecto (células sanguíneas) y mostrará una ventana con los resultados del conteo y las células resaltadas en un rectangulo.
   
4. **Para cambiar de imágenes:** Editar el archivo `main.py` y sustituye la línea `img = data.blood()` por la función correspondiente a la imagen que desees. Todas las funciones de carga están definidas en el archivo `cell_counter/data.py` y las opciones disponibles son: `blood()`, `chlorella()`, `animal()`, `onion_1()` a `onion_7()`, `monocytes()`, `stem()`, `tissue()`, `dna()`, y `human()`.

## Autores
* Aaron Padilla Pizaña
* Daniela Rangel Quiroz 
* Iván de Jesús Rodríguez Flores 
* Rubén Uriel Sandoval de la Rosa 

 
