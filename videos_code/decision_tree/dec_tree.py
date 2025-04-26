from manim import *

class DecisionTreeIntro(Scene):
    def construct(self):
        # 1) Title: "Decision Tree" in big red bold, then fade out more slowly
        title = Text("CLASSIFICATION", font_size=90, color=RED,weight=BOLD)
        self.play(Write(title, run_time=2))
        self.wait(1.5)
        self.play(FadeOut(title, run_time=1.5))
        self.wait(0.5)


        header_text = Text("Let’s Start with a Problem", font_size=40)
        header_text.to_edge(UP)
        self.play(FadeIn(header_text, run_time=2))
        self.wait(1)

        # 3) Feature boxes (Marks, Attendance, Extra-curriculars)
        def make_feature_box(text):
            box = RoundedRectangle(
                width=3, height=1.2, corner_radius=0.1,
                stroke_color=BLUE, fill_color=BLUE, fill_opacity=0.1
            )
            label = Text(text, font_size=22, line_spacing=0.2)
            label.move_to(box.get_center())
            return VGroup(box, label)

        marks_group = make_feature_box("Marks\n(out of 100)")
        attendance_group = make_feature_box("Attendance\n(%)")
        extra_group = make_feature_box("Extra-curriculars\n(Yes/No)")

        features = VGroup(marks_group, attendance_group, extra_group)
        features.arrange(RIGHT, buff=1.5).scale(0.9)
        features.next_to(header_text, DOWN, buff=1)
        self.play(LaggedStartMap(FadeIn, features, shift=UP, lag_ratio=0.3, run_time=2.5))
        self.wait(1)

        # 4) Arrow pointing down to outcomes
        arrow = Arrow(
            start=features.get_bottom(),
            end=features.get_bottom() + DOWN * 1.5,
            buff=0
        )
        self.play(GrowArrow(arrow, run_time=1.8))
        self.wait(1)

        # 5) Outcome boxes: Admitted (green stroke) and Rejected (red stroke)
        def make_outcome_box(text, stroke_color):
            box = RoundedRectangle(
                width=3, height=1.2, corner_radius=0.1,
                stroke_color=stroke_color,
                fill_color=BLUE, fill_opacity=0.1
            )
            label = Text(text, font_size=24)
            label.move_to(box.get_center())
            return VGroup(box, label)

        admit_group = make_outcome_box("Admitted", GREEN)
        reject_group = make_outcome_box("Rejected", RED)

        outcomes = VGroup(admit_group, reject_group)
        outcomes.arrange(RIGHT, buff=2).scale(0.9)
        outcomes.next_to(arrow, DOWN, buff=1)
        self.play(LaggedStartMap(FadeIn, outcomes, shift=UP, lag_ratio=0.3, run_time=2.5))
        self.wait(1.5)


        note_text = Text(
            "Predicting categories → Classification",
            font_size=24
        )
        note_text.to_edge(DOWN)
        self.play(FadeIn(note_text, run_time=2.5))
        self.wait(2)
from manim import *

class DecisionTreeDataTable(Scene):
    def construct(self):
        # 1) Table data: 2D list with header + rows
        data = [
            ["Marks", "Attendance", "Extra-curriculars", "Decision"],
            ["92", "96", "Yes", "Admit"],
            ["85", "90", "No", "Admit"],
            ["40", "65", "No", "Reject"],
            ["72", "80", "Yes", "Admit"],
            ["30", "50", "No", "Reject"],
        ]

        # 2) Create full-screen table first
        table = Table(
            table=data,
            include_outer_lines=False,
            line_config={"stroke_width": 1.5},
            element_to_mobject=lambda item: Text(item, color=BLUE),
        )
        table.scale(0.75)

        # 3) Show full-size table first
        self.play(FadeIn(table, run_time=2))
        self.wait(1)

        # 4) Animate shrinking and shifting to the right
        self.play(
            table.animate.scale(0.5).shift(RIGHT * 2),
            run_time=2
        )
        self.wait(1)

        # 3) Add a brain SVG to the left
        brain = SVGMobject("brain.svg")
        brain.scale(1.5)
        brain.next_to(table, LEFT, buff=1)

        self.play(DrawBorderThenFill(brain, run_time=2))
        self.wait(2)

from manim import *

