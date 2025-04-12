from manim import *
import numpy as np

def crear_ejes_y_vs_t(t_max, h_real):
    axes = Axes(
        x_range=[0, t_max + 0.5, t_max],
        y_range=[-0.5, h_real + 0.5, h_real],
        x_length=2,
        y_length=2,
        axis_config={
            "color": YELLOW,
            "include_numbers": False,
            "stroke_width": 2
        },
        tips=False
    ).to_corner(UP + LEFT)
    
    # Crear grilla completa (horizontal y vertical)
    grid = VGroup()
    # Líneas verticales
    for x in np.linspace(0, t_max, 5):
        grid.add(Line(
            start=axes.c2p(x, -0.5, 0),
            end=axes.c2p(x, h_real + 0.5, 0),
            stroke_color=YELLOW,
            stroke_width=1,
            stroke_opacity=0.5
        ))
    # Líneas horizontales
    for y in np.linspace(-0.5, h_real + 0.5, 5):
        grid.add(Line(
            start=axes.c2p(0, y, 0),
            end=axes.c2p(t_max, y, 0),
            stroke_color=YELLOW,
            stroke_width=1,
            stroke_opacity=0.5
        ))
    
    return VGroup(axes, grid)

def crear_ejes_v_vs_t(t_max, g, y_vs_t_axes):
    v_min = -g * t_max
    axes = Axes(
        x_range=[0, t_max + 0.5, t_max],
        y_range=[v_min - 0.5, 0.5, v_min],
        x_length=2,
        y_length=2,
        axis_config={
            "color": ORANGE,
            "include_numbers": False,
            "stroke_width": 2
        },
        tips=False
    ).move_to(5.5*LEFT)
    
    # Grilla con énfasis en líneas horizontales
    grid = VGroup()
    # Líneas verticales (menos visibles)
    for x in np.linspace(0, t_max, 5):
        grid.add(Line(
            start=axes.c2p(x, v_min - 0.5, 0),
            end=axes.c2p(x, 0.5, 0),
            stroke_color=ORANGE,
            stroke_width=0.5,
            stroke_opacity=0.5
        ))
    # Líneas horizontales (más visibles)
    for y in np.linspace(v_min, 0, 5):
        grid.add(Line(
            start=axes.c2p(0, y, 0),
            end=axes.c2p(t_max, y, 0),
            stroke_color=ORANGE,
            stroke_width=1,
            stroke_opacity=0.5
        ))
    
    return VGroup(axes, grid)

def crear_ejes_a_vs_t(t_max, g):
    axes = Axes(
        x_range=[0, t_max + 0.5, t_max],
        y_range=[-g - 0.5, 0.5, -g],
        x_length=2,
        y_length=2,
        axis_config={
            "color": BLUE,
            "include_numbers": False,
            "stroke_width": 2
        },
        tips=False
    ).to_corner(DOWN + LEFT)
    
    # Grilla uniforme
    grid = VGroup()
    # Líneas verticales
    for x in np.linspace(0, t_max, 5):
        grid.add(Line(
            start=axes.c2p(x, -g - 0.5, 0),
            end=axes.c2p(x, 0.5, 0),
            stroke_color=BLUE,
            stroke_width=1,
            stroke_opacity=0.5
        ))
    # Líneas horizontales
    for y in np.linspace(-g, 0, 5):  # Menos líneas horizontales en este gráfico
        grid.add(Line(
            start=axes.c2p(0, y, 0),
            end=axes.c2p(t_max, y, 0),
            stroke_color=BLUE,
            stroke_width=1,
            stroke_opacity=0.5
        ))
    
    return VGroup(axes, grid)