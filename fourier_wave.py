from manim import *
import numpy as np

class FourierSeriesSquareWave(Scene):
    def construct(self):
        N = 30  # Number of Fourier terms (increase for better shape)
        time_tracker = ValueTracker(0)

        # Origin for circles
        origin = LEFT * 4
        wave_origin = RIGHT * 2

        wave_path = VMobject(color=YELLOW)
        wave_path.set_points_as_corners([wave_origin])

        self.add(wave_path)

        # Function to compute the rotating circles and tip
        def get_fourier_group():
            group = VGroup()
            point = origin
            t = time_tracker.get_value()

            for k in range(1, 2*N, 2):  # odd harmonics
                radius = 4 / (k * PI)
                angle = k * t
                circle = Circle(radius=radius, color=BLUE, stroke_opacity=0.5)
                circle.move_to(point)
                group.add(circle)

                vector = radius * np.array([np.cos(angle), np.sin(angle), 0])
                new_point = point + vector
                line = Line(point, new_point, color=WHITE)
                group.add(line)

                point = new_point

            dot = Dot(point, color=RED)
            group.add(dot)

            return group, point

        # Update circle drawing
        def get_drawing_group():
            group, _ = get_fourier_group()
            return group

        drawing_group = always_redraw(get_drawing_group)
        self.add(drawing_group)

        # Update the wave path
        def update_wave(mob):
            _, tip = get_fourier_group()
            new_point = np.array([wave_origin[0], tip[1], 0])
            old_points = mob.get_points()
            if len(old_points) > 500:
                old_points = old_points[1:]
            mob.set_points_as_corners(np.vstack([old_points, new_point]))

        wave_path.add_updater(update_wave)

        self.add(wave_path)

        # Animate time
        self.play(time_tracker.animate.increment_value(2 * PI), run_time=15, rate_func=linear)

        wave_path.remove_updater(update_wave)
        self.wait(2)
