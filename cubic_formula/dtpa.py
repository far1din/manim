'''
To create animation run in terminal:
>>> manim -pql dtpa.py [Class Name]

Ex:
>>> manim -pql dtpa.py DTPA1

###

To create animation with transparent background (used for the functions):
>>> manim -pql dtpa.py [Class Name] - t

Ex:
>>> manim -pql dtpa.py DTPA1 -t
'''

from manim import *
import copy


def f1(x):
    return x**3 + 3*x**2 - 6*x - 8


class DTPA1(Scene):
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        general_equation = MathTex("ax^3 + bx^2 + cx + d = 0")
        general_equation[0][0].set_color(PINK)
        general_equation[0][4].set_color(BLUE)
        general_equation[0][8].set_color(GREEN_B)
        general_equation[0][11].set_color(ORANGE)

        arrow = Arrow(start=UP, end=DOWN, color=YELLOW_A).next_to(general_equation, DOWN)

        dc_equation = MathTex("x^3 + mx = n").next_to(arrow, DOWN).set_color(YELLOW_A)
        dc_equation[0][3].set_color(BLUE)
        dc_equation[0][6].set_color(PURPLE)

        initial_functions = VGroup(general_equation, dc_equation, arrow).move_to(ORIGIN)

        ### INFO: VIDEO ###
        self.wait(1)

        self.play(Write(general_equation))
        self.wait(1)
        self.play(Write(arrow), Write(dc_equation))
        self.wait(1)


        f = MathTex("f(x) = ax^3 + bx^2 + cx + d").scale(.8).to_edge( UP + LEFT )
        f[0][0:4].set_color(YELLOW_C)
        f[0][0+5].set_color(PINK)
        f[0][4+5].set_color(BLUE)
        f[0][8+5].set_color(GREEN_B)
        f[0][11+5].set_color(ORANGE)
        self.play( ShowPassingFlash( SurroundingRectangle(general_equation[0][0:12]), time_width=.5 ) )
        self.wait(1)

        self.play( 
            Write(f),
            FadeOut(arrow, dc_equation)
        )
        self.wait(1)

        axes = Axes(
            x_range=[-7, 7],
            y_range=[-12, 12, 2],
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 27
            },
            tips=False,
        )

        plot = axes.plot(lambda x: ((x)**3 + 3*(x)**2 - 6*(x) - 8), color=YELLOW_C)


        self.play(
            Create(axes),
            Create(plot),
            general_equation.animate.to_edge(UP + RIGHT)
        )
        self.wait(1)


        zp1 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(-4, 0, 0)).set_z_index(2)
        ip = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(-1, 0, 0)).set_z_index(2)
        zp2 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(2, 0, 0)).set_z_index(2)

        self.play( ShowPassingFlash( SurroundingRectangle(general_equation), time_width=.5) ) 
        self.wait(1)

        self.play( ShowPassingFlash( SurroundingRectangle(f), time_width=.5) ) 
        self.wait(2)
        
        self.play( ReplacementTransform(general_equation, VGroup(zp1, zp2, ip)) ) 
        self.wait(1)


        # points_array = []
        # for i in range(260):
        #     x = -5 +i*.03
        #     y = f1(x)
        #     point = Dot(color=YELLOW, radius=.03).move_to(axes.coords_to_point(x, y, 0)).set_z_index(1.9)
        #     points_array.append(point)

        # points = VGroup(*points_array)

        # self.play( Indicate(plot, color=YELLOW_E, scale_factor=1) )
        # self.wait(1)
        # self.play( FadeOut(plot, run_time=.5), Create(points) )
        # self.wait(1)