class ShiftedCleanDecisionTree(Scene):
    def construct(self):
        # Title
        title = Text("Decision Tree", color=RED, weight=BOLD).scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).to_edge(UP), run_time=1.5)
        self.wait(0.5)

        # Constants
        BOX_WIDTH = 1.5
        BOX_HEIGHT = 1.0

        def uniform_box(text, text_size=20, color=BLUE):
            t = Text(text, font_size=text_size)
            box = RoundedRectangle(width=BOX_WIDTH, height=BOX_HEIGHT,
                                   corner_radius=0.2,
                                   color=color, fill_color=color,
                                   fill_opacity=0.1)
            return VGroup(box, t.move_to(box.get_center()))

        # Nodes
        root = uniform_box("Marks > 60?", 15)
        root.next_to(title,DOWN+LEFT,buff=0.9)
        reject_left = uniform_box("Reject", 18, RED)
        attend = uniform_box("Attendance \n> 75%?", 15)
        admit = uniform_box("Admit", 18, GREEN)
        extracurriculars = uniform_box("Extra-\ncurriculars?", 15)
        admit_extra = uniform_box("Admit", 18, GREEN)
        reject_extra = uniform_box("Reject", 18, RED)

        # Positioning
        root.move_to(UP * 2.5)
        reject_left.next_to(root, DOWN, buff=1).shift(LEFT * 2)
        attend.next_to(root, DOWN, buff=1).shift(RIGHT * 2)

        admit.next_to(attend, DOWN, buff=0.8).shift(LEFT * 1.2)
        extracurriculars.next_to(attend, DOWN, buff=0.8).shift(RIGHT * 1.2)

        admit_extra.next_to(extracurriculars, DOWN, buff=0.8).shift(LEFT * 0.8)
        reject_extra.next_to(extracurriculars, DOWN, buff=0.8).shift(RIGHT * 0.8)

        # Arrows
        arrow1 = Arrow(start=root.get_bottom(), end=reject_left.get_top(), stroke_width=2)
        arrow2 = Arrow(start=root.get_bottom(), end=attend.get_top(), stroke_width=2)

        arrow3 = Arrow(start=attend.get_bottom(), end=admit.get_top(), stroke_width=2)
        arrow4 = Arrow(start=attend.get_bottom(), end=extracurriculars.get_top(), stroke_width=2)

        arrow5 = Arrow(start=extracurriculars.get_bottom(), end=admit_extra.get_top(), stroke_width=2)
        arrow6 = Arrow(start=extracurriculars.get_bottom(), end=reject_extra.get_top(), stroke_width=2)

        # Labels — manually placed near arrows, not on boxesShiftedCleanDecisionTree
        yes1 = Text("Yes", font_size=20).next_to(arrow2, LEFT, buff=0.1).shift(LEFT*1.19+UP * 0.1)
        no1 = Text("No", font_size=20).next_to(arrow1, RIGHT, buff=0.1).shift(RIGHT*1.19+UP * 0.1)

        yes2 = Text("Yes", font_size=20).next_to(arrow3, LEFT, buff=0.1).shift(UP * 0.1)
        no2 = Text("No", font_size=20).next_to(arrow4, RIGHT, buff=0.1).shift(UP * 0.1)

        yes3 = Text("Yes", font_size=20).next_to(arrow5, LEFT, buff=0.1).shift(UP * 0.1)
        no3 = Text("No", font_size=20).next_to(arrow6, RIGHT, buff=0.1).shift(UP * 0.1)

        # Group and shift left
        tree_group = VGroup(root, reject_left, attend, admit, extracurriculars,
                            admit_extra, reject_extra,
                            arrow1, arrow2, arrow3, arrow4, arrow5, arrow6,
                            yes1, no1, yes2, no2, yes3, no3)
        tree_group.shift(LEFT * 1.5)

        # Animate
        self.play(FadeIn(root))
        self.wait(0.5)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.play(FadeIn(reject_left), FadeIn(attend))
        self.play(FadeIn(yes1), FadeIn(no1))
        self.wait(0.5)

        self.play(GrowArrow(arrow3), GrowArrow(arrow4))
        self.play(FadeIn(admit), FadeIn(extracurriculars))
        self.play(FadeIn(yes2), FadeIn(no2))
        self.wait(0.5)

        self.play(GrowArrow(arrow5), GrowArrow(arrow6))
        self.play(FadeIn(admit_extra), FadeIn(reject_extra))
        self.play(FadeIn(yes3), FadeIn(no3))
        self.wait(3)

from manim import *

class DecisionTreeSplitExplained(Scene):
    def construct(self):
        # Title
        title = Text("How a Decision Tree Picks the Best Split", color=BLUE_B).scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Marks and labels
        data_points = [
            (30, "Reject 🔴"),
            (40, "Reject 🔴"),
            (72, "Admit 🟢"),
            (85, "Admit 🟢"),
            (92, "Admit 🟢")
        ]

        # Horizontal line for number line
        line = NumberLine(x_range=[20, 100, 10], length=10, include_ticks=True, include_numbers=True)
        line.to_edge(DOWN).shift(UP * 3.5)
        self.play(Create(line))

        # Plot data points
        dots = []
        labels = []
        for x, label in data_points:
            dot = Dot(point=line.n2p(x), color=RED if "Reject" in label else GREEN)
            text = Text(label, font_size=20).next_to(dot, UP)
            dots.append(dot)
            labels.append(text)

        self.play(*[FadeIn(d) for d in dots], *[FadeIn(t) for t in labels])
        self.wait(1)

        # Midpoints
        midpoints = [
            (35, "🔍"),
            (56, "✅ Best!"),
            (78.5, "?"),
            (88.5, "?")
        ]

        midlines = []
        midlabels = []

        for val, tag in midpoints:
            x = line.n2p(val)[0]
            vline = DashedLine(start=[x, line.get_bottom()[1] - 0.3, 0], end=[x, line.get_top()[1] + 0.3, 0], color=YELLOW)
            label = Text(tag, font_size=24, color=YELLOW).next_to(vline, UP)
            midlines.append(vline)
            midlabels.append(label)

        self.play(*[Create(l) for l in midlines], *[FadeIn(t) for t in midlabels])
        self.wait(1.5)

        # Highlight the perfect split at 56
        best_line = midlines[1]
        best_tag = Text("Perfect Split!", font_size=30, color=GREEN).next_to(best_line, UP, buff=0.8)
        self.play(Write(best_tag))
        self.wait(1)

        # Baskets
        basket_left = Rectangle(width=2.5, height=1.2, color=RED, fill_opacity=0.1).next_to(best_line, DOWN, buff=2).shift(LEFT*1.7)
        basket_right = Rectangle(width=3.5, height=1.2, color=GREEN, fill_opacity=0.1).next_to(best_line, DOWN, buff=2).shift(RIGHT*1.7)
        label_left = Text("Reject 🔴", font_size=24).next_to(basket_left, UP, buff=0.1)
        label_right = Text("Admit 🟢", font_size=24).next_to(basket_right, UP, buff=0.1)

        self.play(Create(basket_left), Create(basket_right), FadeIn(label_left), FadeIn(label_right))

        # Move points into baskets to show clean split
        self.play(
            dots[0].animate.move_to(basket_left.get_center() + LEFT * 0.5),
            dots[1].animate.move_to(basket_left.get_center() + RIGHT * 0.5),
            dots[2].animate.move_to(basket_right.get_center() + LEFT * 1.2),
            dots[3].animate.move_to(basket_right.get_center()),
            dots[4].animate.move_to(basket_right.get_center() + RIGHT * 1.2),
        )
        self.wait(3)

