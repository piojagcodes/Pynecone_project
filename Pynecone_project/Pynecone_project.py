import pynecone as pc


class State(pc.State):
    count = 0

    color = "red"

    color_list = ["red", "green", "blue", "orange", "purple"]

    color_index = 0

    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1

    def backwards(self):
        self.color_index -= 1
        self.color_index %= 5
        self.color = self.color_list[self.color_index]

    def forward(self):
        self.color_index += 1
        self.color_index %= 5
        self.color = self.color_list[self.color_index]

def index():
    return pc.hstack(
        pc.button("-", color_scheme="red", border_radius="1em",
                on_click=State.decrement),
        pc.heading(State.count, font_size="2em"),
        pc.button("+", color_scheme="green", border_radius="1em",
                on_click=State.increment),
        

        )

def other():
    return pc.vstack(
            pc.button("<", color_scheme="gray", border_radius="1em",
                on_click=State.backwards),
            pc.heading("Hello World", color=State.color, font_size="2em"),

            pc.button(">", color_scheme="gray", border_radius="1em",
                on_click=State.forward)
            )

app = pc.App(state=State)
app.add_page(index, path="/")
app.add_page(other, path="/other")
app.compile()