class DTPA2(Scene):
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        general_equation = MathTex("ax^3 + bx^2 + cx + d = 0")
        general_equation[0][0].set_color(YELLOW)
        general_equation[0][4].set_color(RED)
        general_equation[0][8].set_color(GREEN_B)
        general_equation[0][11].set_color(ORANGE)

        arrow = Arrow(start=UP, end=DOWN, color=YELLOW_A).next_to(general_equation, DOWN)

        dc_equation = MathTex("x^3 + mx = n").next_to(arrow, DOWN).set_color(YELLOW_A)
        dc_equation[0][3].set_color(BLUE)
        dc_equation[0][6].set_color(PURPLE)

        f = MathTex("f(x) = ax^3 + bx^2 + cx + d").scale(.8).to_edge( UP + LEFT )
        f[0][0:4].set_color(YELLOW_C)
        f[0][0+5].set_color(PINK)
        f[0][4+5].set_color(BLUE)
        f[0][8+5].set_color(GREEN_B)
        f[0][11+5].set_color(ORANGE)

        axes = Axes(
            x_range=[-7, 7],
            y_range=[-12, 12, 2],
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 27
            },
            tips=False,
        )

        plot = axes.plot(lambda x: ((x)**3 + 3*(x)**2 - 6*(x) - 8), color=YELLOW_C)

        zp1 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(-4, 0, 0)).set_z_index(2)
        ip = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(-1, 0, 0)).set_z_index(2)
        zp2 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(2, 0, 0)).set_z_index(2)

        self.add(f, axes, plot, zp1, ip, zp2)

        ###* NEW *###

        g = MathTex("g(x) = f(x - \\frac{b}{3a})").scale(.8).next_to(f, DOWN).to_edge( LEFT ).set_color(YELLOW)
        g[0][0:4].set_color(RED)
        g[0][4].set_color(WHITE)
        g[0][9].set_color(BLUE)
        g[0][12].set_color(RED)

        plot_g = copy.deepcopy(plot).shift( axes.coords_to_point(1, 0, 0) ).set_color(RED)
        g_zero_points = copy.deepcopy( VGroup(zp1, ip, zp2) ).shift( axes.coords_to_point(1, 0, 0) ).set_color(YELLOW)


        ### INFO: VIDEO ###
        self.wait(1)
        
        self.play(
            FadeIn(plot_g, shift=RIGHT)
        )
        self.wait(1)

        self.play(
            Write(g),
        )
        self.wait(1)

        self.play( Create(g_zero_points) )
        self.wait(1)

        self.play(
            FadeOut(g_zero_points, VGroup(zp1, ip, zp2)),
            FadeOut(f),
            FadeOut(g),

            Uncreate(plot_g),
            Uncreate(plot),
        )
        self.wait(1)
        