from manim import *

class FeatureSplitSequence(Scene):
    def construct(self):
        # Title
        title = Text("Which Feature?", color=RED_B).scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.7).to_edge(UP), run_time=1.2)

        # === Data ===
        marks_data = [
            ["Marks", "Outcome"],
            ["30", "Reject"],
            ["40", "Reject"],
            ["72", "Admit"],
            ["85", "Admit"],
            ["92", "Admit"]
        ]
        attendance_data = [
            ["Attendance", "Outcome"],
            ["60%", "Reject"],
            ["55%", "Reject"],
            ["80%", "Admit"],
            ["90%", "Admit"],
            ["95%", "Admit"]
        ]
        extracurriculars_data = [
            ["Extracurriculars", "Outcome"],
            ["No", "Reject"],
            ["No", "Reject"],
            ["Yes", "Admit"],
            ["Yes", "Admit"],
            ["Yes", "Admit"]
        ]

        def create_feature_table(data):
            table = Table(
                table=data,
                include_outer_lines=False,
                line_config={"stroke_width": 1.5},
                element_to_mobject=lambda item: Text(item, color=BLUE, font_size=25)
            ).scale(0.65)

            for line in table.get_horizontal_lines():
                line_width = 2.5
                center = line.get_center()
                line.set_points_as_corners([
                    center + LEFT * line_width / 1.2,
                    center + RIGHT * line_width / 1.2
                ])
            return table

        # Tables
        marks_table = create_feature_table(marks_data).to_edge(LEFT).shift(DOWN * 0.5)
        attendance_table = create_feature_table(attendance_data).shift(DOWN * 0.5)
        extra_table = create_feature_table(extracurriculars_data).to_edge(RIGHT).shift(DOWN * 0.5)

        self.play(FadeIn(marks_table), FadeIn(attendance_table), FadeIn(extra_table))
        self.wait(2)

        # === Show Split for MARKS ===
        self.show_split(
            table=marks_table,
            values=[(30, "Reject 🔴"), (40, "Reject 🔴"), (72, "Admit 🟢"), (85, "Admit 🟢"), (92, "Admit 🟢")],
            split_val=56,
            split_tag="Perfect Split!"
        )

        # === Show Split for ATTENDANCE ===
        self.show_split(
            table=attendance_table,
            values=[(55, "Reject 🔴"), (60, "Reject 🔴"), (80, "Admit 🟢"), (90, "Admit 🟢"), (95, "Admit 🟢")],
            split_val=70,
            split_tag="Best Info Gain"
        )

        # === Show Split for EXTRACURRICULARS ===
        self.show_split(
            table=extra_table,
            values=[(0, "Reject 🔴"), (0, "Reject 🔴"), (1, "Admit 🟢"), (1, "Admit 🟢"), (1, "Admit 🟢")],
            split_val=0.5,
            split_tag="Clear Separation"
        )

        self.wait(2)

    def show_split(self, table, values, split_val, split_tag):
        self.play(FadeOut(table))
        self.wait(0.3)

        # Create NumberLine in same position
        number_line = NumberLine(x_range=[min(v[0] for v in values) - 10, max(v[0] for v in values) + 10, 10],
                                 length=4.5, include_ticks=True, include_numbers=True,font_size=10)
        number_line.move_to(table.get_center())
        self.play(Create(number_line))

        # Plot points
        dots = []
        labels = []
        for val, label in values:
            dot = Dot(point=number_line.n2p(val), color=RED if "Reject" in label else GREEN)
            text = Text(label, font_size=8).next_to(dot, UP, buff=0.15)
            dots.append(dot)
            labels.append(text)
        self.play(*[FadeIn(d) for d in dots], *[FadeIn(t) for t in labels])
        self.wait(0.5)

        # Split line
        x = number_line.n2p(split_val)[0]
        split_line = DashedLine(
            start=[x, number_line.get_bottom()[1] - 0.3, 0],
            end=[x, number_line.get_top()[1] + 0.3, 0],
            color=YELLOW
        )
        split_label = Text(split_tag, font_size=24, color=YELLOW).next_to(split_line, UP, buff=0.3)
        self.play(Create(split_line), FadeIn(split_label))

        # Baskets
        basket_left = Rectangle(width=1.5, height=1, color=RED, fill_opacity=0.1).next_to(split_line, DOWN, buff=1.5).shift(LEFT * 1)
        basket_right = Rectangle(width=2.3, height=1, color=GREEN, fill_opacity=0.1).next_to(split_line, DOWN, buff=1.5).shift(RIGHT * 1)
        label_left = Text("Reject 🔴", font_size=20).next_to(basket_left, UP, buff=0.1)
        label_right = Text("Admit 🟢", font_size=20).next_to(basket_right, UP, buff=0.1)
        self.play(Create(basket_left), Create(basket_right), FadeIn(label_left), FadeIn(label_right))

        # Move dots
        reject_index = [i for i, v in enumerate(values) if "Reject" in v[1]]
        admit_index = [i for i, v in enumerate(values) if "Admit" in v[1]]

        for i, idx in enumerate(reject_index):
            self.play(dots[idx].animate.move_to(basket_left.get_center() + LEFT * (0.3 * (len(reject_index) - i))))
        for i, idx in enumerate(admit_index):
            self.play(dots[idx].animate.move_to(basket_right.get_center() + RIGHT * (0.3 * i)))

        self.wait(1)
        self.play(FadeOut(*dots), FadeOut(*labels), FadeOut(split_line), FadeOut(split_label),
                  FadeOut(basket_left), FadeOut(basket_right), FadeOut(label_left), FadeOut(label_right),
                  FadeOut(number_line))
        self.wait(0.3)

