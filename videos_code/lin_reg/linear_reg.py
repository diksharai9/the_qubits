from manim import *

class HoursVsMarksScene(Scene):
    def construct(self):
        # Title
        title = Text("Hours Studied vs. Marks Scored", font="Helvetica", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            x_length=8,
            y_length=5.5,
            axis_config={"color": WHITE},
            tips=False,
        ).to_edge(DOWN).shift(UP * 0.5)

        x_label = axes.get_x_axis_label("Hours", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label("Marks", edge=LEFT, direction=LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Sample data points (Hours studied, Marks scored)
        data_points = [
            (1, 30),
            (2, 40),
            (3, 50),
            (4, 55),
            (5, 65),
            (6, 70),
            (7, 80),
            (8, 88),
            (9, 92),
        ]

        # Plot points
        dots = VGroup()
        for x, y in data_points:
            dot = Dot(axes.c2p(x, y), color=BLUE)
            dots.add(dot)

        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.2), run_time=2)
        self.wait(1)

        # Regression line (visually approximated)
        regression_line = axes.plot(lambda x: 7 * x + 25, x_range=[0, 10], color=YELLOW)
        reg_label = MathTex(r"\hat{y} = 7x + 25", font_size=28).next_to(regression_line, UP).shift(RIGHT * 2)

        self.play(Create(regression_line), Write(reg_label))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(dots), FadeOut(regression_line), FadeOut(reg_label), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(title))
        self.wait(1)

from manim import *

class StudyHoursMarksTable(Scene):
    def construct(self):
        title = Text(
            "Hours Studied vs. Marks Scored",
            font="Helvetica-Bold",
            font_size=30
        ).to_edge(UP)  # or .to_edge(UP+RIGHT) if you want it over on the right

        # Now just write it in place
        self.play(Write(title))
        self.wait(1)
        # Table headers and data
        headers = ["Hours Studied", "Marks Scored"]
        data = [
            [1, 30],
            [2, 40],
            [3, 50],
            [4, 60],
            [5, 72],
            [6, 85],
        ]

        num_rows = len(data) + 1
        cell_width = 3
        cell_height = 0.8
        table_top = 2

        table_elements = VGroup()

        # Add headers
        for j, header in enumerate(headers):
            text = Text(header, font="Helvetica-Bold", font_size=25, color=BLUE)
            x = (-0.5 + j) * cell_width
            y = table_top
            text.move_to([x, y - cell_height / 2, 0])
            table_elements.add(text)

        # Add data
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                text = Text(str(item), font="Helvetica", font_size=23, color=YELLOW)
                x = (-0.5 + j) * cell_width
                y = table_top - (i + 1) * cell_height
                text.move_to([x, y - cell_height / 2, 0])
                table_elements.add(text)

        # Vertical and horizontal lines
        v_line = Line(
            start=UP * table_top,
            end=UP * (table_top - num_rows * cell_height),
            color=WHITE
        )

        h_line = Line(
            start=LEFT * cell_width + UP * (table_top - cell_height),
            end=RIGHT * cell_width + UP * (table_top - cell_height),
            color=WHITE
        )

        # Group table and lines
        full_table = VGroup(table_elements, v_line, h_line)

        # Play full table at center first
        self.play(FadeIn(full_table))
        self.wait(1.5)

        # Move and scale table to right
        self.play(
            full_table.animate.scale(0.8).to_edge(RIGHT),
            run_time=1.5
        )
        self.wait(1)

        # Create axes on the left
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            x_length=5.5,
            y_length=4,
            axis_config={"color": WHITE},
            tips=False,
        ).to_edge(LEFT*2.3).shift(DOWN * 0.5)

        x_label = Text("Hours", font="Helvetica", font_size=20,color=PINK)
        y_label = Text("Marks", font="Helvetica", font_size=20,color=PINK)

        # Position them relative to the axes
        x_label.next_to(axes.x_axis, DOWN)
        y_label.next_to(axes.y_axis, LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Sample points
        data_points = [
            (1, 30), (2, 40), (3, 50), (4, 55), (5, 65), (6, 70), (7, 80), (8, 88), (9, 92),
        ]

        dots = VGroup()
        for x, y in data_points:
            dot = Dot(axes.c2p(x, y), color=BLUE)
            dots.add(dot)

        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.2), run_time=2)
        self.wait(1)

        # Regression line
        regression_line = axes.plot(lambda x: 7 * x + 25, x_range=[0, 10], color=YELLOW)
        reg_label = MathTex(r"\hat{y} = 7x + 25", font_size=28).next_to(regression_line, UP).shift(RIGHT * 2)

        self.play(Create(regression_line), Write(reg_label))
        self.wait(2)