class DTPA3(Scene):
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        axes = Axes(
            x_range=[-7, 7],
            y_range=[-12, 12, 2],
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 27
            },
            tips=False,
        )
        self.add(axes)

        def cubic(x, a, b, c, d):
            return a*x**3 + b*x**2 + c*x + d

        ### INFO: VIDEO ###
        a = ValueTracker(1)
        b = ValueTracker(0)
        c = ValueTracker(-5)
        d = ValueTracker(3)
        

        plot = always_redraw(lambda: axes.plot(lambda x: cubic(x, a.get_value(), b.get_value(), c.get_value(), d.get_value()), color=YELLOW_C))
        ip = always_redraw(lambda: Dot(color=BLUE, radius=.1).move_to(axes.coords_to_point(0, d.get_value(), 0)).set_z_index(2))

        
        ft1 = MathTex(f"f(x) = x^3 - 5x + 3").set_color(YELLOW_A).scale(.8).to_edge(UP + LEFT) 
        # info: Transformations
        self.play(
            Create(plot), 
            FadeIn(ip), 
            Write(ft1)
        )
        self.wait()

        ft2 = MathTex(f"f(x) = 3x^3 - 3x + 1").set_color(YELLOW_A).scale(.8).to_edge(UP + LEFT) 
        self.play(
            a.animate.set_value(3),
            c.animate.set_value(-3),
            d.animate.set_value(1),
            ReplacementTransform(ft1, ft2),

            run_time=1.5
        )
        ft3 = MathTex(f"f(x) = 4x^3 - 5x - 1").set_color(YELLOW_A).scale(.8).to_edge(UP + LEFT) 
        self.play(
            a.animate.set_value(4),
            c.animate.set_value(-5),
            d.animate.set_value(-1),
            ReplacementTransform(ft2, ft3),

            run_time=1.5
        )
        ft4 = MathTex(f"f(x) = x^3 - 8x").set_color(YELLOW_A).scale(.8).to_edge(UP + LEFT) 
        self.play(
            a.animate.set_value(1),
            c.animate.set_value(-8),
            d.animate.set_value(0),
            ReplacementTransform(ft3, ft4),

            run_time=1.5
        )
        ft5 = MathTex(f"f(x) = 2x^3 + x + 4").set_color(YELLOW_A).scale(.8).to_edge(UP + LEFT) 
        self.play(
            a.animate.set_value(2),
            c.animate.set_value(1),
            d.animate.set_value(4),
            ReplacementTransform(ft4, ft5),

            run_time=1.5
        )
        ft6 = MathTex(f"f(x) = 2x^3 - 5x + 3").set_color(YELLOW_A).scale(.8).to_edge(UP + LEFT) 
        self.play(
            a.animate.set_value(2),
            c.animate.set_value(-5),
            d.animate.set_value(3),
            ReplacementTransform(ft5, ft6),

            run_time=1.5
        )
        self.wait()

        self.play( Indicate(ip, color=BLUE_D), Flash(ip, color=BLUE) )
        self.wait()
        # info: Transformations

        ip_function = MathTex("f''(x) = 0").next_to(ft6, DOWN, buff=0.6).scale(0.8).to_edge(LEFT).set_color(BLUE_C)
        self.play( ReplacementTransform(ip, ip_function[0][0:6]) )
        self.wait()
        self.play( Write( ip_function[0][6:8] ) )
        self.wait()

        f2 = MathTex("f(x) = ax^3 + bx^2 + cx + d").scale(.8).to_edge( UP + LEFT )
        f2[0][0:4].set_color(YELLOW_C)
        f2[0][0+5].set_color(PINK)
        f2[0][4+5].set_color(BLUE)
        f2[0][8+5].set_color(GREEN_B)
        f2[0][11+5].set_color(ORANGE)
        self.play(
            a.animate.set_value(1),
            b.animate.set_value(3),
            c.animate.set_value(-6),
            d.animate.set_value(-8),

            ReplacementTransform(ft6, f2),
        )
        self.wait()

         
        f_dd = MathTex("f''(x) = 6ax + 2b = 0").scale(.8).move_to(ip_function).to_edge( LEFT )
        f_dd[0][0:6].set_color(YELLOW_C)
        f_dd[0][8].set_color(PINK)
        f_dd[0][12].set_color(BLUE)
        self.play( ReplacementTransform(ip_function, f_dd[0:13]) )
        self.wait()

         
        f_dd_1 = MathTex("6ax + 2b = 0").scale(.8).move_to(ip_function).to_edge( LEFT )
        f_dd_1[0][1].set_color(PINK)
        f_dd_1[0][5].set_color(BLUE)
        self.play( ReplacementTransform(f_dd, f_dd_1) )
        self.wait()

         
        x_eq = MathTex("x = - \\frac{b}{3a}").scale(.8).move_to(ip_function).to_edge( LEFT )
        x_eq[0][0].set_color(BLUE_D)
        x_eq[0][6].set_color(PINK)
        x_eq[0][3].set_color(BLUE)
        self.play( ReplacementTransform(f_dd_1, x_eq) )
        self.wait()

        ip_1 = Dot(color=BLUE_D, radius=.1).move_to(axes.coords_to_point(-1, 0, 0)).set_z_index(2)
        self.play( ReplacementTransform( copy.deepcopy(x_eq), ip_1 ) )
        self.wait()


        x_zero = MathTex("0").scale(0.8).move_to(x_eq[0][0])
        self.play( 
            ReplacementTransform( x_eq[0][0], x_zero ),
            Indicate(axes.y_axis, scale_factor=1, color=BLUE),
            
            VGroup(plot, ip_1).animate.shift( axes.coords_to_point(1, 0, 0) ),

            #FadeIn(plot_copy, shift=RIGHT)
            
        )
        plot_copy = copy.deepcopy(plot).shift( axes.coords_to_point(1, 0, 0) ) # fix the always redraw issue after shift..
        self.remove(plot)
        self.add(plot_copy)
        self.wait()

        b_zero = MathTex("0").scale(0.8).move_to(x_eq[0][3]).set_color(BLUE)
        self.play( 
            ReplacementTransform( x_eq[0][3], b_zero ),
            ShowPassingFlash( SurroundingRectangle( x_eq[0][3], color=RED ), time_width=0.5 )
        )
        self.wait()


        b_zero_1 = MathTex("0").scale(0.8).move_to(f2[0][9]).set_color(BLUE)
        self.play( 
            ReplacementTransform( f2[0][9], b_zero_1 ),
            FadeOut( copy.deepcopy(b_zero), shift=UP+RIGHT )
        )
        self.wait()


        self.play( ShowPassingFlash( SurroundingRectangle( f2[0][9:12], color=RED ), time_width=0.5 ) )
        self.wait()


        f3 = MathTex("f(x) = ax^3 + cx + d").scale(.8).to_edge( UP + LEFT )
        f3[0][0:4].set_color(YELLOW_C)
        f3[0][0+5].set_color(PINK)
        f3[0][9].set_color(GREEN_B)
        f3[0][12].set_color(ORANGE)

        self.play( 
            ReplacementTransform( f2, f3 ),
            FadeOut(x_eq)
        )
        self.wait(2)

        self.play( FadeOut(f3, plot_copy, ip_1) )
        self.wait()




        ###* NEW *###

