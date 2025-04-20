from manim import *

class LinearRegressionLearning(Scene):
    def construct(self):
        # Title
        title = Text("Linear Regression: Learning from Error", font="DejaVu Sans", font_size=30)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Axes setup
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 40, 5],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=5,
            tips=False
        )

        x_label = axes.get_x_axis_label("Bike Features (x)", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label("Price (y)", edge=LEFT, direction=LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Training data points (x, y)
        data_points = [
            Dot(axes.c2p(1, 5), color=YELLOW),
            Dot(axes.c2p(2, 10), color=YELLOW),
            Dot(axes.c2p(3, 15), color=YELLOW),
            Dot(axes.c2p(4, 20), color=YELLOW),
            Dot(axes.c2p(5, 25), color=YELLOW),
            Dot(axes.c2p(6, 30), color=YELLOW),
        ]
        self.play(*[FadeIn(dot) for dot in data_points])
        self.wait(1)

        # Wrong prediction line
        wrong_line = axes.plot(lambda x: 9 * x - 9, x_range=[0, 5], color=RED)
        wrong_label = MathTex(r"\hat{y} = 10x - 10", font_size=28).next_to(wrong_line, UP)
        self.play(Create(wrong_line), Write(wrong_label))
        self.wait(1)

        # Show error
        error_text = Text("High Error!", font="DejaVu Sans", font_size=20, color=RED)
        error_text.next_to(wrong_line, RIGHT*2).shift(RIGHT)
        self.play(FadeIn(error_text))
        self.wait(1.5)
        self.play(FadeOut(error_text))

        # Model correcting itself
        correct_line = axes.plot(lambda x: 5 * x, x_range=[0, 7], color=GREEN)
        correct_label = MathTex(r"\hat{y} = 5x", font_size=28).next_to(correct_line, UP)

        self.play(Transform(wrong_line, correct_line), Transform(wrong_label, correct_label))
        self.wait(1)

        # Success message
        success = Text("Model Learned Correctly!", font="DejaVu Sans", font_size=28, color=GREEN)
        success.to_edge(DOWN)
        self.play(Write(success))
        self.wait(2)
