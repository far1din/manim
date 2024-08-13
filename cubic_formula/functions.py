'''
To create animation run in terminal:
>>> manim -pql functions.py [Class Name]

Ex:
>>> manim -pql functions.py F1

###

To create animation with transparent background (used for the functions):
>>> manim -pql functions.py [Class Name] - t

Ex:
>>> manim -pql functions.py F1 -t
'''

from manim import *
import copy

# info: 2D TEXT ANIMATION (MERGE TOGETHER WITH 3D ANIMATIONS IN VIDEO EDITOR...)
# SCENES FOR GENERAL SOLUTION
class F1(Scene):
    # info: pass in -t in the terminal to get transparent background
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        f = MathTex("x", "^3", "+", "m", "x", "=", "n")
        f[0:2].set_color(YELLOW)
        f[3:5].set_color(BLUE)
        f[6].set_color(PURPLE)

        x_3 = MathTex("x^3")
        _6x = MathTex("mx").next_to(x_3, RIGHT, buff=3)
        

        VGroup(x_3, _6x).move_to(ORIGIN).set_opacity(.7).set_color(BLACK)
        _6x.shift(RIGHT)    


        ## VIDEO ###
        self.wait(1)
        self.play( Write(f) )
        self.wait(3)
        self.play( 
            Indicate(f[3], scale_factor=1),
            Indicate(f[6], scale_factor=1),
            ShowPassingFlash(SurroundingRectangle(f[3], color=BLUE ), time_width=.5),
            ShowPassingFlash(SurroundingRectangle(f[6], color=PURPLE ), time_width=.5),
        )
        self.wait(4)

        self.play( 
            Indicate(f[0:2], scale_factor=1, color=YELLOW_D),
            ShowPassingFlash(SurroundingRectangle(f[0:2], color=RED ), time_width=.5),
        )
        self.wait(1)
 
        self.play( 
            Indicate(f, color=RED, scale_factor=1),
        )
        self.wait(3)
        
        self.play( f.animate.to_edge(UP + RIGHT) )
        self.wait(4)

        self.play( ShowPassingFlash(SurroundingRectangle(f[0:2]), time_width=.5) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(f[3:5], color=BLUE), time_width=.5) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(f[6], color=PURPLE), time_width=.5) )
        self.wait(1)

        self.play( Write(x_3) )
        self.wait(1)
        self.play( Write(_6x) )
        self.wait(1)

        self.play( ReplacementTransform(VGroup(x_3, _6x), f[0:5]) )
        self.wait(5)

        t_u_m = MathTex("t", " \\cdot", "u", "=", "m" ).set_color(BLUE).next_to(f, DOWN, buff=.5).to_edge(RIGHT)
        self.play(Write(t_u_m[0:4]))
        self.wait(1)
        self.play(Write(t_u_m[4]))
        self.wait(5)
        


        t_equals = MathTex("t", "=", "x", "+", "\\frac{u}{", "3}", ", \\quad").next_to(f, LEFT, buff=.5)
        self.play(Write(t_equals[0:2]))
        self.wait(1)
        self.play(Write(t_equals[2:7]))
        self.wait(1)


        complete_cube_eq = MathTex( "t", "^3", "-", "\\left(", "\\frac{u}{", "3} \\right)^3", "=", "n" ).next_to(t_u_m, DOWN, buff=.5).to_edge(RIGHT)
        complete_cube_eq[3:6].set_color(RED)
        complete_cube_eq[7].set_color(PURPLE)

        self.play(Write(complete_cube_eq[0:2]))
        self.wait(1)
        self.play(Write(complete_cube_eq[2]))
        self.wait(1)
        self.play(Write(complete_cube_eq[3:6]))
        self.wait(2)

        self.play( ShowPassingFlash(SurroundingRectangle(f[0:2]), time_width=.5) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(f[3:5], color=BLUE), time_width=.5) )
        self.wait(1)
        self.play( 
            ShowPassingFlash(SurroundingRectangle(f), time_width=1), 
            Write(complete_cube_eq[6:8]),
         )
        self.wait(1)


        self.play(
            Indicate(t_u_m[0], scale_factor=1.05),
            Indicate(complete_cube_eq[0], scale_factor=1.05),
            run_time=.5

        )
        self.play(
            Indicate(t_u_m[2], scale_factor=1.05),
            Indicate(complete_cube_eq[4][0], scale_factor=1.05),
            run_time=.5
        )
        self.wait(1)
        self.play( 
            ShowPassingFlash(SurroundingRectangle(complete_cube_eq, color=RED_E), time_width=.5),
            ShowPassingFlash(SurroundingRectangle(t_u_m, color=RED_E), time_width=.5),
        )
        self.wait(1)


        t_u_x = MathTex("t, \\quad", "u, \\quad", "x")
        self.play(
            Write(t_u_x[0]),
            Indicate(t_u_m[0], scale_factor=1.05, color=YELLOW_E),
            Indicate(complete_cube_eq[0], scale_factor=1.05, color=YELLOW_E),
            Indicate(t_equals[0], scale_factor=1.05, color=YELLOW_E),
            run_time=.5

        )
        self.wait(1)
        self.play(
            Write(t_u_x[1]),
            Indicate(t_u_m[2], scale_factor=1.05),
            Indicate(complete_cube_eq[4][0], scale_factor=1.05),
            Indicate(t_equals[4][0], scale_factor=1.05),
            run_time=.5
        )
        self.wait(1)
        self.play(
            Write(t_u_x[2]),
            Indicate(f[0], scale_factor=1.05, color=RED_E),
            Indicate(f[4], scale_factor=1.05, color=RED_E),
            Indicate(t_equals[2], scale_factor=1.05, color=RED_E),
            run_time=.5
        )
        self.wait(3)


        self.play( 
            Unwrite(t_u_x, reverse=False),
            complete_cube_eq.animate.move_to(ORIGIN),
            t_u_m.animate.to_edge(LEFT + UP),
            t_equals[0:6].animate.move_to(ORIGIN).to_edge(UP),
            FadeOut(t_equals[6]),
         )
        self.wait(1)