from manim import *

class LinearRegressionIntro(Scene):
    def construct(self):
        # Step 0: Show big question mark
        question_mark = Text("?", font="Helvetica-Bold", font_size=150, color=YELLOW)
        self.play(Write(question_mark))
        self.wait(1)

        # Replace with "Problem Statement"
        self.play(FadeOut(question_mark))
        problem_statement = Text("Problem Statement", font="Helvetica-Bold", font_size=40)
        self.play(FadeIn(problem_statement))
        self.wait(1)
        self.play(FadeOut(problem_statement))

        # Title
        title = Text("Finding an Algo", font="Helvetica-Bold", font_size=32, color=RED)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.to_edge(UP))

        # Show SVG of a student studying
        student = SVGMobject("study.svg").scale(1.5)
        student.to_edge(LEFT + DOWN)
        self.play(FadeIn(student, shift=LEFT + DOWN))
        self.wait(1)

        # Thought bubble with "More hours = Better marks?"
        thought = SVGMobject("cloud.svg").scale(1.2).next_to(student, RIGHT + UP, buff=0.3)
        idea = Text("More hours = Better marks?", font="Helvetica", font_size=15, color=BLUE).move_to(thought.get_center())

        self.play(FadeIn(thought), Write(idea))
        self.wait(1.5)

        # Replace thought with an equation
        self.play(FadeOut(idea))


        # Fade out everything and fade in next heading
        self.play(FadeOut(student), FadeOut(thought))



        # MODEL box
        model_box = Rectangle(width=3, height=1, color=RED)
        model_label = Text("Model", font="Helvetica-Bold", font_size=24).move_to(model_box.get_center())
        model_group = VGroup(model_box, model_label).move_to(DOWN * 1)
        self.play(Create(model_box), Write(model_label))
        self.wait(1)

        # Input and Output arrows
        input_text = Text("Input: Hours studied", font="Helvetica", font_size=20).next_to(model_box, LEFT, buff=1.5)
        output_text = Text("Output: Marks scored", font="Helvetica", font_size=20).next_to(model_box, RIGHT, buff=1.5)
        input_arrow = Arrow(start=input_text.get_right(), end=model_box.get_left(), color=GREEN)
        output_arrow = Arrow(start=model_box.get_right(), end=output_text.get_left(), color=BLUE)

        self.play(Write(input_text), Create(input_arrow))
        self.play(Write(output_text), Create(output_arrow))
        self.wait(2)
        group=VGroup(input_text,output_text,input_arrow,output_arrow,model_group)

        # Step 1: Introduce the thought of a relationship
        find_relation = Text(
            "Now, we want to find a relationship between them...",
            font="Helvetica", font_size=24
        )
        self.play(Write(find_relation))
        self.wait(2)

        # Step 2: Replace with idea of a simple relationship like y = x
        self.play(FadeOut(find_relation))
        simple_guess = MathTex("y = x", font_size=36)
        self.play(Write(simple_guess))
        self.wait(1.5)

        # Step 3: Realize this is too simple — fade it out
        self.play(FadeOut(simple_guess))

        # Step 4: Say we need tunable parameters (like slope & intercept)
        tuning_needed = Text(
            "But we need flexibility — tunable parameters!",
            font="Helvetica", font_size=24
        )
        self.play(Write(tuning_needed))
        self.wait(2)
        self.play(FadeOut(tuning_needed))

        # Step 5: Show the relation label
        relation = Text(
            "Simple Relation between two variables",
            font="Helvetica-Bold", font_size=20, color=YELLOW
        )
        self.play(Write(relation))
        self.wait(1)
        self.play(FadeOut(group))

        # Step 6: Then bring in the actual general equation just below
        eq = MathTex("y = mx + c", font_size=40).next_to(relation, DOWN, buff=0.3)
        self.play(Write(eq))
        self.wait(2)

        # Optional: Fade out when done
        self.play(FadeOut(relation), FadeOut(eq))

from manim import *

