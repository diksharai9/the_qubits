from manim import *

class ModelExplanationScene(Scene):
    def construct(self):
        # Title
        title = Text("What is a Model?", font="DejaVu Sans", font_size=36).to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Model box at the center
        model_box = Rectangle(width=3, height=1, color=BLUE, fill_opacity=0.2).move_to(ORIGIN)
        model_label = Text("Model", font="DejaVu Sans", font_size=24).next_to(model_box, UP, buff=0.1)
        self.play(Create(model_box), Write(model_label))
        self.wait(0.5)

        # Split the box into two halves and move them to the left
        self.play(FadeOut(model_box))
        top_half = Rectangle(width=3, height=0.5, color=BLUE, fill_opacity=0.2).move_to(model_label.get_bottom() + DOWN * 0.25)
        bot_half = Rectangle(width=3, height=0.5, color=BLUE, fill_opacity=0.2).move_to(model_label.get_bottom() + DOWN * 0.75)
        self.play(FadeIn(top_half), FadeIn(bot_half))
        self.wait(0.2)

        # Animate halves opening and move everything left
        self.play(
            top_half.animate.shift(UP * 0.5),
            bot_half.animate.shift(DOWN * 0.5),
            model_label.animate.shift(LEFT * 2),
            run_time=0.7
        )
        self.wait(0.3)

        # Reveal equation inside the model box (shifted appropriately)
        equation = MathTex(r"\hat y = w_{1}x_{1} + w_{2}x_{2} + \cdots + b") \
            .scale(0.8).move_to(model_label.get_bottom() + DOWN * 0.5).shift(RIGHT * 1.7)
        self.play(Write(equation))
        self.wait(1)

        # Label below the equation (shifted appropriately)
        eq_label = Text("Mathematical Equation", font="DejaVu Sans", font_size=24) \
            .next_to(equation, DOWN, buff=1).shift(RIGHT * 0.3)
        self.play(Write(eq_label))
        self.wait(0.5)

        # Slide everything right and shrink
        group = VGroup(top_half, bot_half, model_label, equation, eq_label)
        self.play(group.animate.scale(0.9).shift(LEFT * 2))
        self.wait(0.5)

        # Show X and Y on the right side of the screen
        x_text = Text("X = [Input Data]", font="DejaVu Sans", font_size=24) \
            .next_to(group, RIGHT, buff=1)
        y_text = Text("Y = [Predicted Output]", font="DejaVu Sans", font_size=24) \
            .next_to(x_text, DOWN, buff=0.5)
        self.play(Write(x_text), Write(y_text))
        self.wait(0.5)

        # "Saves to memory" at the bottom center
        mem_text = Text("Model saves to memory", font="DejaVu Sans", font_size=24,color=RED) \
            .next_to(y_text,DOWN)
        mem_icon = Square(side_length=0.4, color=GREEN).next_to(mem_text, RIGHT, buff=0.2)
        self.play(Write(mem_text), Create(mem_icon))
        self.wait(1)