class F2(MovingCameraScene):
    # info: pass in -t in the terminal to get transparent background
    def construct(self):
        self.camera.frame.save_state()

        f = MathTex("x", "^3", "+", "m", "x", "=", "n").to_edge( RIGHT + UP )
        f[0:2].set_color(YELLOW)
        f[3:5].set_color(BLUE)
        f[6].set_color(PURPLE)

        t_u_m = MathTex("t",  "\\cdot", "u", "= m").set_color(BLUE).to_edge(LEFT + UP)
        t_x_u_3 = MathTex("t", "=", "x", "+", "\\frac{u}{", "3}").move_to(ORIGIN).to_edge(UP)
        complete_cube_eq = MathTex( "t", "^3", "-", "\\left(", "\\frac{u}{", "3} \\right)^3", "=", "n" )
        complete_cube_eq[3:6].set_color(RED_E)
        complete_cube_eq[7].set_color(PURPLE)

        self.add(f, t_u_m, t_x_u_3, complete_cube_eq)

        ### VIDEO ###
        self.wait(1)
        cc_eq_1 = MathTex( "t", "^3", "-", "\\frac{u^3}{", "27}", "=", "n", "\\quad  \\left| \\cdot", "27" ) # complete cube equation 1
        cc_eq_1[3:5].set_color(RED)
        cc_eq_1[6].set_color(PURPLE)
        cc_eq_1[8].set_color(RED)
        
        self.play( ReplacementTransform(complete_cube_eq, cc_eq_1[0:7]) )
        self.wait(1)
        self.play( Write( cc_eq_1[7:9] ) )
        self.wait(1)
        self.play( ShowPassingFlash( SurroundingRectangle(cc_eq_1[4]), time_width=.5 ) )
        self.wait(1)
        

        cc_eq_2 = MathTex( "27", "t", "^3", "-", "u", "^3", "=", "27n" ) # complete cube equation 1
        self.play( ReplacementTransform( cc_eq_1, cc_eq_2 ) )
        self.wait(1)
        self.play( 
            ShowPassingFlash( SurroundingRectangle(cc_eq_2[1]), time_width=.5 ),
            ShowPassingFlash( SurroundingRectangle(cc_eq_2[4]), time_width=.5 )
        )
        self.wait(1)
        self.play( 
            ShowPassingFlash( SurroundingRectangle(cc_eq_2), time_width=.5 ),
            ShowPassingFlash( SurroundingRectangle(t_u_m), time_width=.5 )
        )
        self.wait(1)
        self.play( 
            Indicate( cc_eq_2, scale_factor=1.005, color=YELLOW_E ),
            self.camera.frame.animate.move_to(cc_eq_2.get_center()).set_width(cc_eq_2.width * 2)
        )
        self.wait(1)
        
        self.play( 
            self.camera.frame.animate.move_to(t_u_m.get_center()),
            ShowPassingFlash( SurroundingRectangle(t_u_m, color=YELLOW_E), time_width=.5, lag_ratio=0.5 ),

        )
        self.wait(1)

        u_m_t = MathTex("u =", "\\frac{m}{t}").set_color(BLUE).to_edge(UP + LEFT)
        self.play( 
            ReplacementTransform( t_u_m, u_m_t ),
            self.camera.frame.animate.move_to(u_m_t.get_center())
        )
        self.wait(1)


        cc_eq_3 = MathTex( "27t", "^3", "-", "\\left(", "\\frac{m}{", "t} \\right)^3", "=", "27n" )
        cc_eq_3[3:6].set_color(BLUE)

        _6_t_copy = copy.deepcopy( cc_eq_3[3:6] )
        self.play( 
            ReplacementTransform( copy.deepcopy(u_m_t[1]), _6_t_copy), 
            Unwrite((cc_eq_2), reverse=False), 
            Write(cc_eq_3),
            self.camera.frame.animate.restore()
        )
        self.wait(1)
        self.remove(_6_t_copy)

