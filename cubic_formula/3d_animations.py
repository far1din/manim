'''
To create animation run in terminal:
>>> manim -pql 3d_animations.py [Class Name]

Ex:
>>> manim -pql 3d_animations.py A1

###

To create animation with transparent background (used for the functions):
>>> manim -pql 3d_animations.py [Class Name] - t

Ex:
>>> manim -pql 3d_animations.py A1 -t
'''
from manim import *
import copy
import numpy as np


# info: 3D ANIMATIONS
# INITIAL SCENES
class A1(ThreeDScene):
    #info: EQ: x^3 + 6x = 20
    #info: Here we use the updater to show that the bottom can be whatever as long as the area is equal to ###. However, there are some issues with choosing random sidelengths for the bottom.
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        # axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES, gamma=0*DEGREES, zoom=0.8)
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES, gamma=0*DEGREES, zoom=0.8)


        # YELLOW CUBE #
        cube_dim = 3

        cube = Cube(side_length=cube_dim, fill_opacity=1, fill_color=YELLOW_D)

        b1 = Brace(cube, RIGHT)
        t1 = MathTex("x").next_to(b1, RIGHT).rotate(180*DEGREES)
        BG1 = VGroup(b1, t1).rotate(90*DEGREES, axis=LEFT).shift(DOWN * (cube_dim*.5 + .05))

        b2 = Brace(cube, RIGHT)
        t2 = MathTex("x").next_to(b2, RIGHT).rotate(90*DEGREES)
        BG2 = VGroup(b2, t2).shift(IN * (cube_dim*.5 + .1))

        b3 = Brace(cube, IN)
        t3 = MathTex("x").next_to(b3, UP).rotate(180*DEGREES)
        BG3 = VGroup(b3, t3).shift(IN * (cube_dim*.5 + .1))
        # YELLOW CUBE #



        # BLUE PRISM #
        area = 3.5*.5
        blue_width = ValueTracker(0.5)

        area_text = "m"
        blue_depth_text = ValueTracker(6)

        bp1_opacity = ValueTracker(0)
        bp2_opacity = ValueTracker(0)
        bp3_opacity = ValueTracker(0)

        bluep1 = always_redraw(
            lambda: Prism(
                dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
                fill_opacity=1, 
                fill_color=BLUE).next_to(cube, LEFT, buff=1.5).shift(UP*4.5).set_opacity(bp1_opacity.get_value())
        )

        bluep2 = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
            fill_opacity=1, 
            fill_color=BLUE).next_to(bluep1, LEFT, buff=0).set_opacity(bp2_opacity.get_value())
        )
        
        bluep3 = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
            fill_opacity=1, 
            fill_color=BLUE).next_to(bluep2, LEFT, buff=0).set_opacity(bp3_opacity.get_value())
        )

        
        bluep_group = VGroup(bluep1, bluep2, bluep3)
        
        
        b4 = always_redraw(
            lambda: Brace(Line([0, 0, 0], [cube_dim, 0, 0]), DOWN).rotate(90*DEGREES).rotate(90*DEGREES, axis=RIGHT).next_to(bluep_group, RIGHT).shift(.5*area/blue_width.get_value()*DOWN)
        )
        t4 = always_redraw(lambda: MathTex("x").next_to(b4, RIGHT).rotate(90*DEGREES, axis=RIGHT))
        BG4 = VGroup(b4, t4)


        # b5 = always_redraw(lambda: Brace(bluep_group, RIGHT).shift(IN * (cube_dim*.5 + .1)))
        # t5 = always_redraw(lambda: MathTex( str( "{:.2f}".format( np.around( blue_depth_text.get_value(), 2)) ) ).next_to(b5, RIGHT).rotate(90*DEGREES))
        # BG5 = VGroup(b5, t5)

        # b6 = always_redraw(lambda: Brace(bluep_group, IN).shift(IN * (cube_dim*.5 + .1)))
        # t6 = always_redraw(lambda: MathTex( str( "{:.2f}".format(np.round(area_text/blue_depth_text.get_value(), 2) )) ).next_to(b6, UP).rotate(PI))
        # BG6 = VGroup(b6, t6)
        # BLUE PRISM #


        always_redraw(lambda: VGroup(cube, BG1, BG2, BG3, bluep1, bluep2, bluep3, BG4).move_to((0,0,0)))

        blue_prism_pre_slice = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value()*3, area/blue_width.get_value(), cube_dim], fill_opacity=1, fill_color=BLUE).move_to(bluep_group).set_opacity(0.3)
        )
        
        
        blue_bottom = always_redraw(lambda: Rectangle(width=blue_width.get_value()*3, height=area/blue_width.get_value(), fill_opacity=1, fill_color=BLUE, stroke_opacity=0).move_to(bluep_group).shift(.5*cube_dim*IN))
        blue_bottom_area_text = always_redraw(lambda: MathTex(str(area_text), color=BLACK).rotate(180*DEGREES).move_to(blue_bottom))

        self.add( bluep1, bluep2, bluep3 )



        ### info: video ###
        self.wait(2)
        self.play( FadeIn(cube), Create(BG1), Create(BG2), Create(BG3) )
        self.wait(1)
        self.play( 
            FadeIn(blue_prism_pre_slice), 
            Create( BG4 ),
            Create( blue_bottom ),
            Create( blue_bottom_area_text),
        )

        self.pause(1)
        self.play(
            blue_width.animate.set_value(1), 
            blue_depth_text.animate.set_value(1.5), 
 
            rate_func=linear, 
            run_time=1.5
        )
        self.pause(1)

        self.play(
            Indicate(blue_bottom_area_text, color=RED),
            ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text, color=RED), time_width=0.5 ),
            FadeOut(blue_bottom)
        )
        self.pause(1)

        # self.play( ReplacementTransform(VGroup(copy.deepcopy(t5), copy.deepcopy(t6)),blue_bottom_area_text), Indicate(blue_bottom_area_text), ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text, color=WHITE), time_width=0.5 ) )
        # self.pause(1)
        
        self.play( 
            Indicate( cube, scale_factor=1, color=RED ),
        )
        self.pause(1)
        self.play( 
            Indicate( blue_prism_pre_slice, scale_factor=1, color=RED )
        )
        self.pause(1)




        # new_bb_1 = Brace(bluep1, IN).shift(IN * (cube_dim*.5 + .1)) # new blue brace 1
        # new_bbt_1 = MathTex("\\frac{4}{3}").next_to(new_bb_1, UP).rotate(180*DEGREES) # new blue brace text 1

        # new_bb_2 = Brace(bluep2, IN).shift(IN * (cube_dim*.5 + .1))
        # new_bbt_2 = MathTex("\\frac{4}{3}").next_to(new_bb_2, UP).rotate(180*DEGREES)

        # new_bb_3 = Brace(bluep3, IN).shift(IN * (cube_dim*.5 + .1))
        # new_bbt_3 = MathTex("\\frac{4}{3}").next_to(new_bb_3, UP).rotate(180*DEGREES)

        self.play(
            FadeOut(blue_prism_pre_slice, blue_bottom_area_text),
            # FadeIn(new_bb_1, new_bbt_1, new_bb_2, new_bbt_2, new_bb_3, new_bbt_3, ),
            bp1_opacity.animate.set_value(0.5),
            bp2_opacity.animate.set_value(0.5),
            bp3_opacity.animate.set_value(0.5)
        )
        self.pause(1)

        
        
        
        
        
        
        
        # info: rotate the prisms to show the difficulty of completing the cube
        # rotate the first prism piece
        ttt = abs(cube_dim - area/blue_width.get_value())

        bluep1_copy = copy.deepcopy(bluep1)
        bluep2_copy = copy.deepcopy(bluep2)
        bluep3_copy = copy.deepcopy(bluep3)
        self.play( 
            bluep1_copy.animate.rotate(90*DEGREES, axis=RIGHT).next_to(cube, RIGHT, buff=0).shift(0.5*ttt*OUT),
            bp1_opacity.animate.set_value(0),
            FadeOut(BG1, BG2, BG3),
            
            bluep2_copy.animate.rotate(90*DEGREES).next_to(cube, UP, buff=0).shift(0.5*ttt*RIGHT),
            bp2_opacity.animate.set_value(0),

            bluep3_copy.animate.rotate(90*DEGREES, axis=UP).next_to(cube, OUT, buff=0).shift(0.5*ttt*UP),
            bp3_opacity.animate.set_value(0),
            FadeOut(BG4)
        )
        self.wait(1)
        brace_1 = Brace(cube, RIGHT).shift(IN * (cube_dim*.5 + .1))

        self.wait(1)

    

        # rotate object
        objects_to_rotate = VGroup( cube, bluep1_copy, bluep2_copy, bluep3_copy )
        self.play( objects_to_rotate.animate.move_to(ORIGIN) )
        
        self.play( Rotating(objects_to_rotate) )
        self.wait(1)

