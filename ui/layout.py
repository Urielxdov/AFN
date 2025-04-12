import tkinter as tk
from nodo_ui import NodoUI

class Window:
    def __init__(self):
      self.window = tk.Tk()
      self.quantity_nodes = 0
      self.occupied_positions = set()
      self.initial_window()

    def initial_window(self):
      self.window.title("Autómatas Finitos No Deterministas")
      self.window.geometry("800x600")

        # Crear un canvas donde se dibujarán los nodos
      self.canvas = tk.Canvas(self.window, bg="white")
      self.canvas.pack(fill="both", expand=True)

      initial_pos = (20, 300)
      for i in range(10):
        x, y = self.generate_next_position(initial_pos)
        NodoUI(self.canvas, x, y, 20, self.)
        self.occupied_positions.add((x, y))

      self.window.mainloop()
      

    def add_nodes(self, node):
      position = self.generate_next_position()
      NodoUI(self.canvas, position[0], position[1], 20, self.quantity_nodes)
      self.quantity_nodes += 1

    def generate_next_position(self, start_position):
      NODE_DISTANCE = 100
      x, y = start_position

      intents = [
        (x + NODE_DISTANCE, y),
        (x + NODE_DISTANCE, y + NODE_DISTANCE),
        (x + NODE_DISTANCE, y - NODE_DISTANCE),
      ]

      for position in intents:
        if position not in self.occupied_positions:
          return position
      
      while True:
        x += NODE_DISTANCE
        if (x, y) not in self.occupied_positions:
          return (x, y) 
      
      
    

if __name__ == "__main__":
  Window()
