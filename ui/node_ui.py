class NodoUI:
    def __init__(self, canvas, x, y, radio, number):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radio = radio
        self.number = number
        self.draw()

    
    def draw(self):
        x0 = self.x - self.radio
        y0 = self.y - self.radio
        x1 = self.x + self.radio
        y1 = self.y + self.radio
        self.canvas.create_oval(x0, y0, x1, y1, fill="lightblue", outline="black")
        self.canvas.create_text(self.x, self.y, text=("q" + str(self.number)), font=("Arial", 12))

    def create_node(self):
        pass

    def join_node(self, starting_position, ending_position):
        pass

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y