class ConceptOfLinearEquation(Scene):
    def construct(self):
        # Title
        title = Text("Understanding y = mx + c", font_size=34, color=YELLOW)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # Axes
        axes = Axes(
            x_range=[0, 6],
            y_range=[0, 60, 10],
            x_length=5,
            y_length=3.5,
            axis_config={"color": GREY},
            tips=False,
        ).shift(LEFT * 2)

        self.play(Create(axes))

        # Start with generic equation
        generic_eq = MathTex("y = mx + c", font_size=32).to_edge(RIGHT).shift(UP * 1)
        self.play(Write(generic_eq))
        self.wait(1)

        # Plot the actual line with m=5, c=10
        line = axes.plot(lambda x: 5 * x + 10, x_range=[0, 5.5], color=BLUE)
        self.play(Create(line))
        self.wait(1)

        # Show intercept (c)
        intercept_dot = Dot(axes.c2p(0, 10), color=RED)
        intercept_label = Text("Intercept (c)", font_size=20, color=RED).next_to(intercept_dot, LEFT)
        self.play(FadeIn(intercept_dot), Write(intercept_label))
        self.wait(1)

        # Show slope (m)
        p0 = axes.c2p(0, 10)
        p1 = axes.c2p(1, 15)
        slope_arrow = Arrow(p0, p1, color=YELLOW)
        slope_note = Text("1 hr → +5 marks", font_size=20, color=YELLOW).next_to(slope_arrow, RIGHT)
        slope_text = Text("Let's assume\n1 hr more study\nincreases marks by 5", font_size=20, color=WHITE).to_edge(
            RIGHT).shift(DOWN * 1.5)

        self.play(GrowArrow(slope_arrow), Write(slope_note))
        self.play(Write(slope_text))
        self.wait(2)

        # Transition to specific equation
        specific_eq = MathTex("y = 5x + 10", font_size=32).move_to(generic_eq)
        self.play(Transform(generic_eq, specific_eq))
        self.wait(2)
        # Fade everything for model comparison
        self.play(
            FadeOut(slope_arrow),
            FadeOut(slope_note),
            FadeOut(slope_text),
            FadeOut(intercept_label),
            FadeOut(intercept_dot),
            FadeOut(line),
            FadeOut(generic_eq),
            FadeOut(axes),
            FadeOut(title)
        )

        # Polynomial regression plot
        poly_axes = Axes(
            x_range=[-1, 1],
            y_range=[-4, 4, 2],
            x_length=6,
            y_length=3.5,
            axis_config={"color": GREY},
            tips=False
        ).shift(LEFT * 2)

        poly_eq = poly_axes.plot(lambda x: x**3 - 2*x, color=GREEN)
        poly_label = MathTex("y = x^3 - 2x", font_size=28).next_to(poly_eq, UP).shift(RIGHT * 0.5)

        self.play(Create(poly_axes), Create(poly_eq), Write(poly_label))
        self.wait(2)

        # Logistic regression plot
        self.play(FadeOut(poly_axes), FadeOut(poly_eq), FadeOut(poly_label))

        logistic_axes = Axes(
            x_range=[-6, 6],
            y_range=[0, 1, 0.2],
            x_length=6,
            y_length=3,
            axis_config={"color": GREY},
            tips=False
        ).shift(LEFT * 2)

        logistic_eq = logistic_axes.plot(lambda x: 1 / (1 + np.exp(-x)), color=ORANGE)
        logistic_label = MathTex("y = \\frac{1}{1 + e^{-x}}", font_size=28).next_to(logistic_eq, UP).shift(RIGHT * 1)

        self.play(Create(logistic_axes), Create(logistic_eq), Write(logistic_label))
        self.wait(3)


from manim import *


