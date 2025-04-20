# Manim code for the "Imagine Teaching a Bike Price Predictor" animation
from manim import *

class BikePricePredictorScene(Scene):
    def construct(self):
        # # Step 1: Title at top center
        # title = Text("Imagine Teaching a Bike Price Predictor", font_size=36)
        # title.to_edge(UP, buff=0.5)
        # self.play(Write(title))
        # self.wait(0.5)
        #
        # # Step 2: Show bike at left-middle (positioned manually)
        # bike = SVGMobject("./bike.svg").scale(0.6).move_to(LEFT * 4 + UP * 0.3)
        # bike_label = Text("Bike", font_size=24).next_to(bike, DOWN, buff=0.2)
        # self.play(FadeIn(bike), Write(bike_label))
        # self.wait(0.5)
        #
        # # Step 3: Features to the right of bike
        # features = VGroup(
        #     Text("Brand: Hero", font_size=20),
        #     Text("Gears: 6", font_size=20),
        #     Text("Weight: 15kg", font_size=20),
        # ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(bike, RIGHT, buff=0.8)
        # self.play(LaggedStart(*[Write(f) for f in features], lag_ratio=0.2))
        # self.wait(0.5)
        #
        # # Step 4: Arrow from bike to model at right-middle
        model = Circle(radius=0.6, color=YELLOW).to_edge(RIGHT).shift(UP * 0.3)
        model_label = Text("Model", font_size=24).next_to(model, DOWN, buff=0.2)
        # arrow = Arrow(start=bike.get_right() + RIGHT * 0.1,
        #               end=model.get_left() + LEFT * 0.1,
        #               buff=0)
        # self.play(GrowArrow(arrow), FadeIn(model), Write(model_label))
        self.wait(0.5)
        #
        # # Step 5: Prediction arrow and price text below arrow tip
        # price_text = Text("₹5000", font_size=24, color=GREEN)
        # pred_arrow = Arrow(start=model.get_right() + RIGHT * 0.1,
        #                    end=model.get_right() + RIGHT * 1.5,
        #                    buff=0)
        # price_text.next_to(pred_arrow.get_end(), DOWN, buff=0.2)
        # self.play(GrowArrow(pred_arrow), Write(price_text))
        # self.wait(1)
        #
        # # Fade out all first scene elements using improved fade animation
        # animations = [
        #     FadeOut(title, shift=UP),
        #     FadeOut(bike, shift=LEFT),
        #     FadeOut(bike_label, shift=DOWN),
        #     FadeOut(features, shift=LEFT),
        #     FadeOut(model, shift=RIGHT),
        #     FadeOut(model_label, shift=DOWN),
        #     FadeOut(arrow, shift=RIGHT),
        #     FadeOut(pred_arrow, shift=RIGHT),
        #     FadeOut(price_text, shift=DOWN)
        # ]
        # self.play(AnimationGroup(*animations, lag_ratio=0.1))
        # self.wait(0.3)

        # Step 6: Training phase heading under title
        training_text = Text("Training Phase: Feeding many bikes & prices", font_size=26, color=BLUE)
        training_text.to_edge(UP, buff=0.5)
        self.play(Write(training_text))
        self.wait(0.5)

        # Step 7: Show multiple training examples on left
        example_bikes = VGroup(*[
            SVGMobject("bike.svg").scale(0.3).shift(LEFT * 3 + UP * (0.9 - i * 0.6))
            for i in range(4)
        ])
        example_prices = VGroup(*[
            Text(f"₹{3000 + i*500}", font_size=20)
            .next_to(example_bikes[i], RIGHT, buff=0.2)
            for i in range(4)
        ])
        input_arrows = VGroup(*[
            Arrow(start=example_bikes[i].get_right(),
                  end=RIGHT * 2.5 + UP * 0.3,
                  buff=0).set_color(GREY)
            for i in range(4)
        ])
        # Bring back central model for training
        model.move_to(RIGHT * 3 + UP * 0.3)
        model_label.next_to(model, DOWN, buff=0.2)
        self.play(FadeIn(model), Write(model_label))
        self.play(LaggedStart(*[FadeIn(b) for b in example_bikes], lag_ratio=0.2),
                  LaggedStart(*[Write(p) for p in example_prices], lag_ratio=0.2))
        self.play(LaggedStart(*[GrowArrow(a) for a in input_arrows], lag_ratio=0.2))
        self.wait(0.5)

        # Step 8: Show error feedback next to model
        error_arrow = Arrow(start=model.get_center() + RIGHT * 0.8,
                            end=model.get_center() + RIGHT * 1.8,
                            buff=0).set_color(RED)
        error_label = Text("Error", font_size=20, color=RED).next_to(error_arrow.get_end(), UP, buff=0.2)
        self.play(GrowArrow(error_arrow), Write(error_label))
        self.wait(0.5)

        # Step 9: Adjustment explanation at bottom
        adjust_text = Text("Model adjusts weights to reduce error", font_size=24, color=YELLOW)
        adjust_text.to_edge(DOWN, buff=0.5)
        self.play(Write(adjust_text))
        self.wait(0.5)

        # Step 10: Zoom into model parameters centered
        self.play(FadeOut(*example_bikes, *example_prices, *input_arrows, training_text, error_arrow, error_label, adjust_text, model, model_label))
        zoom_model = Circle(radius=1.2, color=YELLOW).move_to(ORIGIN).set_fill(YELLOW, opacity=0.5)
        params_text = Text("Weights (Parameters)", font_size=24).next_to(zoom_model, DOWN, buff=0.2)
        self.play(FadeIn(zoom_model), Write(params_text))
        self.wait(1)

        # End scene
        self.play(FadeOut(zoom_model, params_text))
