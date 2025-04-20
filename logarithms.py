from manim import *
from manim import config


class Log(Scene):
    def construct(self):
        # Display the word "Logarithms" with an underline
        morning = Text("Logarithms", font_size=100)
        self.play(Write(morning), run_time=3)
        self.wait()
        morning.font_size = 50
        self.play(morning.animate.to_edge(UP), run_time=1)
        ul = Underline(morning)  # Underlining the word
        self.add(morning, ul)
        self.wait()

        # Display the introductory text
        intro_text = Text("Logarithms or logs for short aren't that easy to understand in the first go.").scale(0.8)
        intro_text.move_to(DOWN * 1.5)
        intro_text.set_width(config.frame_width - 2 * LARGE_BUFF)  # Adjust the width
        self.play(Write(intro_text), run_time=3)
        self.wait()
        # Draw a confused human-like figure
        human = ImageMobject("/home/diksha/Downloads/video_images/confused.png").scale(1.5).move_to(UP*1.5)
        self.play(FadeIn(human), run_time=2)
        self.wait()

        # Add question marks in the background
        question_marks = Text("???").scale(2).next_to(human, RIGHT)
        question_marks2 = Text("???").scale(2).next_to(human, LEFT)
        self.play(Write(question_marks), run_time=1)
        self.wait()
        self.play(Write(question_marks2), run_time=1)
        self.wait()

class Log2(Scene):
    def construct(self):

        # Move the quote with rectangle to the top edge and scale it down
        # Display the quote text
        quote = Text(
            "The logarithm is the inverse function to exponentiation.\n"
            "That means the logarithm of a given number x is the exponent to\n"
            "which another fixed number, the base b, must be raised,\n"
            "to produce that number x.",
            color=BLUE,
        ).scale(0.50)

        # Create a surrounding rectangle for the quote
        quote_rect = SurroundingRectangle(quote, color=WHITE, buff=MED_LARGE_BUFF)

        # Play the creation animation
        self.play(Create(quote_rect), Write(quote), run_time=5)
        self.wait()
        quote_rect_target_position = quote_rect.get_top()
        quote_target_position = quote.get_top()
        self.play(
            quote_rect.animate.move_to(quote_rect_target_position),
            quote.animate.move_to(quote_target_position),
            quote_rect.animate.scale(0.65),
            quote.animate.scale(0.65),
            run_time=1
        )
        self.wait()
        g=VGroup(quote,quote_rect)
        self.play(g.animate.to_edge(UP), run_time=1)
        self.wait(5)
        # Draw a logarithmic graph on the right side
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": False},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        ).scale(0.5)

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        graph2 = VGroup(ax,graph)
        self.play(Write(graph2))
        self.play(graph2.animate.to_edge(RIGHT), run_time=1)
        self.wait(3)
        self.add(ax, graph)

        t1 = MathTex(r"\log_{b}(ab)=log_{b}(a)+log_{b}(b)")
        t2 = MathTex(r"\log_{b}(a/b)=log_{b}(a)-log_{b}(b)")
        t3 = MathTex(r"\log_{b}(b)=1")
        t4 = MathTex(r"\log_{b}(1)=0")
        t5 = MathTex(r"\log_{a}(m)=log_{b}(m)/log_{b}(a)")
        t6 = MathTex(r"\log_{b}(m^n)=nlog_{b}(m)")
        t_group=VGroup(t1,t2,t3,t4,t5,t6).scale(0.75)
        t_group.arrange(DOWN,aligned_edge=LEFT)
        # t_group.move_to(LEFT*4)
        t_group.next_to(graph2,LEFT*8)


        self.play(Write(t_group))
        self.wait(3)

        self.wait()

class Log3(Scene):
    def construct(self):
        where_text=Text("Where did this actually come from?")
        where_text.font_size = 30
        self.play(where_text.animate.to_edge(UP), run_time=1)
        ul = Underline(where_text)  # Underlining the word
        self.add(where_text, ul)
        self.wait()
        explain_text=Text("Back in 1700s, way before scientific calculator was invented..\n"
                          "\n"
                          "People had to multiply large numbers manually and this would\n" 
                          "take days just to perform a simple arithmetic operations.\n"
                          "\n"
                          "Then Jhon Napier came up with an idea of Logarithms.",
                          color=BLUE
                          ).scale(0.50).to_edge(LEFT)
        self.play(Write(explain_text))
        self.play(explain_text.animate.move_to(UP).to_edge(LEFT), runtime=2)
        logo = ImageMobject("/home/diksha/Downloads/video_images/John_Napier.jpg")
        logo.to_edge(RIGHT)
        self.play(FadeIn(logo))
        self.wait(3)
        self.play(FadeOut(logo), FadeOut(explain_text))