from manim import *

class FeatureSplitScene(Scene):
    def construct(self):
        # Step 1: Main "Feature Split" box
        main_box = Rectangle(width=6, height=1.5, color=BLUE, fill_opacity=0.1)
        main_text = Text("Feature Split", font="Arial", font_size=36)
        main_group = VGroup(main_box, main_text).move_to(ORIGIN)
        original_main_pos = main_group.get_center()

        self.play(Create(main_box), Write(main_text))
        self.wait(0.5)
        self.play(main_group.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)

        # Step 2: Three methods below
        ig_box = Rectangle(width=3, height=1, color=GREEN, fill_opacity=0.1)
        ig_text = Text("Information Gain", font="Arial", font_size=24).move_to(ig_box.get_center())
        gini_box = Rectangle(width=3, height=1, color=YELLOW, fill_opacity=0.1)
        gini_text = Text("Gini Index", font="Arial", font_size=24).move_to(gini_box.get_center())
        chi_box = Rectangle(width=3, height=1, color=RED, fill_opacity=0.1)
        chi_text = Text("Chi Square", font="Arial", font_size=24).move_to(chi_box.get_center())

        ig_group = VGroup(ig_box, ig_text)
        gini_group = VGroup(gini_box, gini_text)
        chi_group = VGroup(chi_box, chi_text)

        type_group = VGroup(ig_group, gini_group, chi_group).arrange(RIGHT, buff=1).next_to(main_group, DOWN, buff=0.8)

        self.play(LaggedStartMap(FadeIn, type_group, shift=DOWN), run_time=1.5)
        self.wait(0.5)

        # Step 3: Highlight "Information Gain", enlarge and move to top, fade out others
        self.play(
            FadeOut(gini_group),
            FadeOut(chi_group), FadeOut(main_group),
            ig_group.animate.scale(1.3)
        )
        self.play(
            ig_group.animate.scale(1.3).move_to(original_main_pos)
        )

        self.wait(0.3)
        self.play(ig_group.animate.scale(1.5).to_edge(UP, buff=1.2))
        self.wait(1)


import numpy as np
from manim import *

