# Animación Interactiva de Caída Libre con Manim y Streamlit

<p align="center"><img src="/CaidaLibre_ManimCE_v0.19.0.gif" /></p>

## Descripción

Este proyecto implementa una animación interactiva de caída libre utilizando las bibliotecas **Manim** y **Streamlit**. La app permite modificar la **altura inicial** del objeto en caída libre de manera interactiva, mostrando los gráficos de **posición**, **velocidad** y **aceleración** en tiempo real, junto con un reloj que muestra el tiempo transcurrido.

La aplicación se divide en tres módulos principales:

1. **ejes.py**: Contiene funciones para crear los ejes coordenados y las gráficas de posición, velocidad y aceleración vs tiempo.
2. **reloj.py**: Implementa un reloj analógico que se actualiza en tiempo real durante la animación.
3. **main.py**: Combina los componentes para crear la animación principal de caída libre y permite la interacción del usuario con Streamlit.
4. **streamlit_app.py**: El archivo principal de la aplicación interactiva que utiliza **Streamlit** para permitir la modificación de la altura y la selección de la calidad de la animación de manera sencilla. También genera el archivo `altura.txt` y muestra el video resultante.

## Características Principales

- Animación interactiva de caída libre con ajuste de altura en tiempo real.
- Tres gráficos sincronizados:
  - **Posición vs tiempo (y vs t)**
  - **Velocidad vs tiempo (v vs t)**
  - **Aceleración vs tiempo (a vs t)**
- Reloj analógico que muestra el tiempo transcurrido.
- Trazas que se dibujan en tiempo real en los gráficos.
- Configuración interactiva de parámetros a través de **Streamlit**.
- Generación dinámica de videos en **baja**, **media** o **alta** calidad.

## Requisitos

- Python 3.7+
- Manim Community Edition
- Streamlit

## Instalación

Para ejecutar este proyecto, primero debes instalar las dependencias necesarias. Asegúrate de tener Python 3.7 o superior.

1. Clona este repositorio o descárgalo.
2. Instala las dependencias:

   ```bash
   pip install manim streamlit
   ```
## Ejecución
Para ver la animación directamente en Streamlit, ejecuta el siguiente comando en la terminal:

```bash
streamlit run streamlit_app.py
```

La app de Streamlit abrirá una interfaz en un navegador donde podrás modificar la altura inicial del objeto en caída libre. Los gráficos se actualizarán en tiempo real y podrás generar un video de la animación con la calidad que elijas.

Selecciona la calidad del video desde las opciones de calidad y presiona el botón Generar animación. El video generado aparecerá en la página.

## Estructura del Proyecto

├── streamlit_app.py # La aplicación interactiva en Streamlit 
├── main.py # Lógica principal de la animación de caída libre 
├── ejes.py # Funciones para crear los ejes de los gráficos 
├── reloj.py # Implementación del reloj que se actualiza en tiempo real 
├── altura.txt # Archivo con la altura inicial de la caída
├── ball.png # Archivo con la imagen del objeto
├── LICENSE # Licencia
└── README.md # Este archivo con la documentación del proyecto

## Licencia

Este proyecto está disponible bajo la licencia MIT.
