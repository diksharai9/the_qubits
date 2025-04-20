from manim import *

class PaperAnimation(Scene):
    def construct(self):
        # Create a rectangle to simulate a piece of paper
        paper = Rectangle(width=6, height=8, color=BLACK, fill_opacity=1, fill_color=WHITE)
        paper.shift(DOWN)

        # Add some hand-drawn-like text
        text = Text("Hello, World!", font="Comic Sans MS").scale(0.5)
        text.shift(UP * 2)

        # Draw a hand-drawn-like circle
        circle = Circle(radius=1, color=BLACK)
        circle.shift(DOWN * 2)

        # Animate the text and the circle to create a paper animation effect
        self.play(DrawBorderThenFill(paper), run_time=2)
        self.play(Write(text), run_time=2)
        self.play(Create(circle), run_time=2)
        self.wait(2)

        # Simulate a page turn effect
        self.play(
            Rotate(paper, angle=PI / 2, axis=RIGHT),
            Rotate(text, angle=PI / 2, axis=RIGHT),
            Rotate(circle, angle=PI / 2, axis=RIGHT),
            run_time=2
        )
        self.wait(2)

if __name__ == "__main__":
    scene = PaperAnimation()
    scene.render()