class DTPA4(Scene):
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)
        axes = Axes(
            x_range=[-7, 7],
            y_range=[-12, 12, 2],
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 27
            },
            tips=False,
        )
#        plot = axes.plot(lambda x: ((x)**3 + 3*(x)**2 - 6*(x) - 8), color=YELLOW_C)

        graph_1 = axes.plot(lambda x: ((x)**3 + 3*(x)**2 - 6*(x) - 8), color=YELLOW_C)
        graph_2 = axes.plot(lambda x: ((x - 1)**3 + 3*(x - 1)**2 - 6*(x - 1) - 8), color=RED_C)

        points_array = []

        for i in range(260):
            x = -5 +i*.03
            y = f1(x)
            point = Dot(color=YELLOW, radius=.03).move_to(axes.coords_to_point(x, y, 0)).set_z_index(1.9)
            points_array.append(point)

        points = VGroup(*points_array)

        f = MathTex("f(x) = ax^3 + bx^2 + cx + d").scale(.8).to_edge( UP + LEFT )
        f[0][0:4].set_color(YELLOW_C)
        f[0][0+5].set_color(PINK)
        f[0][4+5].set_color(BLUE)
        f[0][8+5].set_color(GREEN_B)
        f[0][11+5].set_color(ORANGE)

        g = MathTex("g(x) = f(x - \\frac{b}{3a})").scale(.8).next_to(f, DOWN, buff=0.5).to_edge( LEFT )
        g[0][0:4].set_color(RED)
        g[0][5:14].set_color(YELLOW_C)
        g[0][9].set_color(BLUE)
        g[0][12].set_color(PINK)

        g_1 = MathTex("g(x) = ax^3 + cx + d").scale(.8).move_to(g).to_edge( UP + LEFT )
        g_1[0][0:4].set_color(RED)
        g_1[0][0+5].set_color(PINK)
        g_1[0][9].set_color(GREEN_B)
        g_1[0][12].set_color(ORANGE)


        ip_g = Dot(color=BLUE, radius=.1).move_to(axes.coords_to_point(0, 0, 0)).set_z_index(2)

        # self.add(points, axes, zp_1, zp_2, ip_1, f)
        self.add( axes )
        
        ### INFO: VIDEO ###
        self.play( Create(points) )
        self.wait(1)

        self.play( Write(f) )
        self.wait(1)

        self.play( ShowPassingFlash(graph_1, time_width=0.3 ), run_time=3 )
        self.wait(1)

        points_g = copy.deepcopy(points).set_color(RED)
        self.play( 
            Write(g[0][0:8]),
            FadeIn(points_g)
        )
        self.wait(1)

        self.play( points_g.animate.shift( axes.coords_to_point(1, 0, 0) ) )
        self.wait(1)
        
        self.play( Write(g[0][8:14]) )
        self.wait(1)

        self.play( 
            ShowPassingFlash(graph_1, time_width=1 ), 
            ShowPassingFlash(graph_2, time_width=1 ),
            run_time=3 
        )
        self.wait(1)

        self.play( Create( ip_g ) )
        self.wait(2)

        self.play( FadeOut( ip_g, points_g ) )
        self.wait(1)

        g_complete = MathTex("g(x) = ax^3 + \\left( \\frac{3ac - b^2}{3a} \\right)x + \\frac{2b^3 + 27a^2d - 9abc}{27a^2}").scale(.8).move_to(g).to_edge( LEFT )
        g_complete[0][0:4].set_color(RED)
        g_complete[0][5:41].set_color(YELLOW_A)

        g_complete[0][5].set_color(PINK)
        g_complete[0][11].set_color(PINK)
        g_complete[0][28].set_color(PINK)
        g_complete[0][33].set_color(PINK)
        g_complete[0][39].set_color(PINK)
        
        g_complete[0][14].set_color(BLUE)
        g_complete[0][23].set_color(BLUE)
        g_complete[0][34].set_color(BLUE)

        g_complete[0][12].set_color(GREEN_B)
        g_complete[0][35].set_color(GREEN_B)

        g_complete[0][30].set_color(ORANGE)
        points_g[45:110].set_opacity(0.2),
        self.play( 
            FadeOut( points, shift=RIGHT ),
            FadeIn( points_g, shift=RIGHT ),
            ReplacementTransform( g, g_complete ),
            axes.animate.set_opacity(0.2),
        )
        self.wait(2)

        self.play( FadeOut( axes, f, g_complete, points_g ) )
        self.wait(1)