class Log4(Scene):
    def construct(self):
        # Original text
        original_text = Text("ABCDEFG...").shift(UP)
        self.play(Write(original_text))
        self.wait()
        # New text
        new_text = Text("1234567...").shift(DOWN)
        # Perform transformation
        for orig_char, new_char in zip(original_text, new_text):
            self.play(Transform(orig_char, new_char))


class Log5(Scene):
    def construct(self):
        text2 = Text("Hence logs were introduced to represent larger values on smaller scale.\n"
                     "And a log table was created to make the algorithm easier..\n"
                     ).scale(0.5).to_edge(LEFT)
        self.play(Write(text2))
        self.play(text2.animate.to_edge(UP), runtime=2)
        self.wait(1)

        logo = ImageMobject("/home/diksha/Downloads/video_images/log_table.png").scale(0.5)
        logo.to_edge(RIGHT)
        self.play(FadeIn(logo))

        text3=Text("If we have to multiply\n"
                   "789*456\n"
                   "We will apply our newly invented log properties\n ",
                   color=YELLOW
                 ).scale(0.5).to_edge(LEFT)
        t2= MathTex(r"\log_{2}(789*456)=log_{2}(789)+log_{2}(456)").scale(0.5).to_edge(LEFT)
        t3=Text("Look at the log table and substitute the values..").scale(0.5).to_edge(LEFT)
        g=VGroup(text3,t2,t3)
        g.arrange(DOWN)
        g.next_to(logo,LEFT*6)
        self.play(Write(g),runtime=5)

class Log6(Scene):
    def construct(self):
        morning = Text("Applications:Richter Scale", font_size=30)
        self.wait()
        self.play(morning.animate.to_edge(UP), run_time=1)
        ul = Underline(morning)  # Underlining the word
        self.add(morning, ul)
        self.wait()
        text1=Text("It is used to measure the intensity of an earthquake.\n"
                   "The Richter scale is a base-10 logarithmic scale.",color=BLUE
                   ).scale(0.5).to_edge(LEFT)
        text3 = Text("Each order of magnitude is 10 times more intensive than the last one.", color=RED).scale(
            0.5).to_edge(LEFT)
        self.play(Write(text1))
        self.play(text1.animate.move_to(UP).to_edge(LEFT), runtime=2)
        self.wait(1)

        self.play(Write(text3))
        self.play(text3.animate.to_edge(LEFT), runtime=2)
        t1 = MathTex(r"\log_{10}(100)=2",color=YELLOW).to_edge(DOWN)
        t2 = MathTex(r"\log_{10}(1000)=3",color=YELLOW).to_edge(DOWN)
        g2=VGroup(t1,t2).to_edge(DOWN)
        g2.arrange(DOWN)
        # Create a surrounding rectangle for the quote
        quote_rect = SurroundingRectangle(g2, color=WHITE, buff=MED_LARGE_BUFF)

        # Play the creation animation
        self.play(Create(quote_rect), Write(g2), run_time=5)
        self.wait()
        quote_rect_target_position = quote_rect.get_bottom()
        quote_target_position = g2.get_bottom()
        self.play(
            quote_rect.animate.move_to(quote_rect_target_position),
            g2.animate.move_to(quote_target_position),
            quote_rect.animate.scale(0.85),
            g2.animate.scale(0.85),
            run_time=1
        )
        self.wait()
        g = VGroup(g2, quote_rect)
        self.play(g.animate.to_edge(DOWN), run_time=1)
        self.wait(5)

class Thumbnail(Scene):
    def construct(self):
        text=Text("Logarithms",font_size=100,color=WHITE,font=BOLD)
        text2=Text("What and How??",font_size=50,color=BLUE)
        g=VGroup(text,text2)
        g.arrange(DOWN)
        self.add(g)


class GridBackground(Scene):
    def construct(self):
        # Create a NumberPlane with denser grid lines and without axes
        grid = NumberPlane(
            x_range=(-7, 7, 0.45),  # x-axis range from -7 to 7 with a step of 0.5
            y_range=(-4, 4, 0.45),  # y-axis range from -4 to 4 with a step of 0.5
            axis_config={"include_numbers": False},  # Hide numbers on axes
            background_line_style={
                "stroke_color": BLUE_B,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )

        # Hide the axes

        grid.axes.set_stroke(opacity=0)  # Set axes opacity to 0 to hide them

        # Add the grid to the scene
        self.add(grid)

