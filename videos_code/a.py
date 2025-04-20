from manim import *

class LogoIntro(Scene):
    def construct(self):
        # Background
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            color=BLACK,
            fill_opacity=1
        )
        self.add(background)

        # Channel logo
        logo = SVGMobject("logo2.svg")

        # Channel name
        channel_name = Text("The Qubits", font="Futura").scale(1.3)

        # Positioning
        logo.move_to(UP * 1.4)
        channel_name.move_to(DOWN * 1.5)

        # Animation
        self.play(DrawBorderThenFill(logo), run_time=2)
        self.wait(0.5)
        self.play(Write(channel_name))
        self.wait(1)

        # Neon blink animation
        neon_colors = [RED, YELLOW, GREEN, BLUE, PURPLE]
        for color in neon_colors:
            self.play(channel_name.animate.set_color(color), run_time=0.2)
            self.wait(0.5)
        # Settle back to white
        self.play(channel_name.animate.set_color(WHITE), run_time=0.5)
        self.wait(1)

        self.play(FadeOut(logo), FadeOut(channel_name))


# Render the advanced intro scene
intro_scene = LogoIntro()
intro_scene.render()