class A1_FIX(ThreeDScene):
    #info: EQ: x^3 + 6x = 20
    #info: Here we use the updater to show that the bottom can be whatever as long as the area is equal to ###. However, there are some issues with choosing random sidelengths for the bottom.
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        # axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES, gamma=0*DEGREES, zoom=0.8)
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES, gamma=0*DEGREES, zoom=0.8)


        # YELLOW CUBE #
        cube_dim = 3

        cube = Cube(side_length=cube_dim, fill_opacity=1, fill_color=YELLOW_D)

        b1 = Brace(cube, RIGHT)
        t1 = MathTex("x").next_to(b1, RIGHT).rotate(180*DEGREES)
        BG1 = VGroup(b1, t1).rotate(90*DEGREES, axis=LEFT).shift(DOWN * (cube_dim*.5 + .05))

        b2 = Brace(cube, RIGHT)
        t2 = MathTex("x").next_to(b2, RIGHT).rotate(90*DEGREES)
        BG2 = VGroup(b2, t2).shift(IN * (cube_dim*.5 + .1))

        b3 = Brace(cube, IN)
        t3 = MathTex("x").next_to(b3, UP).rotate(180*DEGREES)
        BG3 = VGroup(b3, t3).shift(IN * (cube_dim*.5 + .1))
        # YELLOW CUBE #



        # BLUE PRISM #
        area = 3.5*.5
        blue_width = ValueTracker(0.5)

        area_text = "m"
        blue_depth_text = ValueTracker(6)

        bp1_opacity = ValueTracker(0)
        bp2_opacity = ValueTracker(0)
        bp3_opacity = ValueTracker(0)

        bluep1 = always_redraw(
            lambda: Prism(
                dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
                fill_opacity=1, 
                fill_color=BLUE).next_to(cube, LEFT, buff=1.5).shift(UP*4.5).set_opacity(bp1_opacity.get_value())
        )

        bluep2 = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
            fill_opacity=1, 
            fill_color=BLUE).next_to(bluep1, LEFT, buff=0).set_opacity(bp2_opacity.get_value())
        )
        
        bluep3 = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
            fill_opacity=1, 
            fill_color=BLUE).next_to(bluep2, LEFT, buff=0).set_opacity(bp3_opacity.get_value())
        )

        
        bluep_group = VGroup(bluep1, bluep2, bluep3)
        
        
        b4 = always_redraw(
            lambda: Brace(Line([0, 0, 0], [cube_dim, 0, 0]), DOWN).rotate(90*DEGREES).rotate(90*DEGREES, axis=RIGHT).next_to(bluep_group, RIGHT).shift(.5*area/blue_width.get_value()*DOWN)
        )
        t4 = always_redraw(lambda: MathTex("x").next_to(b4, RIGHT).rotate(90*DEGREES, axis=RIGHT))
        BG4 = VGroup(b4, t4)

        always_redraw(lambda: VGroup(cube, BG1, BG2, BG3, bluep1, bluep2, bluep3, BG4).move_to((0,0,0)))

        blue_prism_pre_slice = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value()*3, area/blue_width.get_value(), cube_dim], fill_opacity=1, fill_color=BLUE).move_to(bluep_group).set_opacity(0.3)
        )
        
        
        blue_bottom = always_redraw(lambda: Rectangle(width=blue_width.get_value()*3, height=area/blue_width.get_value(), fill_opacity=1, fill_color=BLUE, stroke_opacity=0).move_to(bluep_group).shift(.5*cube_dim*IN))
        blue_bottom_area_text = always_redraw(lambda: MathTex(str(area_text), color=BLACK).rotate(180*DEGREES).move_to(blue_bottom))

        self.add( cube, BG1, BG2, BG3, bluep1, bluep2, bluep3, blue_prism_pre_slice, BG4, blue_bottom, blue_bottom_area_text )



        ### info: video ###
        self.play(
            blue_width.animate.set_value(1), 
            blue_depth_text.animate.set_value(1.5), 
 
            rate_func=linear, 
            run_time=1.5
        )

        self.play( FadeOut(blue_prism_pre_slice, BG4, blue_bottom, blue_bottom_area_text ) )
        self.pause(2)

        self.play( 
            FadeIn(blue_prism_pre_slice), 
            Create( BG4 ),
            Create( blue_bottom ),
            Create( blue_bottom_area_text),
        )
        self.pause(1)

        self.play(
            Indicate(t4),
            ShowPassingFlash( SurroundingRectangle(t4, color=RED, buff=.2).rotate(90*DEGREES, axis=RIGHT), time_width=0.5 )
        )
        self.pause(1)

        self.play(
            Indicate(blue_bottom_area_text),
            ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text, color=RED), time_width=0.5 ),
            FadeOut(blue_bottom)
        )
        self.pause(1)

