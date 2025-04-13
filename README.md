# Animación de Caída Libre con Manim

<p align="center"><img src ="/CaidaLibre_ManimCE_v0.19.0.gif" /></p>

## Descripción

Este proyecto implementa una animación de caída libre utilizando la biblioteca Manim, dividida en tres módulos principales:

1. **ejes.py**: Contiene funciones para crear ejes coordenados y gráficas de posición, velocidad y aceleración vs tiempo.
2. **reloj.py**: Implementa un reloj analógico que se actualiza en tiempo real durante la animación.
3. **main.py**: Combina los componentes para crear la animación principal de caída libre.

## Características Principales

- Animación física realista de un objeto en caída libre
- Tres gráficos sincronizados:
  - Posición vs tiempo (y vs t)
  - Velocidad vs tiempo (v vs t)
  - Aceleración vs tiempo (a vs t)
- Reloj analógico que muestra el tiempo transcurrido
- Trazas que se dibujan en tiempo real en los gráficos

## Requisitos

- Python 3.7+
- Manim Community

## Estructura del Código

### Módulo ejes.py

Contiene tres funciones para crear sistemas de ejes:

1. `crear_ejes_y_vs_t(t_max, h_real)`: Crea ejes para posición vs tiempo
   - Eje x: tiempo (0 a t_max)
   - Eje y: posición (0 a h_real)
   - Color amarillo

2. `crear_ejes_v_vs_t(t_max, g, y_vs_t_axes)`: Crea ejes para velocidad vs tiempo
   - Eje x: tiempo (0 a t_max)
   - Eje y: velocidad (negativa, proporcional a g*t_max)
   - Color naranja

3. `crear_ejes_a_vs_t(t_max, g)`: Crea ejes para aceleración vs tiempo
   - Eje x: tiempo (0 a t_max)
   - Eje y: aceleración (-g a 0)
   - Color azul

Cada función devuelve un VGroup que contiene los ejes y una grilla decorativa.

### Módulo reloj.py

Implementa la clase `Reloj` que muestra:
- Manecilla de segundos (roja)
- Manecilla de centésimas (azul)
- Números del 1 al 12 como marcadores horarios

El reloj se actualiza automáticamente usando un ValueTracker para seguir el tiempo de la simulación.

### Módulo main.py

Clase principal `CaidaLibre` que:
1. Configura parámetros físicos (altura inicial, gravedad, tiempo máximo)
2. Crea la pelota con rotación proporcional a la velocidad
3. Instancia el reloj
4. Crea los tres sistemas de ejes
5. Implementa puntos móviles y trazas para cada gráfico
6. Ejecuta la animación principal

## Cómo Ejecutar

1. Instalar las dependencias:
   ```
   pip install manim
   ```

2. Ejecutar la animación:
   ```
   manim -pql main.py CaidaLibre
   ```

   (Para renderizado de mayor calidad, usar `-pqh` o `-pqm` en lugar de `-pql`)

## Personalización

Puedes modificar los siguientes parámetros en main.py:
- `h_real`: Altura inicial del objeto
- `g`: Aceleración gravitatoria
- `y_top`: Posición vertical inicial de la pelota en la pantalla
- `y_bottom`: Posición vertical final de la pelota en la pantalla

## Notas

- Se asume la existencia de una imagen "ball.png" para representar la pelota
- La duración de la animación se calcula automáticamente según las ecuaciones de caída libre
- Todos los gráficos están sincronizados con el tiempo real de la simulación

## Licencia

Este proyecto está disponible bajo la licencia MIT.
