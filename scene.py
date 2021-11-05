from manim import *
"""
generer la video : manim scene.py SquareToCircle -pql
-> "One can also specify the render quality by using the flags -ql, -qm, -qh, or -qk, for low, medium, high, and 4k quality, respectively."
"""


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 2)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation