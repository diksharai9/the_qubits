# Manim code for the "Supervised vs Unsupervised Learning" script
# Each scene corresponds to a part of the voiceover script

from manim import *

class IntroScene(Scene):
    def construct(self):
        # Step 1: Heading
        heading = Text("How does ChatGPT answer your questions?", font="DejaVu Sans",font_size=36, color=RED)
        self.play(Write(heading))
        self.wait(1)

        # Step 2: Slide heading up
        self.play(heading.animate.to_edge(UP))

        # Step 3: Explanation text
        explanation = Text(
            "It's similar to how humans learn.\n"
            "Models are trained over the data available on the internet.",font="DejaVu Sans",
            font_size=28,
            color=WHITE
        )
        self.play(Write(explanation))
        self.wait(1)

        # Step 4: Surround with yellow box
        box = SurroundingRectangle(explanation, color=YELLOW)
        self.play(Create(box))
        self.wait(2)

        # Step 5: Clear scene
        self.play(FadeOut(heading, explanation, box))

        # Step 6: Data training animation
        # Prepare colored data points
        colors = [RED, BLUE, YELLOW, WHITE, GREEN] * 2 + [RED, BLUE]
        data_points = VGroup(*[
            Dot(color=color).move_to([i * 0.5 - 3, -2.5, 0])
            for i, color in enumerate(colors)
        ])
        # Big circle at center
        big_circle = Circle(radius=1.5, color=BLUE).set_fill(BLUE, opacity=0.5)
        # Small circle below big circle
        # small_circle = Circle(radius=0.5, color=BLUE).set_fill(BLUE, opacity=0.5)
        # small_circle.next_to(big_circle, DOWN, buff=1)

        # Show circles and data points
        self.play(FadeIn(big_circle),FadeIn(data_points))

        # Animate data into big circle center
        for dot in data_points:
            self.play(dot.animate.move_to(big_circle.get_center()), run_time=0.4)

        self.wait(1)
        # Label trained model below small circle
        trained_text = Text("Trained Model", font="DejaVu Sans",font_size=24, color=GREEN)
        trained_text.next_to(big_circle, DOWN)
        self.play(Write(trained_text))
        self.wait(2)

        # Clear training scene
        self.play(FadeOut(data_points, big_circle,trained_text))

from manim import *

class SupervisedLearningScene(Scene):
    def construct(self):
        # Title
        title = Text("Supervised Learning", font="DejaVu Sans",font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 1) Draw the sentence, split into two parts
        labeled_data = Text("Labeled Data", font="DejaVu Sans",font_size=34)
        learn_predict = Text("→ Learn Pattern → Predict",font="DejaVu Sans", font_size=30)
        learn_predict.next_to(labeled_data, RIGHT, buff=0.4)
        sentence = VGroup(labeled_data, learn_predict).move_to(UP * 1)
        self.play(Write(sentence))
        self.wait(1)

        # 2) Prepare flashcards off-screen above the "Labeled Data" text
        specs = [("Cat", BLUE), ("Dog", GREEN), ("Rabbit", RED)]
        flashcards = VGroup()
        for txt, color in specs:
            box = Rectangle(width=1, height=1).set_color(color).set_fill(color, opacity=0.1)
            lab = Text(txt, font="DejaVu Sans",font_size=20).move_to(box.get_center())
            flashcards.add(VGroup(box, lab))
        flashcards.arrange(RIGHT, buff=0.4)
        # position flashcards above the labeled_data position
        flashcards.move_to(labeled_data.get_center() + UP * 2)

        # 3) Animate: flashcards drop into place of "Labeled Data" while that text fades
        drop_target = labeled_data.get_center()
        self.play(
            # flashcards move down to the exact spot where "Labeled Data" was
            flashcards.animate.move_to(drop_target),
            # labeled_data fades out
            FadeOut(labeled_data),
            run_time=1
        )
        self.wait(5)

        # 4) Clean up everything
        self.play(
            FadeOut(flashcards),
            FadeOut(learn_predict)
        )
        self.wait(0.5)


class SupervisedHierarchyScene(Scene):
    def construct(self):
        # Step 1: Top-level box
        top_box = Rectangle(width=6, height=1.5, color=BLUE, fill_opacity=0.1)
        top_text = Text("Supervised Learning", font="DejaVu Sans",font_size=30)
        top_group = VGroup(top_box, top_text).move_to(UP * 2)
        self.play(Create(top_box), Write(top_text))
        self.wait(0.5)

        # Step 2: Child boxes
        class_box = Rectangle(width=3, height=1, color=GREEN, fill_opacity=0.1)
        class_text = Text("Classification",font="DejaVu Sans", font_size=24)
        class_group = VGroup(class_box, class_text).move_to(LEFT * 2 + DOWN * 0.5)

        reg_box = Rectangle(width=3, height=1, color=RED, fill_opacity=0.1)
        reg_text = Text("Regression", font="DejaVu Sans",font_size=24)
        reg_group = VGroup(reg_box, reg_text).move_to(RIGHT * 2 + DOWN * 0.5)

        # Step 3: Arrows from top box to children
        arrow1 = Arrow(
            start=top_box.get_bottom(),
            end=class_box.get_top(),
            buff=0.2
        )
        arrow2 = Arrow(
            start=top_box.get_bottom(),
            end=reg_box.get_top(),
            buff=0.2
        )

        # Animate arrows and boxes
        self.play(GrowArrow(arrow1), Create(class_box), Write(class_text))
        self.wait(0.3)
        self.play(GrowArrow(arrow2), Create(reg_box), Write(reg_text))
        self.wait(0.5)

        # Step 4: Descriptions under each child
        cat_pred = Text("Predict Categories",font="DejaVu Sans", font_size=20).next_to(class_box, DOWN, buff=0.2)
        num_pred = Text("Predict Numbers", font="DejaVu Sans",font_size=20).next_to(reg_box, DOWN, buff=0.2)
        self.play(Write(cat_pred), Write(num_pred))
        self.wait(1)

        # Optional: fade out
        self.play(
            FadeOut(top_group),
            FadeOut(arrow1), FadeOut(arrow2),
            FadeOut(class_box), FadeOut(class_text), FadeOut(cat_pred),
            FadeOut(reg_box), FadeOut(reg_text), FadeOut(num_pred),
        )