class DTPA5(Scene):
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        general_equation = MathTex("ax^3 + bx^2 + cx + d = 0")
        general_equation[0][0].set_color(YELLOW)
        general_equation[0][4].set_color(RED)
        general_equation[0][8].set_color(GREEN_B)
        general_equation[0][11].set_color(ORANGE)

        arrow = Arrow(start=UP, end=DOWN, color=YELLOW_A).next_to(general_equation, DOWN)

        tt = "\\left( x - \\frac{b}{3a} \\right)" # translated text
        general_equation_t = MathTex(f"a{tt}^3 + b{tt}^2 + c{tt} + d = 0").next_to(arrow, DOWN)
        general_equation_t[0][0].set_color(YELLOW)
        general_equation_t[0][7].set_color(YELLOW)
        general_equation_t[0][18].set_color(YELLOW)
        general_equation_t[0][29].set_color(YELLOW)

        general_equation_t[0][4].set_color(RED)
        general_equation_t[0][11].set_color(RED)
        general_equation_t[0][15].set_color(RED)
        general_equation_t[0][26].set_color(RED)
        
        general_equation_t[0][22].set_color(GREEN_B)
        
        general_equation_t[0][32].set_color(ORANGE)

        ##
        g_complete = MathTex("ax^3 + \\left( \\frac{3ac - b^2}{3a} \\right)x + \\frac{2b^3 + 27a^2d - 9abc}{27a^2} = 0").next_to(arrow, DOWN)
        g_complete[0][0].set_color(YELLOW)
        g_complete[0][6].set_color(YELLOW)
        g_complete[0][13].set_color(YELLOW)
        g_complete[0][23].set_color(YELLOW)
        g_complete[0][28].set_color(YELLOW)
        g_complete[0][34].set_color(YELLOW)

        g_complete[0][9].set_color(RED)
        g_complete[0][18].set_color(RED)
        g_complete[0][29].set_color(RED)
        
        
        g_complete[0][7].set_color(GREEN_B)
        g_complete[0][30].set_color(GREEN_B)

        g_complete[0][25].set_color(ORANGE)

        ##
        g_complete_2 = MathTex("ax^3 + \\left( \\frac{3ac - b^2}{3a} \\right)x = - \\frac{2b^3 + 27a^2d - 9abc}{27a^2}").next_to(arrow, DOWN)
        g_complete_2[0][0].set_color(YELLOW)
        g_complete_2[0][6].set_color(YELLOW)
        g_complete_2[0][13].set_color(YELLOW)
        g_complete_2[0][24].set_color(YELLOW)
        g_complete_2[0][29].set_color(YELLOW)
        g_complete_2[0][35].set_color(YELLOW)

        g_complete_2[0][9].set_color(RED)
        g_complete_2[0][19].set_color(RED)
        g_complete_2[0][30].set_color(RED)
        
        
        g_complete_2[0][7].set_color(GREEN_B)
        g_complete_2[0][31].set_color(GREEN_B)
        
        g_complete_2[0][26].set_color(ORANGE)

        ##

        ##
        g_complete_3 = MathTex("x^3 + \\left( \\frac{3ac - b^2}{3a^2} \\right)x = - \\frac{2b^3 + 27a^2d - 9abc}{27a^3}").next_to(arrow, DOWN)
        g_complete_3[0][0].set_color(YELLOW)
        g_complete_3[0][5].set_color(YELLOW)
        g_complete_3[0][12].set_color(YELLOW)
        g_complete_3[0][24].set_color(YELLOW)
        g_complete_3[0][29].set_color(YELLOW)
        g_complete_3[0][35].set_color(YELLOW)

        g_complete_3[0][8].set_color(RED)
        g_complete_3[0][19].set_color(RED)
        g_complete_3[0][30].set_color(RED)
        
        
        g_complete_3[0][7].set_color(GREEN_B)
        g_complete_3[0][31].set_color(GREEN_B)
        
        g_complete_3[0][26].set_color(ORANGE)

        VGroup(general_equation, general_equation_t, g_complete, g_complete_2, g_complete_3, arrow).move_to(ORIGIN)
        _1_a = MathTex(" \\left| \\cdot \\frac{1}{a}").next_to(g_complete_2, RIGHT, buff=0.5)
        _1_a[0][5].set_color(YELLOW)

        ##
        x_solution = MathTex(
            "x = "
            " \\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } } ",
            "-"
            "\\frac{m}{3\\sqrt[3]{ \\frac{n}{2} \\pm  \\sqrt{ \\frac{n^2}{4} + \\frac{m^3}{27} } }}"
         ).set_color(YELLOW_A).next_to(g_complete_3, DOWN, buff=1.5)
        x_solution[0][5].set_color(PURPLE)
        x_solution[0][11].set_color(PURPLE)
        x_solution[1][7].set_color(PURPLE)
        x_solution[1][13].set_color(PURPLE)

        x_solution[0][16].set_color(BLUE)
        x_solution[1][1].set_color(BLUE)
        x_solution[1][18].set_color(BLUE)




        
        ### INFO: VIDEO ###
        self.wait()
        self.play( Write(general_equation) )
        self.wait()

        self.play( 
            Create(arrow), 
            Write(general_equation_t)
        )
        self.wait()

        self.play( ReplacementTransform(general_equation_t, g_complete) )
        self.wait()

        self.play( 
            FadeOut(g_complete[0][0:17]), 
            FadeOut(g_complete[0][17:36], shift=RIGHT), 
            FadeOut(g_complete[0][36:38], shift=LEFT), 

            FadeIn(g_complete_2[0][0:16]),
            FadeIn(g_complete_2[0][16:37], shift=LEFT),
        )
        self.wait()

        self.play( Write(_1_a) )
        self.wait()

        b1 = always_redraw(lambda: Brace( g_complete_3[0][3:15], DOWN, color=BLUE ))
        b1t = always_redraw(lambda: MathTex("m", color=BLUE).next_to(b1, DOWN) )
        B1G =  VGroup(b1, b1t)

        b2 = always_redraw( lambda: Brace( g_complete_3[0][17:37], DOWN, color=PURPLE ) )
        b2t = always_redraw( lambda: MathTex("n", color=PURPLE).next_to(b2, DOWN) )
        B2G = VGroup(b2, b2t)
        self.play( 
            FadeOut(_1_a), 
            ReplacementTransform(g_complete_2, g_complete_3),
            Write(B1G), Write(B2G)
        )
        self.wait()
        
        
        ###
        self.play( 
            FadeOut(arrow, general_equation, shift=UP), 
            Write(x_solution),
            VGroup( x_solution, g_complete_3 ).animate.move_to(ORIGIN)
        )
        self.wait()

        axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-2, 5, 1],
            axis_config={
                "color": WHITE,
                "include_numbers": False,
                "font_size": 27,
            },
            tips=False,
        ).set_opacity(0.7).scale(0.8).move_to(x_solution)

        zp1 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(-3, 0, 0)).set_z_index(2)
        zp2 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(0, 0, 0)).set_z_index(2)
        zp3 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(3, 0, 0)).set_z_index(2)
        zp = VGroup(zp1, zp2, zp3)

        zp11 = Dot(color=YELLOW, radius=.1).move_to(axes.coords_to_point(-4, 0, 0)).set_z_index(2)
        zp12 = Dot(color=YELLOW, radius=.1).move_to(axes.coords_to_point(-1, 0, 0)).set_z_index(2)
        zp13 = Dot(color=YELLOW, radius=.1).move_to(axes.coords_to_point(2, 0, 0)).set_z_index(2)
        zp1 = VGroup(zp11, zp12, zp13)

        self.play(
            Create(axes),
            FadeOut(B1G, B2G),
            ReplacementTransform(x_solution, zp, run_time=1.5)
        )
        self.wait()

        self.play(
            ReplacementTransform(zp, zp1)
        )
        self.wait()


        general_equation.move_to(g_complete_3)
        self.play(
            FadeOut(g_complete_3, shift=UP),
            ReplacementTransform( copy.deepcopy(zp1), general_equation )
        )
        self.wait()

