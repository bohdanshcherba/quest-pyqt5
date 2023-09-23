class Button():
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y
        self.appearence = True
    
    def hide(self):
        self.appearence = False

    def show(self):
        self.appearence = True

btn1 = Button("Press me", 20, 20)

print(btn1.appearence)
btn1.hide()
print(btn1.appearence)