#
from manim import *


class Log(Scene):
    def construct(self):
        morning = Text("Logarithms", font_size=100)
        self.play(Write(morning), run_time=3)
        self.wait()
        morning.font_size=50
        self.play(morning.animate.to_edge(UP),run_time=1)
        ul = Underline(morning)  # Underlining the word
        self.add(morning, ul)
        self.wait()
        quote = Text(
            "The logarithm is the inverse function to exponentiation."
            "That\n means the logarithm of a given number x is the exponent to \nwhich another fixed number,"
            " the base b, must be raised,\nto produce that number x.",
            color=BLUE,
        ).scale(0.60)
        self.play(Create(SurroundingRectangle(quote, color=WHITE, buff=MED_LARGE_BUFF)))
        self.add(quote)
        self.wait()


class LogScal(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
            axis_config={"include_numbers": False},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        self.play(Write(ax),Write(graph))
        self.wait(3)
        self.add(ax, graph)


class Formula(Scene):
    def construct(self):
        t = MathTex(r"\log_{b}(y)=x")
        self.play(Write(t))
        self.wait(3)
#
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
#
# class MyAwesomeScene(VoiceoverScene):
#     def construct(self):
#         self.set_speech_service(GTTSService())
#
#         with self.voiceover(text="This circle is drawn as I speak.") as tracker:
#             self.play(Create(circle))