class CompareAllFeatures(Scene):
    def construct(self):
        # Title
        title = Text("Evaluating Features in Decision Trees", font_size=36, color=RED)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Full data
        data = [
            ["Marks", "Attendance", "Extra-curriculars", "Decision"],
            ["92", "88", "No", "Admit"],
            ["85", "90", "Yes", "Admit"],
            ["72", "60", "No", "Admit"],
            ["40", "95", "Yes", "Reject"],
            ["30", "70", "Yes", "Reject"],
        ]

        # Full table
        table = Table(
            table=data,
            include_outer_lines=False,
            line_config={"stroke_width": 1.5},
            element_to_mobject=lambda item: Text(item, color=BLUE),
        )
        table.scale(0.75)

        # Show full-size table
        self.play(FadeIn(table, run_time=2))
        self.wait(1)

        # Shrink and shift full table to right
        self.play(
            table.animate.scale(0.5).shift(RIGHT * 2),
            run_time=2
        )
        self.wait(1)

        # 1️⃣ HIGHLIGHT the Marks and Decision columns
        marks_col = table.get_columns()[0]  # Marks column (index 0)
        decision_col = table.get_columns()[-1]  # Decision column (last index)

        highlight_rects = VGroup(
            SurroundingRectangle(marks_col, color=YELLOW),
            SurroundingRectangle(decision_col, color=YELLOW)
        )
        self.play(Create(highlight_rects))
        self.wait(1)

        # 2️⃣ Create copies for animation
        marks_col_copy = marks_col.copy()
        decision_col_copy = decision_col.copy()

        # 3️⃣ Animate them sliding left and forming rough two-column layout
        self.play(
            marks_col_copy.animate.scale(1.0).move_to(LEFT * 5),
            decision_col_copy.animate.scale(1.0).move_to(LEFT * 3.8),
            run_time=2
        )
        self.wait(0.5)

        # 4️⃣ Group the moved copies together
        marks_decision_group = VGroup(marks_col_copy, decision_col_copy)

        # 5️⃣ Create the clean Marks-only table
        marks_data = [
            ["Marks", "Decision"],
            ["92", "Admit"],
            ["85", "Admit"],
            ["72", "Admit"],
            ["40", "Reject"],
            ["30", "Reject"],
        ]

        clean_marks_table = Table(
            marks_data,
            include_outer_lines=False,
            line_config={"stroke_width": 1.5},
            element_to_mobject=lambda item: Text(item, color=GREEN if item in ["Admit", "Reject"] else BLUE),
        )
        clean_marks_table.scale(0.4)
        clean_marks_table.move_to(marks_decision_group)

        # 6️⃣ Replace rough columns with clean table
        self.play(
            Transform(marks_decision_group, clean_marks_table),
            FadeOut(highlight_rects),
            run_time=2
        )

        self.wait(2)
        self.play(
            table.animate.shift(RIGHT * 2).set_opacity(0),
            run_time=2
        )
        self.wait(0.5)
        # 1️⃣ Write "Parent Entropy" title
        parent_entropy_title = Text("Parent Entropy", font_size=30, color=YELLOW)
        parent_entropy_title.move_to(RIGHT * 3 + UP * 2)  # adjust to top right nicely

        self.play(Write(parent_entropy_title))
        self.wait(0.5)

        # 2️⃣ Write the entropy formula below the title
        entropy_formula = MathTex(
            r"H(D) = -\sum p(x) \log_2 p(x)",
            font_size=25
        )
        entropy_formula.next_to(parent_entropy_title, DOWN, buff=0.5)

        self.play(Write(entropy_formula))
        self.wait(1)
        # Step 1: Show Admit/Reject counts from table (derived from left table visually)
        prob_table = Table(
            [["Decision", "Count", "Probability"],
             ["Admit", "3", "3/5"],
             ["Reject", "2", "2/5"]],
            include_outer_lines=False,
            line_config={"stroke_width": 1.5},
            element_to_mobject=lambda item: Text(item, color=GREEN if item in ["Admit", "Reject"] else BLUE),
        )
        prob_table.scale(0.45)
        prob_table.next_to(entropy_formula, DOWN, buff=0.7)

        self.play(FadeIn(prob_table))
        self.wait(1)
        # Step 2: Substitute values into entropy formula
        entropy_substituted = MathTex(
            r"H(D) = -\left( \frac{3}{5} \log_2 \frac{3}{5} + \frac{2}{5} \log_2 \frac{2}{5} \right)",
            font_size=34
        )
        entropy_substituted.next_to(prob_table, DOWN, buff=0.6)

        self.play(Write(entropy_substituted))
        self.wait(1)
        # Step 3: Compute the result
        entropy_value = MathTex(
            r"H(D) \approx 0.971",
            font_size=34,
            color=YELLOW
        )
        entropy_value.next_to(entropy_substituted, DOWN, buff=0.5)

        self.play(Write(entropy_value))
        self.wait(2)

        # Fade out the top title first
        self.play(FadeOut(title), run_time=1)
        self.wait(0.5)

        # Shrink and move the clean_marks_table to top-left
        self.play(
            clean_marks_table.animate.scale(0.5).to_corner(UL),
            run_time=2
        )
        self.wait(0.5)

        # Fade out the old rough columns (marks_decision_group) properly
        self.play(
            FadeOut(marks_decision_group),
            run_time=0.5
        )
        self.wait(0.5)
        # 1️⃣ Instead of writing "H(D) ≈ 0.971", create the new correct text:
        parent_entropy_value = Text("Parent Entropy ≈ 0.971", font_size=28, color=YELLOW)
        parent_entropy_value.next_to(entropy_value, DOWN, buff=0.5)

        # 2️⃣ Animate replacement
        self.play(
            Transform(entropy_value, parent_entropy_value),  # Transform old entropy_value into new text
            run_time=1
        )
        self.wait(0.5)

        # 3️⃣ Move the new text to top right corner
        self.play(
            entropy_value.animate.scale(0.8).to_corner(UR),
            run_time=2
        )
        self.wait(0.5)

        # 4️⃣ Fade out everything else on the right (formula, table, etc.)
        right_side_group = VGroup(
            parent_entropy_title,
            entropy_formula,
            prob_table,
            entropy_substituted,
        )

        self.play(
            FadeOut(right_side_group),
            run_time=2
        )
        self.wait(0.5)

        # 1️⃣ Get Marks column values (skip header)
        marks_column = clean_marks_table.get_columns()[0][1:]

        # 2️⃣ Create unsorted copies
        marks_copies_unsorted = [mark.copy() for mark in marks_column]

        # 3️⃣ Arrange them horizontally unsorted (just as they appear)
        unsorted_group = VGroup(*marks_copies_unsorted).arrange(RIGHT, buff=0.6, aligned_edge=DOWN).move_to(DOWN * 1)

        # 🛑 Don't arrange or move anything else yet.

        # 4️⃣ Animate copying them from table to unsorted_group
        self.play(*[TransformFromCopy(orig, copy) for orig, copy in zip(marks_column, marks_copies_unsorted)])
        self.wait(0.5)

        # 5️⃣ NOW create completely NEW sorted group (separate objects)

        # Create (text, value) pairs
        marks_with_values = [(m.text, int(m.text)) for m in marks_copies_unsorted]

        # Sort based on integer value
        marks_sorted = sorted(marks_with_values, key=lambda x: x[1])

        # Create NEW Text objects for sorted marks
        marks_copies_sorted = [Text(text, color=BLUE, font_size=marks_copies_unsorted[0].font_size) for text, _ in
                               marks_sorted]

        # Step 0️⃣ : Before anything, capture the original unsorted group
        original_unsorted_group = VGroup(*marks_copies_unsorted).copy()

        # Step 0️⃣ : Create two groups: one for animation, one dummy left behind
        unsorted_group_for_anim = VGroup(*marks_copies_unsorted)
        unsorted_group_static_copy = unsorted_group_for_anim.copy()

        # Now both groups are **visually identical**, but **separate objects**

        # Show both initially
        self.add(unsorted_group_static_copy)
        self.play(FadeIn(unsorted_group_for_anim))
        self.wait(1)

        # Step 1️⃣ : Arrange sorted group nicely
        sorted_group = VGroup(*marks_copies_sorted).arrange(RIGHT, buff=0.6).move_to(DOWN * 1)

        # Step 2️⃣ : Animate transform: move unsorted ➔ sorted
        self.play(Transform(unsorted_group_for_anim, sorted_group), run_time=2)
        self.wait(1)

        # Step 3️⃣ : Move sorted group to top
        self.play(
            unsorted_group_for_anim.animate.to_edge(UP).shift(DOWN * 0.5),
            run_time=2
        )
        self.wait(1)

        # Step 4️⃣ : Now fade out the static leftover copy
        self.play(FadeOut(unsorted_group_static_copy))
        self.wait(1)

        midpoint_calculations = VGroup(
            MathTex(r"\frac{30 + 40}{2} = 35", font_size=28),
            MathTex(r"\frac{40 + 72}{2} = 56", font_size=28),
            MathTex(r"\frac{72 + 85}{2} = 78.5", font_size=28),
            MathTex(r"\frac{85 + 92}{2} = 88.5", font_size=28)
        ).arrange(RIGHT, buff=1.2)  # Arrange horizontally with some space
        split_title = Text("Finding Split Candidates", font_size=28, color=YELLOW)
        split_title.next_to(sorted_group, DOWN, buff=0.7)

        self.play(Write(split_title))
        self.wait(0.5)

        midpoint_calculations.next_to(split_title, DOWN, buff=0.8)

        self.play(LaggedStart(*[Write(m) for m in midpoint_calculations], lag_ratio=0.6))
        self.wait(2)