class TrainingVisualizationScene(Scene):
    def construct(self):
        # Table for the data
        data = [(1, 30), (2, 40), (3, 50), (4, 60), (5, 72), (6, 85)]
        table_data = [["Hours", "Marks"]] + [[str(x), str(y)] for x, y in data]
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"color": GREY},
            element_to_mobject=Text,
        ).scale(0.6).shift(LEFT * 3)

        self.play(Create(table))
        self.wait(1)

        # Slide and scale down the table
        self.play(
            table.animate.scale(0.5).to_edge(LEFT).shift(UP * 0.5),
        )
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[0, 7],
            y_range=[0, 100, 10],
            x_length=6,
            y_length=4.5,
            axis_config={"color": GREY},
            tips=False,
        ).to_edge(RIGHT, buff=1)
        x_label = axes.get_x_axis_label("Hours")
        y_label = axes.get_y_axis_label("Marks")

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # Data points
        dots = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in data])
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.2))
        self.wait(0.5)

        # Show bad guesses
        guesses = [
            (2, 5, GREY),
            (7, -10, GREY),
            (3, 20, GREY),
        ]
        for m_val, b_val, col in guesses:
            line = axes.plot(lambda x, m=m_val, b=b_val: m * x + b, x_range=[0, 6.5], color=col)
            sign = "+" if b_val >= 0 else "-"
            eq_str = f"y = {m_val}x {sign} {abs(b_val)}"
            label = MathTex(eq_str, font_size=24, color=col).next_to(line, UP, buff=0.1)
            self.play(Create(line), Write(label), run_time=1)
            self.wait(0.5)
            self.play(FadeOut(line), FadeOut(label))

        # # Text explanation of training
        # train_text = Text(
        #     "The goal is to minimize error:\nmake predicted marks close to actual marks.",
        #     font_size=24, line_spacing=1.5
        # ).next_to(axes, DOWN, buff=0.8)
        # self.play(Write(train_text))
        # self.wait(2)
        #
        # # Fade out all
        # self.play(
        #     FadeOut(table), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
        #     FadeOut(dots), FadeOut(train_text)
        # )
        # self.wait(0.5)
        #
        # # Final formulas — nice and colorful
        # formula1 = MathTex(
        #     r"m = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - (\sum x_i)^2}",
        #     font_size=30
        # ).set_color_by_tex("m", BLUE)
        #
        # formula2 = MathTex(
        #     r"b = \frac{\sum y_i - m \sum x_i}{n}",
        #     font_size=30
        # ).set_color_by_tex("b", GREEN)
        #
        # formulas = VGroup(formula1, formula2).arrange(DOWN, aligned_edge=LEFT).move_to(ORIGIN)
        #
        # self.play(Write(formula1))
        # self.wait(1)
        # self.play(Write(formula2))


from manim import *