from manim import *
import random

class UnsupervisedLearningScene(Scene):
    def construct(self):
        # Step 1: Title
        title = Text("Unsupervised Learning", font="DejaVu Sans",font_size=36)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Step 2: Label describing the process
        label = Text("Unlabeled Data → Find Patterns/Groups", font="DejaVu Sans",font_size=30)
        label.to_edge(UP, buff=0.5)
        self.play(Write(label))
        self.wait(1)

        # Step 3: Draw the processing box at center
        model_box = Rectangle(width=5, height=2, color=YELLOW, fill_opacity=0.1)
        box_text = Text("Unsupervised Learning",font="DejaVu Sans", font_size=24)
        box_group = VGroup(model_box, box_text).move_to(ORIGIN)
        self.play(Create(model_box), Write(box_text))
        self.wait(0.5)
        # Create mixed input shapes
        input_shapes = []
        for _ in range(3):
            input_shapes.append(Circle(radius=0.25).set_color(RED))
            input_shapes.append(Square(side_length=0.4).set_color(GREEN))
            input_shapes.append(Triangle().scale(0.3).set_color(BLUE))
        random.shuffle(input_shapes)
        input_group = VGroup(*input_shapes).arrange(DOWN, buff=0.3).to_edge(LEFT)

        # Input arrow
        input_arrow = Arrow(start=input_group.get_right(), end=model_box.get_left(), buff=0.2)
        self.play(FadeIn(input_group), GrowArrow(input_arrow))
        self.wait(0.5)

        # Move shapes into model
        self.play(
            LaggedStart(*[
                shape.animate.move_to(model_box.get_center() + RIGHT * 0.2 * (i % 3) + DOWN * 0.2 * (i // 3))
                for i, shape in enumerate(input_group)
            ], lag_ratio=0.1),
            run_time=2
        )
        self.wait(0.5)
        self.play(FadeOut(input_arrow))

        # Prepare outputs: 3 groups
        group1 = VGroup(*[Circle(radius=0.25).set_color(RED) for _ in range(3)]).arrange(DOWN, buff=0.3)
        group2 = VGroup(*[Square(side_length=0.4).set_color(GREEN) for _ in range(3)]).arrange(DOWN, buff=0.3)
        group3 = VGroup(*[Triangle().scale(0.3).set_color(BLUE) for _ in range(3)]).arrange(DOWN, buff=0.3)

        all_groups = VGroup(group1, group2, group3).arrange(RIGHT, buff=1.0).to_edge(RIGHT)
        output_arrow = Arrow(start=model_box.get_right(), end=all_groups.get_left(), buff=0.2)

        # Show arrow to output side
        self.play(GrowArrow(output_arrow))

        # Animate grouped output one by one
        self.play(FadeIn(group1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(group2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(group3), run_time=0.5)
        self.wait(1)

        # Enclose outputs in a box
        output_box1 = SurroundingRectangle(group1, color=WHITE)
        self.play(Create(output_box1))
        self.wait(2)
        output_box2 = SurroundingRectangle(group2, color=YELLOW)
        self.play(Create(output_box2))
        self.wait(2)
        output_box3 = SurroundingRectangle(group3, color=PINK)
        self.play(Create(output_box3))
        self.wait(2)
        input_shapes=VGroup(*input_shapes)

        # Fade out
        self.play(
            FadeOut(box_group),
            FadeOut(group1), FadeOut(group2), FadeOut(group3),
            FadeOut(output_arrow), FadeOut(output_box1), FadeOut(output_box2), FadeOut(output_box3), FadeOut(label),FadeOut(input_shapes)
        )

class SummaryScene(Scene):
    def construct(self):
        title = Text("Supervised vs Unsupervised Summary",font="DejaVu Sans", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        table = Table([
            ["Supervised Learning", "Unsupervised Learning"],
            ["Labeled Data", "Unlabeled Data"],
            ["Predict outcomes", "Discover patterns"],
            ["Classification, Regression", "Clustering, Reduction"]
        ],
            col_labels=[Text("Type"), Text("Description")],
            include_outer_lines=True
        )

        self.play(Create(table))
        self.wait(3)
        self.play(FadeOut(table))

from manim import *

class OutroScene(Scene):
    def construct(self):
        # Neon colors to cycle through
        neon_colors = [RED, YELLOW, GREEN, BLUE, PURPLE]

        # Create text
        subscribe = Text("Like, Share & Subscribe for more visual ML!", font="DejaVu Sans",font_size=28)
        subscribe.set_color(neon_colors[0])
        subscribe.move_to(ORIGIN)

        # Fade in with slight scale bounce
        self.play(GrowFromCenter(subscribe), run_time=1)

        # Blinking neon animation
        for i in range(10):
            subscribe.set_color(neon_colors[i % len(neon_colors)])
            self.wait(0.5)

        # Fade out
        self.play(FadeOut(subscribe), run_time=1)
