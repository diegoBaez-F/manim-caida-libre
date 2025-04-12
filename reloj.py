from manim import *

class Reloj(VGroup):
    def __init__(self, tiempo: ValueTracker, **kwargs):
        super().__init__(**kwargs)
        self.tiempo = tiempo

        reloj = Circle(radius=0.5, color=WHITE)
        punto_centro = Dot(ORIGIN, color=WHITE)
        self.segundero = Line(ORIGIN, 0.4 * UP, color=RED, stroke_width=4)
        self.cent_hand = Line(ORIGIN, 0.5 * UP, color=BLUE)

        for i in range(12):
            angulo = 60 * DEGREES - i * 30 * DEGREES
            numero = Text(str(i + 1), color=WHITE).scale(0.2)
            numero.move_to(0.6 * np.array([np.cos(angulo), np.sin(angulo), 0]))
            reloj.add(numero)

        self.add(reloj, punto_centro, self.segundero, self.cent_hand)
        self.to_corner(UP + RIGHT)

        self.agregar_updaters()

    def agregar_updaters(self):
        self.segundero.add_updater(lambda mob: mob.set_angle(
            90 * DEGREES - 360 * ((self.tiempo.get_value() % 60) / 60) * DEGREES
        ))
        self.cent_hand.add_updater(lambda mob: mob.set_angle(
            90 * DEGREES - 360 * (((self.tiempo.get_value() * 100) % 100) / 100) * DEGREES
        ))