class GradientDescentToClosedForm(Scene):
    def construct(self):
        # --- Left Side: Gradient Descent ---

        # Title
        gd_title = Text("Gradient Descent", font_size=32, color=RED_B)

        # Equations
        gd_eqs = VGroup(
            MathTex(r"m = m - \alpha \frac{\partial L}{\partial m}", font_size=26),
            MathTex(r"b = b - \alpha \frac{\partial L}{\partial b}", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        gd_group = VGroup(gd_title, gd_eqs).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        gd_group.to_edge(LEFT, buff=0.8)

        # Red box (no fill initially)
        gd_box = SurroundingRectangle(gd_group, color=RED, fill_opacity=0, buff=0.4)
        self.play(FadeIn(gd_group), Create(gd_box))
        self.wait(0.5)

        # --- Center: Arrow Transition ---
        arrow = Arrow(
            start=gd_box.get_right() + RIGHT * 0.4,
            end=gd_box.get_right() + RIGHT * 3.5,
            color=YELLOW, stroke_width=3, buff=0.1
        )
        arrow_label = Text("More Simple!", font_size=22, color=YELLOW).next_to(arrow, UP, buff=0.3)

        self.play(GrowArrow(arrow), FadeIn(arrow_label))

        # Now fill the red box
        self.play(gd_box.animate.set_fill(RED, opacity=0.08))
        self.wait(0.5)

        # --- Right Side: Closed-Form Solution ---
        cf_title = Text("Simple Formula", font_size=32, color=GREEN_B)

        cf_eqs = VGroup(
            MathTex(
                r"m = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - (\sum x_i)^2}",
                font_size=26
            ).set_color_by_tex("m", BLUE),
            MathTex(
                r"b = \frac{\sum y_i - m\,\sum x_i}{n}",
                font_size=26
            ).set_color_by_tex("b", GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        cf_group = VGroup(cf_title, cf_eqs).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        cf_group.next_to(arrow.get_end(), RIGHT, buff=0.6)

        # Green box (lighter fill)
        cf_box = SurroundingRectangle(cf_group, color=GREEN, fill_opacity=0.07, buff=0.4)
        cf_box.set_stroke(opacity=0.6)

        self.play(FadeIn(cf_group), Create(cf_box))
        self.wait(2)
from manim import *

class StepByStepLearningWithDataset(Scene):
    def construct(self):
        # --- Title ---
        title = Text("Error Reduction", font_size=20).to_edge(UP)
        self.play(Write(title))

        # --- Dataset Table ---
        headers = ["Hours (x)", "Marks (y)"]
        values = [(1, 30), (2, 40), (3, 50), (4, 60), (5, 72), (6, 85)]

        table = Table(
            [headers] + [[str(x), str(y)] for x, y in values],
            line_config={"stroke_width": 1},
            element_to_mobject=Text,
            h_buff=1.1
        ).scale(0.25).to_corner(UL, buff=0.6)

        self.play(Create(table))
        self.wait(0.5)

        # --- Axes + Points at Center ---
        axes = Axes(
            x_range=[0, 7, 1], y_range=[0, 90, 10],
            x_length=6.5, y_length=4.5,
            axis_config={"color": GREY},
            tips=False
        ).move_to(DOWN * 0.5)

        points = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW) for x, y in values])

        self.play(Create(axes), LaggedStartMap(FadeIn, points, lag_ratio=0.2))
        self.wait(0.5)

        # --- Step-by-Step Lines ---
        step_titles = ["Initial Guess", "Improved Guess", "Best Fit"]
        slopes_intercepts = [(3, 10), (4.5, 12), (5, 10)]
        colors = [RED, ORANGE, GREEN]  # For error lines

        eq_groups = VGroup()
        current_line = None
        current_label = None
        current_errors = None

        for i, (m, b) in enumerate(slopes_intercepts):
            # --- Plot line and equation label ---
            line = axes.plot(lambda x: m * x + b, color=colors[i])
            label = MathTex(f"y = {m}x + {b}", font_size=24, color=colors[i])
            label.next_to(line, UP)

            # --- Error lines from points to prediction ---
            errors = VGroup(*[
                DashedLine(
                    start=axes.c2p(x, y),
                    end=axes.c2p(x, m * x + b),
                    color=colors[i]
                ) for x, y in values
            ])

            # --- Right side text for step ---
            step_text = Text(step_titles[i], font_size=24, color=colors[i])
            math_eq = MathTex(f"y = {m}x + {b}", font_size=26, color=colors[i])
            side_group = VGroup(step_text, math_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            side_group.to_edge(RIGHT, buff=1).shift(DOWN * i * 1.2)
            eq_groups.add(side_group)

            # --- Animate each step ---
            if i == 0:
                self.play(Create(line), Write(label))
                self.play(Create(errors))
                self.play(FadeIn(side_group))
                current_line = line
                current_label = label
                current_errors = errors
            else:
                self.play(Transform(current_line, line), Transform(current_label, label))
                self.play(Transform(current_errors, errors))
                self.play(FadeIn(side_group))
            self.wait(0.8)

        self.wait(2)

from manim import *

class BiasVarianceVisualDemo(Scene):
    def construct(self):
        self.show_title("🎯 Bias, Variance, Underfitting & Overfitting")
        self.wait(1)
        self.bias_section()
        self.wait(1)
        self.variance_section()
        self.wait(1)
        self.underfitting_section()
        self.wait(1)
        self.overfitting_section()
        self.wait(1)
        self.best_model_section()
        self.wait(2)

    def show_title(self, text):
        title = Text(text, font_size=34,color=RED).to_edge(UP)
        self.play(Write(title))

    def clear_screen(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def bias_section(self):
        self.clear_screen()
        heading = Text("📌 Bias – Wrong Thinking", font_size=30, color=RED).to_edge(UP)
        line_explain = Text("Assumes same output for all inputs", font_size=24).next_to(heading, DOWN)

        character = SVGMobject("study.svg").scale(2).to_edge(LEFT)
        thought = Text("Everyone scores 50!", font_size=24).next_to(character, RIGHT).shift(RIGHT * 0.5)

        axes = Axes(x_range=[0, 7], y_range=[0, 100, 20], x_length=5, y_length=3.2, tips=False)
        axes.to_edge(RIGHT * 1.2)
        line = axes.plot(lambda x: 50, color=RED)
        eq = MathTex("y = 50", font_size=26).next_to(line, UP)

        eg = Text("💼 Predict all salaries as ₹50k", font_size=24).to_edge(DOWN)

        self.play(FadeIn(heading), FadeIn(line_explain))
        self.play(FadeIn(character), Write(thought))
        self.play(Create(axes), Create(line), Write(eq))
        self.play(FadeIn(eg))
        self.wait(1)

    def variance_section(self):
        self.clear_screen()
        heading = Text("📌 Variance – Overthinking", font_size=30, color=BLUE).to_edge(UP)
        explain = Text("Fits too closely to training data", font_size=24).next_to(heading, DOWN)

        character = SVGMobject("think.svg").scale(2).to_edge(LEFT)
        thought = Text("Every point needs a new rule!", font_size=22).next_to(character, RIGHT).shift(RIGHT * 0.5)

        axes = Axes(x_range=[0, 7], y_range=[0, 120, 20], x_length=5, y_length=3.2, tips=False)
        axes.to_edge(RIGHT * 1.2)
        dots = VGroup(*[Dot(axes.c2p(x, 10 * x + (x % 2) * 15), color=YELLOW) for x in range(1, 7)])
        curve = axes.plot(lambda x: 10 * x + (x % 2) * 15, color=BLUE)

        eg = Text("📱 Trying to cover all data points at once", font_size=24).to_edge(DOWN)

        self.play(FadeIn(heading), FadeIn(explain))
        self.play(FadeIn(character), Write(thought))
        self.play(Create(axes), FadeIn(dots), Create(curve))
        self.play(FadeIn(eg))
        self.wait(1)

    def underfitting_section(self):
        self.clear_screen()
        heading = Text("📉 Underfitting = Too Dumb", font_size=30, color=GREY).to_edge(UP)
        explain = Text("Model too simple to learn", font_size=24).next_to(heading, DOWN)

        character = SVGMobject("think.svg").scale(2).to_edge(LEFT )
        thought = Text("I’ll just guess 10 for everyone!", font_size=22).next_to(character, RIGHT).shift(RIGHT * 0.5)

        axes = Axes(x_range=[0, 7], y_range=[0, 100, 20], x_length=5, y_length=3.2, tips=False)
        axes.to_edge(RIGHT * 1.2)
        line = axes.plot(lambda x: 10, color=GREY)
        eq = MathTex("y = 10", font_size=26).next_to(line, UP)

        eg = Text("😅 Student who didn't study at all", font_size=24).to_edge(DOWN)

        self.play(FadeIn(heading), FadeIn(explain))
        self.play(FadeIn(character), Write(thought))
        self.play(Create(axes), Create(line), Write(eq))
        self.play(FadeIn(eg))
        self.wait(1)

    def overfitting_section(self):
        self.clear_screen()
        heading = Text("📈 Overfitting = Too Smart", font_size=30, color=ORANGE).to_edge(UP)
        explain = Text("Memorizes data but fails on new data", font_size=24).next_to(heading, DOWN)

        character = SVGMobject("think.svg").scale(2).to_edge(LEFT)
        thought = Text("I’ll write 10 rules for 5 points!", font_size=22).next_to(character, RIGHT).shift(RIGHT * 0.5)

        axes = Axes(x_range=[0, 7], y_range=[0, 120, 20], x_length=5, y_length=3.2, tips=False)
        axes.to_edge(RIGHT * 1.2)
        dots = VGroup(*[Dot(axes.c2p(x, 10 * x + (x % 2) * 15), color=YELLOW) for x in range(1, 7)])
        curve = axes.plot(lambda x: 10 * x + (x % 2) * 15, color=ORANGE)

        eg = Text("🧠 Student memorizing random trends", font_size=24).to_edge(DOWN)

        self.play(FadeIn(heading), FadeIn(explain))
        self.play(FadeIn(character), Write(thought))
        self.play(Create(axes), FadeIn(dots), Create(curve))
        self.play(FadeIn(eg))
        self.wait(1)

    def best_model_section(self):
        self.clear_screen()
        heading = Text("✅ Best Model = Balanced Thinking", font_size=30, color=GREEN).to_edge(UP)
        explain = Text("Understands trends, generalizes well", font_size=24).next_to(heading, DOWN)

        character = SVGMobject("study.svg").scale(2).to_edge(LEFT)
        thought = Text("I get the pattern!", font_size=24).next_to(character, RIGHT).shift(RIGHT * 0.5)

        axes = Axes(x_range=[0, 7], y_range=[0, 100, 20], x_length=5.5, y_length=3.5, tips=False)
        axes.to_edge(RIGHT * 1.2)
        dots = VGroup(*[Dot(axes.c2p(x, 10 * x + 5), color=YELLOW) for x in range(1, 7)])
        line = axes.plot(lambda x: 10 * x + 5, color=GREEN)
        eq = MathTex("y = 10x + 5", font_size=26).next_to(line, UP)

        eg = Text("🎓 Student who understands concepts", font_size=24).to_edge(DOWN)

        self.play(FadeIn(heading), FadeIn(explain))
        self.play(FadeIn(character), Write(thought))
        self.play(Create(axes), FadeIn(dots), Create(line), Write(eq))
        self.play(FadeIn(eg))
        self.wait(1)
