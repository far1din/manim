'''
To create animation run in terminal:
>>> manim -pql example.py [Class Name]

Ex:
>>> manim -pql example.py EX1

###

To create animation with transparent background (used for the functions):
>>> manim -pql example.py [Class Name] - t

Ex:
>>> manim -pql example.py EX1 -t
'''

from manim import *
import copy

class EX1(Scene):
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        equation = MathTex("x^3 + 9x^2 + 33x + 25 = 0")
        # equation[0][0].set_color(YELLOW)
        equation[0][3].set_color(RED)
        equation[0][7:9].set_color(GREEN_B)
        equation[0][11:13].set_color(ORANGE)
        equation.move_to((0, 1.8466167, 0))



        arrow = Arrow(start=UP, end=DOWN, color=YELLOW_A).next_to(equation, DOWN, buff=0.5)
        t = Text("Translate by 3").scale(0.5).next_to(arrow, RIGHT)
        t2 = MathTex("\\frac{b}{3a}").scale(0.8).next_to(t[10], RIGHT, buff=0.2)
        t2[0][0].set_color(RED)
        t2[0][3].set_color(YELLOW)
        t3 = MathTex("\\frac{9}{3}").scale(0.8).next_to(t[10], RIGHT, buff=0.2)
        t3[0][0].set_color(RED)
        

        tt = "\\left( x - \\frac{b}{3a} \\right)" # translated text
        equation_t_1 = MathTex(f"1{tt}^3 + 9{tt}^2 + 33{tt} + 25 = 0").next_to(arrow, DOWN, buff=0.5)
        equation_t_1[0][0].set_color(YELLOW)
        equation_t_1[0][7].set_color(YELLOW)
        equation_t_1[0][18].set_color(YELLOW)
        equation_t_1[0][30].set_color(YELLOW)

        equation_t_1[0][4].set_color(RED)
        equation_t_1[0][11].set_color(RED)
        equation_t_1[0][15].set_color(RED)
        equation_t_1[0][27].set_color(RED)
        
        equation_t_1[0][22:24].set_color(GREEN_B)
        
        equation_t_1[0][33:35].set_color(ORANGE)



        tt_1 = "\\left( x - \\frac{9}{3} \\right)" # translated text
        equation_t_2 = MathTex(f"{tt_1}^3 + 9{tt_1}^2 + 33{tt_1} + 25 = 0").next_to(arrow, DOWN, buff=0.5)

        equation_t_2[0][3].set_color(RED)
        equation_t_2[0][9].set_color(RED)
        equation_t_2[0][13].set_color(RED)
        equation_t_2[0][24].set_color(RED)
        
        equation_t_2[0][19:21].set_color(GREEN_B)
        
        equation_t_2[0][29:31].set_color(ORANGE)



        equation_t = MathTex(f"x^3 + 6x = 20").next_to(arrow, DOWN, buff=0.5)
        equation_t[0][3].set_color(BLUE)
        equation_t[0][6:8].set_color(PURPLE)
      

        ### INFO: VIDEO ###
        self.wait(1)
        self.play(Write(equation))

        self.wait(1)
        self.play( 
            Write(arrow),
            Write(VGroup(t[0:11], t2, equation_t_1))
        )
        self.wait(1)

        self.play( 
            ReplacementTransform(equation_t_1, equation_t_2),
            ReplacementTransform(t2, t3),
        )
        self.wait(1)

        self.play( 
            ReplacementTransform(equation_t_2, equation_t),
            ReplacementTransform(t3, t[11]),
        )
        self.wait(1)

        self.play( 
            ShowPassingFlash( SurroundingRectangle(equation_t), time_width=0.5 ),
            Indicate(equation_t, scale_factor=1)
        )
        self.wait(1)


