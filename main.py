from manim import *
import numpy as np
from reloj import Reloj
from ejes import crear_ejes_y_vs_t, crear_ejes_v_vs_t, crear_ejes_a_vs_t

class CaidaLibre(Scene):
    def construct(self):

        # Leer la altura desde un archivo
        with open("altura.txt", "r") as f:
            h_real =  float(f.read())

        g = 9.8
        y_top = 3
        y_down = -3
        g1 = (y_top-y_down)*g/h_real
        t_max = np.sqrt(2 * (y_top-y_down) / g1)
        

        def position(t):
            return y_top - 0.5 * g1 * t ** 2
        def velocity(t):
            return -g * t
        def acceleration(t):
            return -g

        time_tracker = ValueTracker(0)

        # Pelota
        ball = ImageMobject("ball.png").scale(0.1).move_to(UP * 3)
        ball.add_updater(lambda m: m.move_to(UP * position(time_tracker.get_value())))
        self.add(ball)


        # Reloj
        reloj = Reloj(time_tracker)
        self.add(reloj)

        # Ejes y gráficos
        y_axes_group = crear_ejes_y_vs_t(t_max, h_real)
        y_axes = y_axes_group[0]  
        y_dot = Dot(color=YELLOW).scale(0.6)
        y_dot.add_updater(lambda m: m.move_to(y_axes.c2p(
            time_tracker.get_value(), h_real - 0.5*g*time_tracker.get_value()**2
        )))
        
        v_axes_group = crear_ejes_v_vs_t(t_max, g, y_axes)
        v_axes = v_axes_group[0]
        v_dot = Dot(color=ORANGE).scale(0.6)
        v_dot.add_updater(lambda m: m.move_to(v_axes.c2p(
            time_tracker.get_value(), velocity(time_tracker.get_value())
        )))
        
        a_axes_group = crear_ejes_a_vs_t(t_max, g)
        a_axes = a_axes_group[0]
        a_dot = Dot(color=BLUE).scale(0.6)
        a_dot.add_updater(lambda m: m.move_to(a_axes.c2p(
            time_tracker.get_value(), acceleration(time_tracker.get_value())
        )))

        # Crear trazas como VMobjects
        y_points = []
        y_trace = VMobject(color=YELLOW, stroke_width=3)
        y_trace.start_new_path(y_dot.get_center())
        
        v_points = []
        v_trace = VMobject(color=ORANGE, stroke_width=3)
        v_trace.start_new_path(v_dot.get_center())
        
        a_points = []
        a_trace = VMobject(color=BLUE, stroke_width=3)
        a_trace.start_new_path(a_dot.get_center())

        # Función de actualización para las trazas
        def update_traces(dt):
            y_points.append(y_dot.get_center())
            y_trace.set_points_as_corners(y_points)
            
            v_points.append(v_dot.get_center())
            v_trace.set_points_as_corners(v_points)
            
            a_points.append(a_dot.get_center())
            a_trace.set_points_as_corners(a_points)

        # Añadir todos los elementos a la escena
        self.add(
            y_axes_group,  # Esto incluye ejes + grillas
            Tex("y vs t", color=YELLOW).scale(0.7).move_to(3*UP+4.5*LEFT), 
            y_dot, y_trace,
            
            v_axes_group,  # Esto incluye ejes + grillas
            Tex("v vs t", color=ORANGE).scale(0.7).move_to(4.5*LEFT), 
            v_dot, v_trace,
            
            a_axes_group,  # Esto incluye ejes + grillas
            Tex("a vs t", color=BLUE).scale(0.7).move_to(3*DOWN+4.5*LEFT), 
            a_dot, a_trace
        )

        # Añadir el updater de las funciones
        self.add_updater(update_traces)

        # Animación principal
        self.play(time_tracker.animate.set_value(t_max), run_time=t_max, rate_func=linear)

        # Remover el updater de trazas
        self.remove_updater(update_traces)

        # Limpiar updaters
        y_dot.clear_updaters()
        v_dot.clear_updaters()
        a_dot.clear_updaters()
        ball.clear_updaters()

        # Punto en y vs t
        punto_y = Dot(color=YELLOW).scale(0.6).move_to(y_axes.c2p(t_max, 0))
        etiqueta_y = Tex(f"{h_real:.1f}", color=WHITE).scale(0.5)
        etiqueta_y.move_to(y_axes.c2p(-0.4, h_real))

        # Punto en v vs t
        v_final = velocity(t_max)
        punto_v = Dot(color=ORANGE).scale(0.6).move_to(v_axes.c2p(t_max, v_final))
        etiqueta_v = Tex(f"{v_final:.1f}", color=WHITE).scale(0.5)
        etiqueta_v.move_to(v_axes.c2p(-0.4, v_final))

        # Punto en a vs t (constante)
        a_final = acceleration(t_max)
        punto_a = Dot(color=BLUE).scale(0.6).move_to(a_axes.c2p(t_max, a_final))
        etiqueta_a = Tex(f"{a_final:.1f}", color=WHITE).scale(0.5)
        etiqueta_a.move_to(a_axes.c2p(-0.4, a_final))

        # Mostrar puntos y etiquetas
        self.play(
            FadeIn(punto_y), FadeIn(etiqueta_y),
            FadeIn(punto_v), FadeIn(etiqueta_v),
            FadeIn(punto_a), FadeIn(etiqueta_a)
        )


        # Mostrar tiempo calculado
        tiempo_texto = Text(f"Tiempo de caída: {t_max:.2f} s", font_size=20)
        tiempo_texto.to_corner(DR)
        self.play(Write(tiempo_texto))

        self.wait(2)