'''
To create animation run in terminal:
>>> manim -pql introduction.py [Class Name]

Ex:
>>> manim -pql introduction.py Intro

###

To create animation with transparent background (used for the functions):
>>> manim -pql introduction.py [Class Name] - t

Ex:
>>> manim -pql introduction.py Intro -t
'''

from manim import *
from random import *
 
class Intro(MovingCameraScene):
    def create_square(self, size):
        """Create a square of the given size."""
        return VGroup(Square(side_length=size), Tex(f"${size}^2$").scale(size))

    def get_camera_centering_animation(self, squares):
        """Center (and scale) the camera at the given square."""
        h = squares.height * 1.5
        return self.camera.frame.animate.set_height(h).move_to(squares)

    def construct(self):
        squares = VGroup(self.create_square(1))


        # INFO: HERE
        egypt_svg = SVGMobject("assets/egypt.svg").scale_to_fit_width(7)

        greece_svg = SVGMobject("assets/greece.svg").scale_to_fit_width(6).shift(DOWN).set_z_index(10)

        self.wait(1)
        egypt_svg[59:62].set_z_index(1)
        self.play(
            FadeIn(egypt_svg[20], shift=UP),
            Create( egypt_svg[23:38] ),
            Create( egypt_svg[38:63] ),
        )
        self.wait(1)
        self.play(
            FadeOut(egypt_svg[23:36]),

            FadeOut(egypt_svg[40:42]),
            Uncreate(egypt_svg[42:56]),
            FadeIn(greece_svg, shift=UP),
        )
        self.wait(1)
        # INFO: HERE


        n = 7

        # create the squares
        a = 1
        b = 1
        directions = [RIGHT, UP, LEFT, DOWN]
        for i in range(n):
            b = b + a
            a = b - a

            direction = directions[i % 4]

            new_square = self.create_square(a).next_to(squares, direction, buff=0)
            squares.add(new_square)


        dot = Dot().move_to(squares[0].get_corner(LEFT + UP)).scale(0.5)

        path = TracedPath(dot.get_center)


        # start the spiral
        squares.set_color(DARK_GRAY),
        self.play(
            FadeIn(squares),
            FadeOut( 
                egypt_svg[20],
                egypt_svg[36:40],
                egypt_svg[56:64],
             ),
            ReplacementTransform(greece_svg, dot),
            AnimationGroup(
                self.get_camera_centering_animation(squares[0]).move_to(dot),
                # self.camera.frame.animate.restore().move_to(dot),
                lag_ratio=0.5,
            ),
        )

        # keep a copy of the dot at the origin
        center_dot = dot.copy()
        self.add(center_dot)

        # for scaling the dot
        starting_frame_height = self.camera.frame.height

        def update_camera_position(camera):
            """Updater k pozicování kamery nad tečkou."""
            camera.move_to(dot.get_center())

        def update_spiral(path):
            """Scale the thickness of the stroke with the zoom of the camera."""
            path.set_stroke_width(self.camera.frame.height / 1.5)

        def update_dot(dot):
            """Scale the size of the dot with the zoom of the camera."""
            dot.set_height(center_dot.height * (self.camera.frame.height / starting_frame_height))

        # don't forget to add the path to the scene so it gets animated
        self.add(path)

        path.add_updater(update_spiral)

        self.camera.frame.add_updater(update_camera_position)

        dot.add_updater(update_dot)

        a = 0
        b = 1
        for i in range(n + 1):
            # the directions are defined in a way where neighbouring directions correspond
            # to points around which we want to rotate
            direction = directions[i % 4] + directions[(i + 1) % 4]
            b = b + a
            a = b - a

            # we're zooming by about the golden ratio each rotation (a little less for
            # the animation to look smoother)
            phi = (1 + 5 ** (1 / 2)) / 2
            zoom_coefficient = phi * 0.9

            self.play(
                Rotate(
                    dot,
                    about_point=squares[i].get_corner(direction),
                    angle=PI / 2,
                ),
                self.camera.frame.animate.scale(zoom_coefficient),
                rate_func=linear,
            )

        # cleanup
        self.camera.frame.clear_updaters()
        path.clear_updaters()
        dot.clear_updaters()

        self.play(self.get_camera_centering_animation(squares))

        self.wait(1)
        
        self.play(
            FadeOut(squares),
            FadeOut(dot),
            AnimationGroup(
                Unwrite(path, run_time=2),
                AnimationGroup(Flash(center_dot, color=WHITE), FadeOut(center_dot)),
                lag_ratio=0.9,
            ),
        )


class I2(ThreeDScene):
# class I2(MovingCameraScene):
    def construct(self):
        general_equation = MathTex("ax^3 + bx^2 + cx + d = 0")
        general_equation[0][0].set_color(YELLOW)
        general_equation[0][4].set_color(RED)
        general_equation[0][8].set_color(GREEN_B)
        general_equation[0][11].set_color(ORANGE)

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
        zp2 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(-1, 0, 0)).set_z_index(2)
        zp3 = Dot(color=RED, radius=.1).move_to(axes.coords_to_point(2, 0, 0)).set_z_index(2)

        ### INFO: VIDEO ###
        self.play( Write(general_equation) )
        self.wait(1)

        self.play( 
            general_equation.animate.scale(0.8).to_edge(UP + LEFT),
            Create( plot, run_time=2 ), 
            Create( axes )
        )
        self.wait(1)
        
        self.play( ReplacementTransform(general_equation, VGroup(zp1, zp2, zp3) ) )
        self.wait(1)

        # info: 3d objects
        cube_dim = 3
        cube = Cube(side_length=cube_dim, fill_opacity=1, fill_color=YELLOW_D)
        blue_width = .5
        blue_depth = 3.5


        bluep1 = Prism(dimensions=[blue_width, blue_depth, cube_dim], fill_opacity=0.5, fill_color=BLUE).next_to(cube, LEFT, buff=1.5).shift(UP*4.5)
        bluep2 = Prism(dimensions=[blue_width, blue_depth, cube_dim], fill_opacity=0.5, fill_color=BLUE).next_to(bluep1, LEFT, buff=0)
        bluep3 = Prism(dimensions=[blue_width, blue_depth, cube_dim], fill_opacity=0.5, fill_color=BLUE).next_to(bluep2, LEFT, buff=0)

        area = 3.5*.5
        ttt = abs(cube_dim - area/blue_width)

        bluep1.rotate(90*DEGREES, axis=RIGHT).next_to(cube, RIGHT, buff=0).shift(0.5*ttt*OUT),
        bluep2.rotate(90*DEGREES).next_to(cube, UP, buff=0).shift(0.5*ttt*RIGHT)
        bluep3.rotate(90*DEGREES, axis=UP).next_to(cube, OUT, buff=0).shift(0.5*ttt*UP)
        
        cube_group = VGroup(cube, bluep1, bluep2, bluep3).rotate(30*DEGREES, axis=UP+RIGHT)
        # info: 3d objects



        self.play(
            ReplacementTransform(VGroup(plot, axes, zp1, zp2, zp3), cube_group),
        )
        self.play(
            Rotating(cube_group, axis=UP+RIGHT, radians=PI, run_time=2.5 )
        )
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
            ReplacementTransform(cube_group, x_solution)
        )
        self.wait(3)
        