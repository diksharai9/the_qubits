from manim import *
from manim.utils.color.BS381 import CRIMSON


class ConditionalLogicScene(Scene):
    def construct(self):
        # Title
        title = Text("How Computers Make Decisions", font_size=35)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Code lines
        line1 = Text("if input == 'apple':", font="Courier New", font_size=28, color=YELLOW)
        line2 = Text("    print('Fruit selected')", font="Courier New", font_size=28, color=GREEN)
        line3 = Text("elif input == 'carrot':", font="Courier New", font_size=28, color=YELLOW)
        line4 = Text("    print('Vegetable selected')", font="Courier New", font_size=28, color=GREEN)
        line5 = Text("else:", font="Courier New", font_size=28, color=YELLOW)
        line6 = Text("    raise Error('Invalid input')", font="Courier New", font_size=28, color=RED)

        # Stack code vertically
        code_block = VGroup(line1, line2, line3, line4, line5, line6).arrange(DOWN, aligned_edge=LEFT)
        code_block.move_to(ORIGIN)

        # Box and label
        code_box = SurroundingRectangle(code_block, color=BLUE, buff=0.4)
        code_label = Text("Code", font_size=30, color=WHITE).next_to(code_box, DOWN)

        # Write each line
        for line in code_block:
            self.play(Write(line), run_time=0.4)
            self.wait(0.2)

        # Create box and label
        self.play(Create(code_box), Write(code_label))
        self.wait(1)

        # Slide everything to the left
        group = VGroup(code_block, code_box, code_label)
        self.play(group.animate.shift(LEFT * 2))
        self.wait(0.8)
        group = VGroup(code_block, code_box)

        # Input (correct)
        correct_input = Text("Input: apple ✅", color=GREEN, font_size=32).next_to(code_box, RIGHT).shift(UP * 0.5)
        self.play(Write(correct_input))
        self.wait(1.4)

        # Remove correct input
        self.play(FadeOut(correct_input))
        self.wait(0.5)

        # Input (wrong)
        wrong_input = Text("Input: pizza ❌", color=RED, font_size=32).next_to(code_box, RIGHT).shift(UP * 0.5)
        self.play(Write(wrong_input))
        self.wait(0.5)

        # Highlight error line
        error_box = SurroundingRectangle(line6, color=RED, buff=0.2)
        self.play(Create(error_box))
        self.play(FadeOut(code_label))

        # Error message
        error_text = Text("Error: Invalid input", color=CRIMSON, font_size=30).next_to(error_box, DOWN)
        self.play(Write(error_text))
        self.wait(2)

        # Cleanup
        self.play(*[FadeOut(mob) for mob in [title, group, wrong_input, error_box, error_text]])
        self.wait(1)
