class Text():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.appearence = True
    
    def print_info(self):
        print(self.text, self.x, self.y)

    def hide(self):
        self.appearence = False

    def show(self):
        self.appearence = True

text = Text("Press me", 20, 20)

text.print_info()