class A2(ThreeDScene):
    #info: EQ: x^3 + 6x = 20
    #info: Here we use the updater to show that the bottom can be whatever as long as the area is equal to ###. However, there are some issues with choosing random sidelengths for the bottom.
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        # axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES, gamma=0*DEGREES, zoom=0.8)
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES, gamma=0*DEGREES, zoom=0.8)


        # YELLOW CUBE #
        cube_dim = 3

        cube = Cube(side_length=cube_dim, fill_opacity=1, fill_color=YELLOW_D)

        b1 = Brace(cube, RIGHT)
        t1 = MathTex("x").next_to(b1, RIGHT).rotate(180*DEGREES)
        BG1 = VGroup(b1, t1).rotate(90*DEGREES, axis=LEFT).shift(DOWN * (cube_dim*.5 + .05))

        b2 = Brace(cube, RIGHT)
        t2 = MathTex("x").next_to(b2, RIGHT).rotate(90*DEGREES)
        BG2 = VGroup(b2, t2).shift(IN * (cube_dim*.5 + .1))

        b3 = Brace(cube, IN)
        t3 = MathTex("x").next_to(b3, UP).rotate(180*DEGREES)
        BG3 = VGroup(b3, t3).shift(IN * (cube_dim*.5 + .1))
        # YELLOW CUBE #



        # BLUE PRISM #
        area = 3.5*.5
        blue_width = ValueTracker(0.5)

        area_text = 6
        blue_depth_text = ValueTracker(6)

        bp1_opacity = ValueTracker(0)
        bp2_opacity = ValueTracker(0)
        bp3_opacity = ValueTracker(0)

        bluep1 = always_redraw(
            lambda: Prism(
                dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
                fill_opacity=1, 
                fill_color=BLUE).next_to(cube, LEFT, buff=1.5).shift(UP*4.5).set_opacity(bp1_opacity.get_value())
        )

        bluep2 = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
            fill_opacity=1, 
            fill_color=BLUE).next_to(bluep1, LEFT, buff=0).set_opacity(bp2_opacity.get_value())
        )
        
        bluep3 = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value(), area/blue_width.get_value(), cube_dim], 
            fill_opacity=1, 
            fill_color=BLUE).next_to(bluep2, LEFT, buff=0).set_opacity(bp3_opacity.get_value())
        )

        
        bluep_group = VGroup(bluep1, bluep2, bluep3)
        
        
        b4 = always_redraw(
            lambda: Brace(Line([0, 0, 0], [cube_dim, 0, 0]), DOWN).rotate(90*DEGREES).rotate(90*DEGREES, axis=RIGHT).next_to(bluep_group, RIGHT).shift(.5*area/blue_width.get_value()*DOWN)
        )
        t4 = always_redraw(lambda: MathTex("x").next_to(b4, RIGHT).rotate(90*DEGREES, axis=RIGHT))
        BG4 = VGroup(b4, t4)


        b5 = always_redraw(lambda: Brace(bluep_group, RIGHT).shift(IN * (cube_dim*.5 + .1)))
        t5 = always_redraw(lambda: MathTex( str( "{:.2f}".format( np.around( blue_depth_text.get_value(), 2)) ) ).next_to(b5, RIGHT).rotate(90*DEGREES))
        BG5 = VGroup(b5, t5)

        b6 = always_redraw(lambda: Brace(bluep_group, IN).shift(IN * (cube_dim*.5 + .1)))
        t6 = always_redraw(lambda: MathTex( str( "{:.2f}".format(np.round(area_text/blue_depth_text.get_value(), 2) )) ).next_to(b6, UP).rotate(PI))
        BG6 = VGroup(b6, t6)
        # BLUE PRISM #


        always_redraw(lambda: VGroup(cube, BG1, BG2, BG3, bluep1, bluep2, bluep3, BG4, BG5, BG6).move_to((0,0,0)))

        blue_prism_pre_slice = always_redraw(
            lambda: Prism(dimensions=[blue_width.get_value()*3, area/blue_width.get_value(), cube_dim], fill_opacity=1, fill_color=BLUE).move_to(bluep_group).set_opacity(0.3)
        )
        
        
        blue_bottom = always_redraw(lambda: Rectangle(width=blue_width.get_value()*3, height=area/blue_width.get_value(), fill_opacity=1, fill_color=BLUE, stroke_opacity=0).move_to(bluep_group).shift(.5*cube_dim*IN))
        blue_bottom_area_text = always_redraw(lambda: MathTex("m", color=BLACK).rotate(180*DEGREES).move_to(blue_bottom))

        self.add(cube, BG1, BG2, BG3, bluep1, bluep2, bluep3, blue_prism_pre_slice, BG4, BG5, BG6, blue_bottom, blue_bottom_area_text )



        # info: VIDEO

        self.play(
            blue_width.animate.set_value(1), 
            blue_depth_text.animate.set_value(1.5), 
            
            rate_func=linear, 
            run_time=1.5
        )
        self.play(
            FadeOut( BG5, BG6, blue_bottom )
        )
        self.pause(2)
        
        blue_bottom_area_text_copy = always_redraw(lambda: copy.deepcopy(blue_bottom_area_text)) # copy to fix z-index issue...
        self.play(
            FadeIn( blue_bottom, blue_bottom_area_text_copy )
        )
        self.remove(blue_bottom_area_text)
        self.pause(1)

        self.play(
            Indicate(t4),
            ShowPassingFlash( SurroundingRectangle(t4, color=RED, buff=.2).rotate(90*DEGREES, axis=RIGHT), time_width=0.5 )
        )
        self.pause(1)

        self.play(
            Indicate(blue_bottom_area_text_copy),
            ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text, color=RED), time_width=0.5 )
        )
        self.pause(1)

        self.play(
            Create(BG5),
            Create(BG6),
        )
        self.play(
            blue_width.animate.set_value(0.5), 
            blue_depth_text.animate.set_value(6), 
            
            rate_func=linear, 
            run_time=1.5
        )
        self.pause(1)

        self.play( ReplacementTransform(VGroup(copy.deepcopy(t5), copy.deepcopy(t6)),blue_bottom_area_text_copy), Indicate(blue_bottom_area_text_copy), ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text_copy, color=WHITE), time_width=0.5 ) )
        self.pause(1)

        t = always_redraw( lambda: MathTex( "t" ).next_to(b5, RIGHT).rotate(90*DEGREES) )
        u = always_redraw( lambda: MathTex( "u" ).next_to(b6, UP).rotate(PI) )
        self.play( 
            ReplacementTransform(t5, t),
            ReplacementTransform(t6, u)
        )
        self.pause(1)

