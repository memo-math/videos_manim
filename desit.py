from manim import *

#especificaciones para TikTok
SCALE_FACTOR = 1
#flip width => height, height => width
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16



class DesigualdadTriangular(Scene):
    def construct(self):
        # Título con degradado de colores
        titulo = Text("La desigualdad triangular", font_size=28)
        titulo.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Write(titulo))
        self.wait(5)
        self.play(FadeOut(titulo))

        # Ecuación de la desigualdad |a + b| <= |a| + |b|
        desigualdad = MathTex(r"|a + b| \leq |a| + |b|", font_size=25)
        self.play(Write(desigualdad))
        self.wait(8)

        # Mover la ecuación hacia arriba
        self.play(desigualdad.animate.shift(UP*2))

        # Definición de valor absoluto como función por partes
        definicion_valor_absoluto = MathTex(
            r"|a + b| = \begin{cases} a + b & \text{si } a + b \geq 0, \\ -(a + b) & \text{si } a + b < 0. \end{cases}", 
            font_size=25
        )
        definicion_valor_absoluto.next_to(desigualdad, DOWN)
        self.play(Write(definicion_valor_absoluto))
        self.wait(10)


        # Desigualdades a <= |a| y b <= |b|
        desigualdad_a = MathTex(r"a \leq |a|", font_size=25)
        desigualdad_b = MathTex(r"b \leq |b|", font_size=25)
        desigualdad_a.next_to(definicion_valor_absoluto, DOWN)
        desigualdad_b.next_to(desigualdad_a, DOWN)

        self.play(Write(desigualdad_a), Write(desigualdad_b))
        self.wait(10)
        desigualdad_a.shift(LEFT)
        desigualdad_b.shift(LEFT)
        self.wait(5)

        # Desigualdades -a <= |a| y -b <= |b|
        desigualdad_neg_a = MathTex(r"-a \leq |a|", font_size=25)
        desigualdad_neg_b = MathTex(r"-b \leq |b|", font_size=25)
        desigualdad_neg_a.next_to(desigualdad_a, RIGHT*2)
        desigualdad_neg_b.next_to(desigualdad_neg_a, DOWN)

        self.play(Write(desigualdad_neg_a), Write(desigualdad_neg_b))
        self.wait(5)

        # a + b centrado 
        a_mas_b = MathTex(r"a + b", font_size=25)
        a_mas_b.next_to(desigualdad_b, DOWN)
        parte_dos = MathTex(r"\leq a + |b|", font_size=25).next_to(a_mas_b, RIGHT)
        parte_tres = MathTex(r"\leq |a| + |b|", font_size=25).next_to(parte_dos, RIGHT)
        self.play(Write(a_mas_b))
        self.wait(5)
        self.play(Write(parte_dos))
        self.wait(5)
        self.play(Write(parte_tres))
        self.wait(5)

        # -(a+b) centrado
        menos_a_mas_b = MathTex(r"-(a + b)", font_size=25).next_to(a_mas_b, DOWN).shift(LEFT+0.1)
        menos_a_menos_b = MathTex(r"=-a - b", font_size=25).next_to(menos_a_mas_b, RIGHT)
        menos_parte_dos = MathTex(r"\leq -a + |b|", font_size=25).next_to(menos_a_menos_b, RIGHT)
        menos_parte_tres = MathTex(r"\leq |a| + |b|", font_size=25).next_to(menos_parte_dos, DOWN)
        self.play(Write(menos_a_mas_b))
        self.wait(5)
        self.play(Write(menos_a_menos_b))
        self.wait(5)
        self.play(Write(menos_parte_dos))
        self.wait(5)
        self.play(Write(menos_parte_tres))
        self.wait(5)

        # Enmarcar |a + b| en la definición de valor absoluto
        rectangulo_valor_absoluto = SurroundingRectangle(definicion_valor_absoluto[0][0:5], color=BLUE, buff=0.1)
        self.play(Create(rectangulo_valor_absoluto))
        self.wait(3)

        # Enmarcar a + b en la desigualdad larga
        rectangulo_a_mas_b = SurroundingRectangle(a_mas_b[0][::], color=BLUE, buff=0.1)
        self.play(Create(rectangulo_a_mas_b))
        self.wait(3)

        # Enmarcar |a| + |b| en la desigualdad larga
        rectangulo_valor_absoluto_b = SurroundingRectangle(parte_tres[0][::], color=BLUE, buff=0.1)
        self.play(Create(rectangulo_valor_absoluto_b))
        self.wait(3)

        # Enmarcar -a - b en la desigualdad larga
        rectangulo_a_mas_b = SurroundingRectangle(menos_a_menos_b[0][::], color=BLUE, buff=0.1)
        self.play(Create(rectangulo_a_mas_b))
        self.wait(3)

        # Enmarcar |a| + |b| en la desigualdad larga
        rectangulo_valor_absoluto_b = SurroundingRectangle(menos_parte_tres[0][::], color=BLUE, buff=0.1)
        self.play(Create(rectangulo_valor_absoluto_b))
        self.wait(3)

        #Enmarcar la desigualdad del triangulo en ROJO
        rectangulo_principal = SurroundingRectangle(desigualdad[0][::], color=BLUE, buff=0.1)
        self.play(Create(rectangulo_principal))
        self.wait(3)

        
