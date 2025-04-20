from manim import *
from manim import config


class AdvancedIntro(Scene):
    def construct(self):
        # Background
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            color=BLACK,
            fill_opacity=1
        )

        # Channel logo
        logo = ImageMobject("/home/diksha/Downloads/logo.png")


        # Channel name
        channel_name = Text("Qubits", font="Montserrat").scale(1.5)

        # Positioning
        logo.move_to(UP * 1.5)
        channel_name.move_to(DOWN * 1.5)

        # Animation
        self.play(FadeIn(logo))
        self.wait(0.5)
        self.play(Write(channel_name))
        self.wait(1)
        self.play(FadeOut(logo), FadeOut(channel_name))


# Render the advanced intro scene
intro_scene = AdvancedIntro()
intro_scene.render()