###
        cc_eq_4 = MathTex( "27t", "^3", "-", "\\frac{m^3}{", "t^3}", "=", "27n", "\\quad  \\left| \\cdot", "t^3" )
        cc_eq_4[3:5].set_color(BLUE)
        cc_eq_4[8].set_color(BLUE)

        self.play( 
            ReplacementTransform( cc_eq_3, cc_eq_4[0:7] ),
            self.camera.frame.animate.move_to(cc_eq_4[0:7].get_center()).set_width(cc_eq_4[0:7].width * 1.5)
        )
        self.wait(1)
        self.play( 
            Write( cc_eq_4[7:9] ),
            self.camera.frame.animate.move_to(cc_eq_4.get_center()).set_width(cc_eq_4.width * 1.5)
        )
        self.wait(1)
        self.play( ShowPassingFlash( SurroundingRectangle(cc_eq_4[4]), time_width=.5 ) )
        self.wait(1)


        cc_eq_5 = MathTex( "27t", "^6", "-", "m^3", "=", "27nt^3" )
        self.play( ReplacementTransform( cc_eq_4, cc_eq_5 ) )
        self.wait(1)

        self.play(Indicate(cc_eq_5[5], color=YELLOW_E, scale_factor=1.01))
        self.wait(1)
        

        cc_eq_6 = MathTex( "27t", "^6", "-",  "27nt^3", "-", "m^3", "= 0" )
        self.play( 
            FadeOut(cc_eq_5[0:2], shift=LEFT), 
            FadeOut(cc_eq_5[2:4], shift=RIGHT), 
            FadeOut(cc_eq_5[4], shift=RIGHT), 
            FadeOut(cc_eq_5[5], shift=LEFT), 

            FadeIn(cc_eq_6[0:3]),
            FadeIn(cc_eq_6[3], shift=LEFT),
            Write(cc_eq_6[4]),
            FadeIn(cc_eq_6[5]),
            FadeIn(cc_eq_6[6], shift=RIGHT),
        )
        self.wait(1)

        self.play( 
            Indicate(cc_eq_6[1], color=RED, scale_factor=1.01),
            ShowPassingFlash( SurroundingRectangle(cc_eq_6[1], color=RED), time_width=.5 ),
            self.camera.frame.animate.restore()            
        )
        self.wait(1)

        k_t_3 = MathTex("k", "=", "t^3").next_to(u_m_t, DOWN, buff=.5).to_edge(LEFT)
        k_t_3[0].set_color(RED)
        self.play(Write(k_t_3))
        self.wait(1)


        cc_eq_k = MathTex( "27", "k", "^2", "-",  "27n", "k", "-", "m^3", "= 0" )
        cc_eq_k[1].set_color(RED)
        cc_eq_k[5].set_color(RED)
        self.play(
            ReplacementTransform(copy.deepcopy(k_t_3[0]), cc_eq_k[1]),
            ReplacementTransform(copy.deepcopy(k_t_3[0]), cc_eq_k[5]),
            FadeOut(cc_eq_6),
            Write(cc_eq_k[1]),
            Write(cc_eq_k[5]),
            FadeIn(cc_eq_k[0]),
            FadeIn(cc_eq_k[2:5]),
            FadeIn(cc_eq_k[6:9]),
        )
        self.wait(1)
        self.play( 
            Indicate(cc_eq_k[2], color=YELLOW_E, scale_factor=1.01),
            ShowPassingFlash( SurroundingRectangle(cc_eq_k[2], color=YELLOW_E), time_width=.5 ) 
        )
        self.wait(1)


        quadratic_formula = MathTex("k = \\frac{ -b \\pm \\sqrt{ b^2 - 4ac } }{2a}").next_to(cc_eq_k, DOWN, buff=1)
        quadratic_formula[0][0].set_color(RED)
        quadratic_formula[0][11].set_color(YELLOW)
        quadratic_formula[0][15].set_color(YELLOW)
        quadratic_formula[0][3].set_color(BLUE)
        quadratic_formula[0][7].set_color(BLUE)
        quadratic_formula[0][12].set_color(GREEN)

        self.play( Write(quadratic_formula) )
        self.wait(1)

        brace_a = Brace(cc_eq_k[0], UP, buff=.1).set_color(YELLOW)
        text_a = MathTex("a").set_color(YELLOW).next_to(brace_a, UP, buff=0.1)
        self.play( Create(VGroup(brace_a, text_a)) )
        self.wait(1)

        brace_b = Brace(cc_eq_k[3:5], UP, buff=.1).set_color(BLUE)
        text_b = MathTex("b").set_color(BLUE).next_to(brace_b, UP, buff=0.1)
        self.play( Create(VGroup(brace_b, text_b)) )
        self.wait(1)

        brace_c = Brace(cc_eq_k[6:8], UP, buff=.1).set_color(GREEN)
        text_c = MathTex("c").set_color(GREEN).next_to(brace_c, UP, buff=0.1)
        self.play( Create(VGroup(brace_c, text_c)) )
        self.wait(1)


        k_sol = MathTex("k", "=", "\\frac{27n \\pm \\sqrt{729n^2 + 108m^3} }{54}").next_to(cc_eq_k, DOWN, buff=1)
        k_sol[2][2].set_color(PURPLE)
        k_sol[2][9].set_color(PURPLE)

        k_sol[2][15].set_color(BLUE)

        k_sol[0].set_color(RED)

        self.play( ReplacementTransform(quadratic_formula, k_sol) )
        self.wait(1)
        self.play(
            k_sol.animate.move_to(ORIGIN), 
            FadeOut(cc_eq_k), 
            FadeOut(brace_a, text_a, brace_b, text_b, brace_c, text_c ),
            self.camera.frame.animate.move_to(ORIGIN).set_width(k_sol.width * 1.5)
        )
        self.wait(1)
        self.play( 
            ShowPassingFlash( SurroundingRectangle(k_sol[2][6:17], color=RED_C), time_width=.5 ),
            Indicate( k_sol[2][6:17], color=RED_C, scale_factor=1),
        )
        self.wait(1)