class A3(ThreeDScene):
    #info: EQ: x^3 + 6x = 20
    #info: Show the cubes 
    def construct(self):
        # plane = NumberPlane()
        # self.add(plane)

        # axes = ThreeDAxes()
        # self.add(axes)
        self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES, gamma=0*DEGREES, zoom=0.8)
        self.set_camera_orientation(phi=65*DEGREES, theta=45*DEGREES, gamma=0*DEGREES, zoom=0.8)


        # YELLOW CUBE #
        cube_dim = 3

        cube = Cube(side_length=cube_dim, fill_opacity=1, fill_color=YELLOW_D)

        b1 = Brace(cube, RIGHT)
        t1 = MathTex("x").next_to(b1, RIGHT).rotate(180*DEGREES)
        BG1 = VGroup(b1, t1).rotate(90*DEGREES, axis=LEFT).shift(DOWN * (cube_dim*.5 + .05))

        b2 = Brace(cube, RIGHT)
        t2 = MathTex("x").next_to(b2, RIGHT).rotate(90*DEGREES)
        BG2 = VGroup(b2, t2).shift(IN * (cube_dim*.5 + .1))

        b3 = Brace(cube, IN)
        t3 = MathTex("x").next_to(b3, UP).rotate(180*DEGREES)
        BG3 = VGroup(b3, t3).shift(IN * (cube_dim*.5 + .1))
        # YELLOW CUBE #



        # BLUE PRISM #
        blue_width = .5
        blue_depth = 3.5

        blue_width_text = "u"
        blue_depth_text = "t"

        bluep1 = Prism(dimensions=[blue_width, blue_depth, cube_dim], fill_opacity=.4, fill_color=BLUE).next_to(cube, LEFT, buff=1.5).shift(UP*4.5)
        bluep2 = Prism(dimensions=[blue_width, blue_depth, cube_dim], fill_opacity=.4, fill_color=BLUE).next_to(bluep1, LEFT, buff=0)
        bluep3 = Prism(dimensions=[blue_width, blue_depth, cube_dim], fill_opacity=.4, fill_color=BLUE).next_to(bluep2, LEFT, buff=0)

        bluep_group = VGroup(bluep1, bluep2, bluep3)
        

        b4 = Brace(Line([0, 0, 0], [cube_dim, 0, 0]), DOWN).rotate(90*DEGREES).rotate(90*DEGREES, axis=RIGHT).next_to(bluep_group, RIGHT).shift(.5*blue_depth*DOWN)
        t4 = MathTex("x").next_to(b4, RIGHT).rotate(90*DEGREES, axis=RIGHT)
        BG4 = VGroup(b4, t4)

        b5 = Brace(bluep_group, RIGHT)
        t5 = MathTex( str(blue_depth_text) ).next_to(b5, RIGHT).rotate(90*DEGREES)
        BG5 = VGroup(b5, t5).shift(IN * (cube_dim*.5 + .1))

        b6 = Brace(bluep_group, IN)
        t6 = MathTex( str(blue_width_text) ).next_to(b6, UP).rotate(PI)
        BG6 = VGroup(b6, t6).shift(IN * (cube_dim*.5 + .1))
        # BLUE PRISM #


        VGroup(cube, BG1, BG2, BG3, bluep1, bluep2, bluep3, BG4, BG5, BG6 ).move_to((0,0,0))
        
        
        blue_prism_pre_slice = Prism(dimensions=[blue_width*3, blue_depth, cube_dim], fill_opacity=1, fill_color=BLUE).move_to(bluep_group)
        blue_bottom = Rectangle(width=blue_width*3, height=blue_depth, fill_opacity=1, fill_color=BLUE, stroke_opacity=0).move_to(bluep_group).shift(.5*cube_dim*IN)
        blue_bottom_area_text = MathTex("m", color=BLACK).rotate(180*DEGREES).move_to(blue_bottom)

        ### video ###
        self.wait(2)
        self.play( FadeIn(cube), Create(BG1), Create(BG2), Create(BG3) )
        self.wait(1)
        self.play( FadeIn(blue_prism_pre_slice), Create(BG4) )
        self.wait(1)
        self.play( FadeIn(blue_bottom, blue_bottom_area_text), blue_prism_pre_slice.animate.set_opacity(0.3) )
        self.wait(1)

        self.play( Indicate(blue_bottom_area_text), ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text, color=WHITE), time_width=0.5 ) )
        self.wait(1)

        
        self.play( Indicate(cube, scale_factor=1, color=RED_E) )
        self.wait(1)
        
        self.play( 
            Indicate(blue_prism_pre_slice, scale_factor=1, color=RED_E),
            Indicate(blue_bottom, scale_factor=1, color=RED_E),
        )
        self.wait(1)


        self.play( Create(BG5), Create(BG6) )
        self.wait(1)

        
        self.play( Indicate(t5, color=RED_E) )
        self.wait(1)
        self.play( Indicate(t6, color=RED_E) )
        self.wait(1)
        self.play( Indicate(blue_bottom_area_text), ShowPassingFlash( SurroundingRectangle(blue_bottom_area_text, color=WHITE), time_width=0.5 ) )
        self.wait(1)
        self.play( Indicate(blue_bottom, color=RED, scale_factor=1) )
        self.wait(1)
        self.play( FadeOut(blue_bottom, blue_bottom_area_text) )
        self.wait(1)




        # info: slice up the prism before rotation
        new_bb_1 = Brace(bluep1, IN).shift(IN * (cube_dim*.5 + .1)) # new blue brace 1
        new_bbt_1 = MathTex("\\frac{u}{3}").next_to(new_bb_1, UP).rotate(180*DEGREES) # new blue brace text 1

        new_bb_2 = Brace(bluep2, IN).shift(IN * (cube_dim*.5 + .1))
        new_bbt_2 = MathTex("\\frac{u}{3}").next_to(new_bb_2, UP).rotate(180*DEGREES)

        new_bb_3 = Brace(bluep3, IN).shift(IN * (cube_dim*.5 + .1))
        new_bbt_3 = MathTex("\\frac{u}{3}").next_to(new_bb_3, UP).rotate(180*DEGREES)

        self.play( 
            FadeOut(blue_prism_pre_slice, b6, t6), 
            FadeIn(
                bluep1, bluep2, bluep3,
                new_bb_1, new_bbt_1, new_bb_2, new_bbt_2, new_bb_3, new_bbt_3
            )
        )
        self.wait(1)


        # rotate the first prism piece
        ttt = abs(cube_dim - blue_depth)
        
        bluep1_copy = copy.deepcopy(bluep1)
        self.play( 
            bluep1_copy.animate.rotate(90*DEGREES, axis=RIGHT).next_to(cube, RIGHT, buff=0).shift(0.5*ttt*OUT),
            FadeOut(new_bb_1, new_bbt_1, bluep1, BG1, BG2, BG3)
        )
        self.wait(1)

        x_brace_left = Brace(bluep1_copy, RIGHT).shift(IN * (cube_dim*.5 + .2))
        x_brace_left_text = MathTex("x").next_to(x_brace_left, RIGHT).rotate(90*DEGREES)
        x_brace_left_group = VGroup(x_brace_left, x_brace_left_text)

        # rotate the second prism piece
        bluep2_copy = copy.deepcopy(bluep2)
        self.play( 
            bluep2_copy.animate.rotate(90*DEGREES).next_to(cube, UP, buff=0).shift(0.5*ttt*RIGHT),
            FadeOut(new_bb_2, new_bbt_2, bluep2)
        )
        self.wait(1)

        t_brace_front = Brace(bluep2_copy, IN).shift(IN * (cube_dim*.5 + .1))
        t_brace_front_text = MathTex("t").next_to(t_brace_front, UP).rotate(180*DEGREES)
        t_brace_front_group = VGroup(t_brace_front, t_brace_front_text)


        u_3_brace_left = BraceBetweenPoints((0, 0, 0), (blue_width, 0, 0), IN).rotate(270*DEGREES).next_to(x_brace_left, UP, buff=0)
        u_3_brace_left_text = MathTex("\\frac{u}{3}").next_to(u_3_brace_left, RIGHT, buff=.4).rotate(90*DEGREES)
        x_u_3_left_group = VGroup(x_brace_left, x_brace_left_text, u_3_brace_left, u_3_brace_left_text)
        

        # rotate the final prism piece
        bluep3_copy = copy.deepcopy(bluep3)
        self.play( 
            bluep3_copy.animate.rotate(90*DEGREES, axis=UP).next_to(cube, OUT, buff=0).shift(0.5*ttt*UP),
            FadeOut(new_bb_3, new_bbt_3, bluep3, t5, BG4, b5)
        )
        self.wait(1)

        x_brace_vertical = Brace(cube, IN).shift(IN * (cube_dim*.5 + .1))
        x_brace_vertical_text = MathTex("x").next_to(x_brace_vertical, UP).rotate(90*DEGREES)

        u_3_brace_vertical = BraceBetweenPoints((0, 0, 0), (blue_width, 0, 0), IN).next_to(x_brace_vertical, LEFT, buff=0)
        u_3_brace_vertical_text = MathTex("\\frac{u}{3}").next_to(u_3_brace_vertical, UP, buff=0).rotate(90*DEGREES)
        
        x_u_3_vertical_group = VGroup(x_brace_vertical, u_3_brace_vertical, x_brace_vertical_text, u_3_brace_vertical_text).rotate(90*DEGREES, axis=UP).next_to(t_brace_front, LEFT, buff=0).shift(OUT*3.5*.5+.3).shift(UP*.3)

        self.play( 
            # FadeIn(vb2_group),
            FadeIn(x_brace_left, x_brace_left_text),
            FadeIn(t_brace_front, u_3_brace_left, t_brace_front_text, u_3_brace_left_text),
            FadeIn(x_u_3_vertical_group),
        )
        
        self.wait(1)


        #info: spin the object
        objects_to_rotate = VGroup( cube, bluep1_copy, bluep2_copy, bluep3_copy, 
                                    x_brace_left, x_brace_left_text, t_brace_front, t_brace_front_text, u_3_brace_left, u_3_brace_left_text, x_brace_vertical, 
                                    x_brace_vertical_text, u_3_brace_vertical, u_3_brace_vertical_text
                                   )

        self.play( objects_to_rotate.animate.move_to(ORIGIN) )
        
        self.play( Rotating(objects_to_rotate, about_point=VGroup( cube, bluep1_copy, bluep2_copy, bluep3_copy ).get_center()) )
        self.wait(2)

        # info: visualize the cube we need to subtract in order to "complete the cube"


        t_brace_vertical = Brace(bluep2_copy, IN).shift(IN * (cube_dim*.5 + .1))
        t_brace_vertical_text = MathTex("t").next_to(t_brace_front, UP).rotate(90*DEGREES)
        t_brace_vertical_group = VGroup(t_brace_vertical, t_brace_vertical_text).rotate(90*DEGREES, axis=UP).move_to(x_u_3_vertical_group)


        t_brace_left = Brace(bluep2_copy, IN).shift(IN * (cube_dim*.5 + .1))
        t_brace_left_text = MathTex("t").next_to(t_brace_front, UP).rotate(180*DEGREES)
        t_brace_left_group = VGroup(t_brace_left, t_brace_left_text).rotate(-90*DEGREES).move_to(x_u_3_left_group).shift(LEFT*.2)
        

        x_brace_front = Brace(bluep1_copy, RIGHT).shift(IN * (cube_dim*.5 + .2))
        x_brace_front_text = MathTex("x").next_to(x_brace_front, RIGHT).rotate(90*DEGREES)
        u_3_brace_front = BraceBetweenPoints((0, 0, 0), (blue_width, 0, 0), IN).rotate(270*DEGREES).next_to(x_brace_front, DOWN, buff=0)
        u_3_brace_front_text = MathTex("\\frac{u}{3}").next_to(u_3_brace_front, RIGHT, buff=.4).rotate(90*DEGREES)

        x_u_3_front_group = VGroup(x_brace_front, x_brace_front_text, u_3_brace_front, u_3_brace_front_text).rotate(90*DEGREES).move_to(t_brace_front_group).shift(UP*.2)

        self.play( ShowPassingFlash( SurroundingRectangle(t_brace_front_text), time_width=.5 ) )
        self.wait(1)

        self.play( FadeOut(t_brace_front_group), FadeIn(x_u_3_front_group), ShowPassingFlash( SurroundingRectangle(x_brace_front_text), time_width=.5 ) )
        self.wait(1)
        self.play( ShowPassingFlash( SurroundingRectangle(u_3_brace_front_text), time_width=.5 ) )
        self.wait(1)

        cube_to_subtract = Cube( .5, fill_opacity=.0, fill_color=BLUE ).next_to(bluep1_copy, UP, buff=0).shift(OUT*1.5)
        self.add(cube_to_subtract)

        self.play( 
            cube_to_subtract.animate.set_opacity(1), 
            bluep1_copy.animate.set_opacity(1), 
            bluep2_copy.animate.set_opacity(1), 
            bluep3_copy.animate.set_opacity(1),

            FadeOut( 
                x_brace_left_group, u_3_brace_left, u_3_brace_left_text,
                x_brace_front, x_brace_front_text, u_3_brace_front, u_3_brace_front_text,
                x_u_3_vertical_group
            ),
            FadeIn( t_brace_left_group, t_brace_front_group, t_brace_vertical_group ),
        )
        self.wait(1)
        self.play(
            Indicate(t_brace_left_text, color=RED),
            Indicate(t_brace_front_text, color=RED),
            Indicate(t_brace_vertical_text, color=RED),
           

        )
        self.wait(1)
        
        self.play( 
            cube_to_subtract.animate.set_opacity(0),
            bluep1_copy.animate.set_opacity(.4), 
            bluep2_copy.animate.set_opacity(.4), 
            bluep3_copy.animate.set_opacity(.4),
            FadeOut( t_brace_left_group, t_brace_front_group, t_brace_vertical_group ),
            FadeIn( 
                x_brace_left_group, u_3_brace_left, u_3_brace_left_text,
                x_brace_front, x_brace_front_text, u_3_brace_front, u_3_brace_front_text,
                x_u_3_vertical_group,
            ),
        )
        self.wait(1)

        self.play(
            cube_to_subtract.animate.set_opacity(.5).set_color(RED_E),
            Indicate(u_3_brace_left_text, color=RED),
            Indicate(u_3_brace_front_text, color=RED),
            Indicate(u_3_brace_vertical_text, color=RED),
        )
        self.wait(1)

        self.play(
            FadeOut( 
                x_brace_left_group, u_3_brace_left, u_3_brace_left_text,
                x_brace_front, x_brace_front_text, u_3_brace_front, u_3_brace_front_text,
                x_u_3_vertical_group,
                bluep1_copy, bluep2_copy, bluep3_copy, cube_to_subtract
            ),
        )        
        self.wait(1)

        self.play(
            FadeIn( 
                # x_brace_left_group, u_3_brace_left, u_3_brace_left_text,
                # x_brace_front, x_brace_front_text, u_3_brace_front, u_3_brace_front_text,
                # x_u_3_vertical_group,
                bluep1_copy, bluep2_copy, bluep3_copy
            ),
        )        
        self.wait(1)

        self.play( Rotating(VGroup(cube, bluep1_copy, bluep2_copy, bluep3_copy), about_point=VGroup( cube, bluep1_copy, bluep2_copy, bluep3_copy ).get_center()) )
        self.wait(2)