from manim import *

class MidpointStepByStepFinal(Scene):
    def construct(self):
        # 1️⃣ Midpoints at top
        # 5️⃣ Create the clean Marks-only table
        marks_data = [
            ["Marks", "Decision"],
            ["92", "Admit"],
            ["85", "Admit"],
            ["72", "Admit"],
            ["40", "Reject"],
            ["30", "Reject"],
        ]

        clean_marks_table = Table(
            marks_data,
            include_outer_lines=False,
            line_config={"stroke_width": 1.5},
            element_to_mobject=lambda item: Text(item, color=GREEN if item in ["Admit", "Reject"] else BLUE),
        )

        # 🛠️ Scale and move the table
        clean_marks_table.scale(0.2)  # Scale down to half
        clean_marks_table.to_corner(UL, buff=0.3)  # Move to top-left with a little buffer

        # ✨ Add it directly (no animation)
        self.add(clean_marks_table)

        midpoints = VGroup(
            MathTex(r"35", font_size=36),
            MathTex(r"56", font_size=36),
            MathTex(r"78.5", font_size=36),
            MathTex(r"88.5", font_size=36),
        ).arrange(RIGHT, buff=1.5)
        midpoints.to_edge(UP)

        self.play(FadeIn(midpoints))
        self.wait(1)

        # 2️⃣ Set up to store calculated entropies
        entropy_values = []

        midpoint_data = [
            {
                "split_info": "Split at 35:\nLeft (≤35): 1 Reject\nRight (>35): 1 Reject, 3 Admit",
                "probs": [
                    r"p(\text{Reject left}) = \frac{1}{5}",
                    r"p(\text{Reject right}) = \frac{1}{5}",
                    r"p(\text{Admit right}) = \frac{3}{5}"
                ],
                "formula": r"H(D|35) = -\left( \frac{1}{5}\log_2\frac{1}{5} + \frac{1}{5}\log_2\frac{1}{5} + \frac{3}{5}\log_2\frac{3}{5} \right)",
                "entropy_result": r"0.950"
            },
            {
                "split_info": "Split at 56:\nLeft (≤56): 2 Reject\nRight (>56): 3 Admit",
                "probs": [
                    r"p(\text{Reject left}) = \frac{2}{5}",
                    r"p(\text{Admit right}) = \frac{3}{5}"
                ],
                "formula": r"H(D|56) = -\left( \frac{2}{5}\log_2\frac{2}{5} + \frac{3}{5}\log_2\frac{3}{5} \right)",
                "entropy_result": r"0.0"  # PERFECT SPLIT!
            },
            {
                "split_info": "Split at 78.5:\nLeft (≤78.5): 2 Reject, 1 Admit\nRight (>78.5): 2 Admit",
                "probs": [
                    r"p(\text{Reject left}) = \frac{2}{5}",
                    r"p(\text{Admit left}) = \frac{1}{5}",
                    r"p(\text{Admit right}) = \frac{2}{5}"
                ],
                "formula": r"H(D|78.5) = -\left( \frac{2}{5}\log_2\frac{2}{5} + \frac{1}{5}\log_2\frac{1}{5} + \frac{2}{5}\log_2\frac{2}{5} \right)",
                "entropy_result": r"1.522"
            },
            {
                "split_info": "Split at 88.5:\nLeft (≤88.5): 2 Reject, 2 Admit\nRight (>88.5): 1 Admit",
                "probs": [
                    r"p(\text{Reject left}) = \frac{2}{5}",
                    r"p(\text{Admit left}) = \frac{2}{5}",
                    r"p(\text{Admit right}) = \frac{1}{5}"
                ],
                "formula": r"H(D|88.5) = -\left( \frac{2}{5}\log_2\frac{2}{5} + \frac{2}{5}\log_2\frac{2}{5} + \frac{1}{5}\log_2\frac{1}{5} \right)",
                "entropy_result": r"1.522"
            },
        ]

        # 4️⃣ Process each midpoint
        for idx, data in enumerate(midpoint_data):
            # Highlight the midpoint
            self.play(midpoints[idx].animate.set_color(YELLOW))
            self.wait(0.5)

            # Split Info
            split_info = Text(data["split_info"], font_size=22)
            split_info.next_to(midpoints[idx], DOWN, buff=1.2)
            self.play(Write(split_info))
            self.wait(1)

            # Probabilities
            prob_texts = VGroup(
                *[MathTex(p, font_size=24).set_color(BLUE) for p in data["probs"]]
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            prob_texts.next_to(split_info, DOWN, buff=0.6)
            self.play(LaggedStart(*[Write(p) for p in prob_texts], lag_ratio=0.3))
            self.wait(1.5)

            # Formula
            formula = MathTex(data["formula"], font_size=22)
            formula.next_to(prob_texts, DOWN, buff=0.6)
            self.play(Write(formula))
            self.wait(2)

            # Entropy Result
            entropy = MathTex(
                rf"H(D|{midpoints[idx].get_tex_string()}) \approx {data['entropy_result']}",
                font_size=30,
                color=RED
            )
            entropy.next_to(formula, DOWN, buff=0.8)

            self.play(Write(entropy))
            self.wait(2)

            # 5️⃣ Store entropy result to show below top midpoint later
            entropy_values.append(
                MathTex(
                    rf"{data['entropy_result']}",
                    font_size=24,
                    color=RED
                ).next_to(midpoints[idx], DOWN, buff=0.3)
            )

            # Fade out all except midpoints
            self.play(
                FadeOut(split_info),
                FadeOut(prob_texts),
                FadeOut(formula),
                FadeOut(entropy),
                midpoints[idx].animate.set_color(WHITE)
            )
            self.wait(0.5)

        # 6️⃣ Finally show entropy results below each midpoint
        self.play(LaggedStart(*[FadeIn(e) for e in entropy_values], lag_ratio=0.3))
        self.wait(3)

from manim import *

class ShowInformationGain(Scene):
    def construct(self):
        # 1️⃣ Title
        title = Text("Choosing Best Split by Information Gain", font_size=36, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2️⃣ Parent Entropy
        parent_entropy = MathTex(r"H(D) \approx 0.971", font_size=30)
        parent_entropy.next_to(title, DOWN, buff=0.8)
        self.play(Write(parent_entropy))
        self.wait(1)

        # 3️⃣ Show Feature Names (like Marks, Rank, Experience etc.)
        features = VGroup(
            Text("Marks", font_size=28, color=BLUE),
            Text("Rank", font_size=28, color=BLUE),
            Text("Experience", font_size=28, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        features.next_to(parent_entropy, DOWN, buff=1.5, aligned_edge=LEFT)

        self.play(LaggedStart(*[FadeIn(f) for f in features], lag_ratio=0.5))
        self.wait(1)

        # 4️⃣ Show Entropies After Splits
        feature_entropies = VGroup(
            MathTex(r"H(D|\text{Marks}) \approx 0.0", font_size=26, color=WHITE),
            MathTex(r"H(D|\text{Rank}) \approx 0.6", font_size=26, color=WHITE),
            MathTex(r"H(D|\text{Experience}) \approx 0.8", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        feature_entropies.next_to(features, RIGHT, buff=1.5)

        self.play(LaggedStart(*[FadeIn(ent) for ent in feature_entropies], lag_ratio=0.5))
        self.wait(1)

        # 5️⃣ Now show that Lower Entropy ➔ Higher Information Gain
        idea = Text("Lower Entropy ➔ Higher Information Gain", font_size=28, color=GREEN)
        idea.next_to(feature_entropies, DOWN, buff=1.2)
        self.play(Write(idea))
        self.wait(2)

        # 6️⃣ Now actually calculate IG for each feature
        ig_marks = MathTex(
            r"IG(\text{Marks}) = 0.971 - 0 = 0.971",
            font_size=28,
            color=YELLOW
        )
        ig_rank = MathTex(
            r"IG(\text{Rank}) = 0.971 - 0.6 = 0.371",
            font_size=28,
            color=YELLOW
        )
        ig_exp = MathTex(
            r"IG(\text{Experience}) = 0.971 - 0.8 = 0.171",
            font_size=28,
            color=YELLOW
        )

        igs = VGroup(ig_marks, ig_rank, ig_exp).arrange(DOWN, buff=0.7)
        igs.next_to(idea, DOWN, buff=1.5)

        self.play(LaggedStart(*[Write(ig) for ig in igs], lag_ratio=0.6))
        self.wait(2)

        # 7️⃣ Highlight the best split
        best_split = SurroundingRectangle(ig_marks, color=GREEN, buff=0.2)
        self.play(Create(best_split))
        self.wait(2)

        # 8️⃣ Announce
        conclusion = Text("Best Split: Marks", font_size=32, color=RED)
        conclusion.next_to(igs, DOWN, buff=1.2)
        self.play(Write(conclusion))
        self.wait(3)
from manim import *

from manim import *

class InformationGainMarksOnly(Scene):
    def construct(self):
        # 1️⃣ Title
        title = Text("Choosing Best Split (Marks Feature)", font_size=36, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2️⃣ Parent Entropy
        parent_entropy = MathTex(r"H(D) \approx 0.971", font_size=30,color=PINK)
        parent_entropy.next_to(title, DOWN, buff=0.3)
        self.play(Write(parent_entropy))
        self.wait(1)

        # 3️⃣ Midpoints list (moved to left edge)
        midpoints = VGroup(
            Text("35", font_size=28, color=BLUE),
            Text("56", font_size=28, color=BLUE),
            Text("78.5", font_size=28, color=BLUE),
            Text("88.5", font_size=28, color=BLUE),
        ).arrange(DOWN, buff=0.8)
        midpoints.to_edge(LEFT, buff=1).shift(UP * 0.1)  # slightly down from top edge

        self.play(LaggedStart(*[FadeIn(mp) for mp in midpoints], lag_ratio=0.3))
        self.wait(1)

        # 4️⃣ Entropy after each split (to the right of midpoints)
        midpoints_entropy = VGroup(
            MathTex(r"H(D|35) \approx 0.971", font_size=26),
            MathTex(r"H(D|56) \approx 0.0", font_size=26),
            MathTex(r"H(D|78.5) \approx 0.650", font_size=26),
            MathTex(r"H(D|88.5) \approx 0.918", font_size=26),
        ).arrange(DOWN, buff=0.8)
        midpoints_entropy.next_to(midpoints, RIGHT, buff=1)

        self.play(LaggedStart(*[FadeIn(e) for e in midpoints_entropy], lag_ratio=0.3))
        self.wait(1)

        # 5️⃣ Arrows from midpoint ➔ entropy
        arrows = VGroup(*[
            Arrow(
                midpoints[i].get_right(),
                midpoints_entropy[i].get_left(),
                buff=0.1
            ) for i in range(4)
        ])
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.2))
        self.wait(1)

        # 6️⃣ Info Gain Calculation (further right, but we'll clamp it)
        igs = VGroup(
            MathTex(r"IG(35) = 0.971 - 0.971 = 0.0", font_size=25),
            MathTex(r"IG(56) = 0.971 - 0.0 = 0.971", font_size=25),
            MathTex(r"IG(78.5) = 0.971 - 0.650 = 0.321", font_size=25),
            MathTex(r"IG(88.5) = 0.971 - 0.918 = 0.053", font_size=25),
        ).arrange(DOWN, buff=0.8)
        igs.next_to(midpoints_entropy, RIGHT, buff=1)

        # If it still goes off-screen, scale down slightly:
        igs.scale(0.9)

        self.play(LaggedStart(*[Write(ig) for ig in igs], lag_ratio=0.4))
        self.wait(2)

        # 7️⃣ Highlight best split at 56
        best_box = SurroundingRectangle(igs[1], color=GREEN, buff=0.2)
        self.play(Create(best_box))
        self.wait(1.5)

        # 8️⃣ Final conclusion
        conclusion = Text("Best Split at 56 (Perfect Split!)", font_size=30, color=RED)
        conclusion.next_to(igs, DOWN, buff=1.5)
        self.play(Write(conclusion))
        self.wait(3)
from manim import *

class BestFeatureSelection(Scene):
    def construct(self):
        # 1️⃣ Title
        title = Text("Choosing Best Feature", font_size=36, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2️⃣ Parent Entropy
        parent_entropy = MathTex(r"H(D) \approx 0.971", font_size=30)
        parent_entropy.next_to(title, DOWN, buff=0.8)
        self.play(Write(parent_entropy))
        self.wait(1)

        # 3️⃣ Features list
        features = VGroup(
            Text("Marks", font_size=28, color=BLUE),
            Text("Attendance", font_size=28, color=BLUE),
            Text("Assignments", font_size=28, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)
        features.next_to(parent_entropy, DOWN, buff=1)

        self.play(LaggedStart(*[FadeIn(f) for f in features], lag_ratio=0.3))
        self.wait(1)

        # 4️⃣ Best IG for each feature
        best_igs = VGroup(
            MathTex(r"IG_{\text{Marks}} = 0.971", font_size=26, color=GREEN),
            MathTex(r"IG_{\text{Attendance}} = 0.650", font_size=26, color=GREEN),
            MathTex(r"IG_{\text{Assignments}} = 0.820", font_size=26, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)
        best_igs.next_to(features, RIGHT, buff=2)

        arrows = VGroup(
            Arrow(features[0].get_right(), best_igs[0].get_left(), buff=0.1),
            Arrow(features[1].get_right(), best_igs[1].get_left(), buff=0.1),
            Arrow(features[2].get_right(), best_igs[2].get_left(), buff=0.1),
        )

        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.2))
        self.play(LaggedStart(*[Write(ig) for ig in best_igs], lag_ratio=0.3))
        self.wait(2)

        # 5️⃣ Highlight the best feature
        best_feature_box = SurroundingRectangle(features[0], color=RED, buff=0.2)
        best_ig_box = SurroundingRectangle(best_igs[0], color=RED, buff=0.2)

        self.play(Create(best_feature_box), Create(best_ig_box))
        self.wait(1.5)

        # 6️⃣ Final Conclusion
        conclusion = Text("Select 'Marks' Feature for Split!", font_size=32, color=RED)
        conclusion.next_to(best_igs, DOWN+LEFT, buff=1.5)
        self.play(Write(conclusion))
        self.wait(3)

        # 7️⃣ Fade out
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