class EX2(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        equation = MathTex("x^3 + 9x^2 + 33x + 25 = 0").move_to((0, 1.8466167, 0))
        # equation[0][0].set_color(YELLOW)
        equation[0][3].set_color(RED)
        equation[0][7:9].set_color(GREEN_B)
        equation[0][11:13].set_color(ORANGE)
        arrow = Arrow(start=UP, end=DOWN, color=YELLOW_A).next_to(equation, DOWN, buff=0.5)
        t = Text("Translate by 3").scale(0.5).next_to(arrow, RIGHT)
        t2 = Text("Translate by -3").scale(0.5).next_to(arrow, RIGHT)
        

        equation_t = MathTex(f"x^3 + 6x = 20").next_to(arrow, DOWN, buff=0.5)
        equation_t[0][3].set_color(BLUE)
        equation_t[0][6:8].set_color(PURPLE)
        arrow_2 = Arrow(start=UP, end=DOWN, color=YELLOW_A).next_to(equation_t, DOWN, buff=0.5)



        x_solution = MathTex(
            "x = "
            " \\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } } ",
            "-"
            "\\frac{m}{3\\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } }}"
         ).set_color(YELLOW_A).next_to(arrow_2, DOWN, buff=0.5)
        x_solution[0][5].set_color(PURPLE)
        x_solution[0][11].set_color(PURPLE)
        x_solution[1][7].set_color(PURPLE)
        x_solution[1][13].set_color(PURPLE)

        x_solution[0][16].set_color(BLUE)
        x_solution[1][1].set_color(BLUE)
        x_solution[1][18].set_color(BLUE)

        x_solution_1 = MathTex(
            "x =  \\sqrt[3]{ \\frac{20}{2} \\pm  \\sqrt{ \\frac{20^2}{4} + \\frac{6^3}{27} } } - \\frac{6}{3\\sqrt[3]{ \\frac{20}{2} \\pm  \\sqrt{ \\frac{20^2}{4} + \\frac{6^3}{27} } }}").set_color(YELLOW_A).next_to(arrow_2, DOWN, buff=0.5)
        x_solution_1[0][5:7].set_color(PURPLE)
        x_solution_1[0][12:14].set_color(PURPLE)
        x_solution_1[0][30:32].set_color(PURPLE)
        x_solution_1[0][37:39].set_color(PURPLE)

        x_solution_1[0][18].set_color(BLUE)
        x_solution_1[0][24].set_color(BLUE)
        x_solution_1[0][43].set_color(BLUE)

        axes = NumberLine(
            x_range=[-3, 3, 1],
            length=10,
            include_numbers=True,
            label_direction=DOWN,
        ).set_opacity(0.7).scale(0.9).next_to(arrow_2, DOWN, buff=0.5).shift(DOWN*0.3)
        
        zp1 = Dot(color=RED, radius=.1).move_to(axes.number_to_point(2)).set_z_index(2)


        x_2 = MathTex(", \\quad x = 2").next_to(equation_t, RIGHT).shift(DOWN*0.08)
        x_2[0][1].set_color(RED)

        x_m1 = MathTex(", \\quad x = -1").next_to(equation, RIGHT).shift(DOWN*0.08)
        x_m1[0][1].set_color(YELLOW)


        ### INFO: VIDEO ###
        self.add(equation, arrow, t, equation_t)

        self.wait(1)
        self.play(
            Write(arrow_2),
            Write(x_solution),
            self.camera.frame.animate.move_to(arrow_2.get_center()).shift(DOWN)
        )
        self.wait(1)

        self.play(
            Unwrite(x_solution, reverse=False),
            Write(x_solution_1, reverse=False),
        )
        self.wait(1)

        self.play( 
            Write(axes),
            ReplacementTransform(x_solution_1, zp1)
        )
        self.wait(1)

        self.play( 
            self.camera.frame.animate.move_to(equation_t.get_center()).set_height( VGroup(equation, arrow, equation_t, arrow_2).height*1.7 ),
            ReplacementTransform(copy.deepcopy(zp1), x_2)
        
        )
        self.wait(1)

        self.play( 
            Write(x_m1[0][0:3]),

            FadeOut(arrow_2),
            VGroup(equation, x_m1[0][0:3]).animate.move_to(ORIGIN).next_to(arrow, UP, buff=0.5),
            VGroup(axes, zp1).animate.next_to(arrow, DOWN, buff=0.5),
            self.camera.frame.animate.move_to(arrow.get_center()).set_height( VGroup(equation, arrow, equation_t, arrow_2).height * 1.3 ),
            FadeOut(equation_t, x_2)
        )
        self.wait(1)

        self.play( 
            ShowPassingFlash( SurroundingRectangle(t), time_width=0.5 ) ,
            Indicate( t, scale_factor=1 ) ,
        )
        self.wait(1)

        self.play( 
            arrow.animate.rotate(180*DEGREES),
            Unwrite(t, reverse=False),
            Write(t2),

            # FadeOut(arrow_2),
            # VGroup(equation, x_m1[0][0:3]).animate.move_to(ORIGIN).next_to(arrow, UP, buff=0.5),
            # VGroup(axes, zp1).animate.next_to(arrow, DOWN, buff=0.5),
            # self.camera.frame.animate.move_to(arrow.get_center()).set_height( VGroup(equation, arrow, equation_t, arrow_2).height * 1.3 ),
            # FadeOut(equation_t, x_2)
        )
        self.wait(1)

        x_m1[0][3:5].next_to(x_m1[0][2], RIGHT)
        zp_sol = Dot(color=YELLOW, radius=.1).move_to(axes.number_to_point(-1)).set_z_index(2)
        self.play( 
            ReplacementTransform(zp1, zp_sol)
        )
        self.wait(1)

        self.play( 
            Write(x_m1[0][3:5]),
            ReplacementTransform(copy.deepcopy(zp_sol), copy.deepcopy(x_m1[0][3:5])),

            self.camera.frame.animate.move_to(x_m1[0][1:5].get_center()).set_width( x_m1[0][1:5].width * 1.7 ),

        )
        self.wait(1)
