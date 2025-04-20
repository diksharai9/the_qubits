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
