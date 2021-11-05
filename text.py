from manim import *

class HelloWorld(Scene):
    def construct(self):
        #text = Text("Happiness is a lie", font_size=144)
        #self.add(text)
        
        title = Tex(r"Reality is often disappointing")
        self.play(
            Write(title),
        )

        self.wait()

        self.play(
            FadeOut(title)
        )        

References: Tex

