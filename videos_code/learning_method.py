from manim import *

class LearningMethodsScene(Scene):
    def construct(self):
        # Step 1: Main "Learning Methods" box
        main_box = Rectangle(width=6, height=1.5, color=BLUE, fill_opacity=0.1)
        main_text = Text("Learning Methods", font="Arial", font_size=36)
        main_group = VGroup(main_box, main_text)
        main_group.move_to(ORIGIN)

        # Animate main box in, then slide it up
        self.play(Create(main_box), Write(main_text))
        self.wait(0.5)
        self.play(main_group.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)

        # Step 2: Three type boxes appear in a row beneath
        sup_box = Rectangle(width=3, height=1, color=GREEN, fill_opacity=0.1)
        sup_text = Text("Supervised", font="Arial", font_size=24).move_to(sup_box.get_center())
        unsup_box = Rectangle(width=3, height=1, color=YELLOW, fill_opacity=0.1)
        unsup_text = Text("Unsupervised", font="Arial", font_size=24).move_to(unsup_box.get_center())
        rl_box = Rectangle(width=3, height=1, color=RED, fill_opacity=0.1)
        rl_text = Text("Reinforcement", font="Arial", font_size=24).move_to(rl_box.get_center())

        type_group = VGroup(
            VGroup(sup_box, sup_text),
            VGroup(unsup_box, unsup_text),
            VGroup(rl_box, rl_text)
        ).arrange(RIGHT, buff=1).next_to(main_group, DOWN, buff=0.8)

        self.play(LaggedStartMap(FadeIn, type_group, shift=DOWN), run_time=1)
        self.wait(0.5)

        # Step 3: Model box appears below the types
        model_box = Rectangle(width=2.5, height=1, color=BLUE, fill_opacity=0.1)
        model_text = Text("Model", font="Arial", font_size=24).move_to(model_box.get_center())
        model_group = VGroup(model_box, model_text).move_to(DOWN * 2)

        self.play(FadeIn(model_box), Write(model_text))
        self.wait(0.5)

        # Step 4: Arrows from each learning type to the model
        arrows = VGroup(
            Arrow(sup_box.get_bottom(), model_box.get_top(), buff=0.1),
            Arrow(unsup_box.get_bottom(), model_box.get_top(), buff=0.1),
            Arrow(rl_box.get_bottom(), model_box.get_top(), buff=0.1),
        )
        arrows.set_stroke(width=1.5)  # make all arrows thinner
        self.play(LaggedStartMap(GrowArrow, arrows, lag_ratio=0.3), run_time=1)
        self.wait(0.5)

        # Step 5: Label arrows with brief descriptions
        label1 = Text("Labeled data", font="Arial", font_size=18).next_to(arrows[0].get_center(), RIGHT, buff=0.3)
        label2 = Text("Find patterns", font="Arial", font_size=18).next_to(arrows[1].get_center(), RIGHT, buff=0.3)
        label3 = Text("Trial & reward", font="Arial", font_size=18).next_to(arrows[2].get_center(), RIGHT, buff=0.3)

        self.play(Write(label1), Write(label2), Write(label3))
        self.wait(2)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in [
                main_group, type_group, model_group, arrows, label1, label2, label3
            ]]
        )