### 2

        k_sol_1 = MathTex("k", "=", "\\frac{27n \\pm \\sqrt{9(81n^2 + 12m^3)} }{54}")
        k_sol_1[2][2].set_color(PURPLE)
        k_sol_1[2][10].set_color(PURPLE)
        k_sol_1[2][15].set_color(BLUE)
        k_sol_1[0].set_color(RED)
        self.play( ReplacementTransform(k_sol, k_sol_1) )
        self.wait(1)


        k_sol_2 = MathTex("k", "=", "\\frac{27n \\pm \\sqrt{9} \\cdot \\sqrt{81n^2 + 12m^3} }{54}")
        k_sol_2[2][2].set_color(PURPLE)
        k_sol_2[2][12].set_color(PURPLE)
        k_sol_2[2][17].set_color(BLUE)
        k_sol_2[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_1, k_sol_2) )
        self.wait(1)


        k_sol_3 = MathTex("k", "=", "\\frac{27n \\pm 3 \\sqrt{81n^2 + 12m^3} }{54}")
        k_sol_3[2][2].set_color(PURPLE)
        k_sol_3[2][9].set_color(PURPLE)
        k_sol_3[2][14].set_color(BLUE)
        k_sol_3[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_2, k_sol_3) )
        self.wait(1)
        self.play( Indicate(k_sol_3[2][4], color=RED) )
        self.wait(1)


        k_sol_4 = MathTex("k", "=", "\\frac{9n \\pm \\sqrt{81n^2 + 12m^3} }{18}")
        k_sol_4[2][1].set_color(PURPLE)
        k_sol_4[2][7].set_color(PURPLE)
        k_sol_4[2][12].set_color(BLUE)
        k_sol_4[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_3, k_sol_4) )
        self.wait(1)


        k_sol_5 = MathTex("k", "=", "\\frac{9n}{18}", "\\pm", "\\frac{\\sqrt{81n^2 + 12m^3}}{", "18}")
        k_sol_5[2][1].set_color(PURPLE)
        k_sol_5[4][4].set_color(PURPLE)
        k_sol_5[4][9].set_color(BLUE)
        k_sol_5[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_4, k_sol_5) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(k_sol_5[2]), time_width=.5) )
        self.wait(1)

        n_2 = MathTex("\\frac{n}{2}").move_to(k_sol_5[2])
        n_2[0][0].set_color(PURPLE)
        self.play( Transform(k_sol_5[2], n_2) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(k_sol_5[4:6], color=RED), time_width=.5) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(k_sol_5[5], color=RED), time_width=.5) )
        self.wait(1)
        sqrt324 = MathTex("\\sqrt{324}").move_to(k_sol_5[5])
        self.play( Transform(k_sol_5[5], sqrt324) )
        self.wait(1)
        self.play( 
            ShowPassingFlash( SurroundingRectangle( k_sol_5[4], color=RED ), time_width=.5 ),
            ShowPassingFlash( SurroundingRectangle( k_sol_5[5], color=RED ), time_width=.5 )
        )
        self.wait(1)
        

        k_sol_6 = MathTex("k", "=", "\\frac{n}{2}", "\\pm", "\\sqrt{ \\frac{81n^2 + 12m^3}{324} }")
        k_sol_6[2][0].set_color(PURPLE)
        k_sol_6[4][4].set_color(PURPLE)
        k_sol_6[4][9].set_color(BLUE)
        k_sol_6[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_5, k_sol_6) )
        self.wait(1)
        

        k_sol_7 = MathTex("k", "=", "\\frac{n}{2}", "\\pm", "\\sqrt{ \\frac{81n^2}{324} + \\frac{12m^3}{324} }")
        k_sol_7[2][0].set_color(PURPLE)
        k_sol_7[4][4].set_color(PURPLE)
        k_sol_7[4][13].set_color(BLUE)
        k_sol_7[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_6, k_sol_7) )
        self.wait(1)
        

        k_sol_8 = MathTex("k", "=", "\\frac{n}{2}", "\\pm", "\\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} }")
        k_sol_8[2][0].set_color(PURPLE)
        k_sol_8[4][2].set_color(PURPLE)
        k_sol_8[4][7].set_color(BLUE)
        k_sol_8[0].set_color(RED)
        self.play( ReplacementTransform(k_sol_7, k_sol_8) )
        self.wait(2)
        self.play( 
            ShowPassingFlash(SurroundingRectangle(k_sol_8[0], color=RED_E), time_width=.5),
            self.camera.frame.animate.restore()
        )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(k_t_3, color=RED_E), time_width=.5) )
        self.wait(1)

        t_3_k = MathTex(",", "\\quad t = \\sqrt[3]{k}").next_to(k_t_3, RIGHT)
        t_3_k[1][5].set_color(RED)
        self.play( Write(t_3_k) )
        self.wait(1)
        self.play(t_3_k[1].animate.to_edge(LEFT), FadeOut(k_t_3, t_3_k[0]))
        self.wait(1)


        t_u_equals = MathTex(
            "t = \\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } }", 
            ", \\quad u = \\frac{m}{\\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } }}"
        ).shift(DOWN*.5)
        t_u_equals[0][5].set_color(PURPLE)
        t_u_equals[0][11].set_color(PURPLE)
        t_u_equals[0][16].set_color(BLUE)

        t_u_equals[1][3].set_color(BLUE)
        t_u_equals[1][8].set_color(PURPLE)
        t_u_equals[1][14].set_color(PURPLE)
        t_u_equals[1][19].set_color(BLUE)
        t_copy = copy.deepcopy(t_u_equals[0])
        t_u_equals[0].move_to(ORIGIN)
        self.play( Write(t_u_equals[0]), Unwrite(k_sol_8, reverse=False, run_rate=.5) )
        self.wait(1)
        self.play( ShowPassingFlash(SurroundingRectangle(u_m_t, color=BLUE), time_width=.5) )
        self.wait(1)
        self.play( t_u_equals[0].animate.move_to(t_copy), Write(t_u_equals[1]) )
        self.wait(1)
        self.play( ShowPassingFlash( SurroundingRectangle(t_x_u_3), time_width=.5 ) )
        self.wait(1)


        x_equals = MathTex("x", "=", "t", "-", "\\frac{u}{3}").to_edge(UP)
        self.play( Write( x_equals[0:2] ), Unwrite(t_x_u_3, reverse=False) )
        self.wait(1)
        self.play( Write( x_equals[2:5] ) )
        self.wait(1)


        x_solution = MathTex(
            "x = "
            " \\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } } ",
            "-"
            "\\frac{m}{3\\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } }}"
         ).set_color(YELLOW_A)
        x_solution[0][0].set_color(RED)
        x_solution[0][5].set_color(PURPLE)
        x_solution[0][11].set_color(PURPLE)
        x_solution[1][7].set_color(PURPLE)
        x_solution[1][13].set_color(PURPLE)

        x_solution[0][16].set_color(BLUE)
        x_solution[1][1].set_color(BLUE)
        x_solution[1][18].set_color(BLUE)
        self.play( 
            Write( x_solution ),
            FadeOut( t_u_equals, t_3_k, u_m_t, x_equals  ),
            f.animate.move_to(x_equals)
        )
        self.wait(3)
