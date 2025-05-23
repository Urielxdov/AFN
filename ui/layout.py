import tkinter as tk
from node_ui import NodoUI

class Window:
    def __init__(self):
      self.window = tk.Tk()
      self.quantity_nodes = 0
      self.occupied_positions = set()
      self.NODE_RADIUS = 20
      self.initial_window()

    def initial_window(self):
      self.window.title("Autómatas Finitos No Deterministas")
      self.window.geometry("800x600")

        # Crear un canvas donde se dibujarán los nodos
      self.canvas = tk.Canvas(self.window, bg="white")
      self.canvas.pack(fill="both", expand=True)

      current_node = None
      for _ in range(10):
        current_node = self.add_nodes(current_node)
        self.add_nodes(current_node)
      

      self.window.mainloop()
      

    def add_nodes(self, node: NodoUI = None):
      self.quantity_nodes += 1
      
      position = (
        self.generate_next_position([20, 300]) # Separado por 20px del margen y acomodado mas o menos en la mitad del panel
        if node is None
        else self.generate_next_position([node.get_x(), node.get_y()])
      )

      self.occupied_positions.add(position)

      print(f"nodo: {[node.get_x(), node.get_y()] if node is not None else ""} \nnuevas: {position} \n\n\n")

      return NodoUI(self.canvas, position[0], position[1], self.NODE_RADIUS, self.quantity_nodes)


    def generate_next_position(self, start_position):
      NODE_DISTANCE = 100
      x, y = start_position

      intents = [
        (x + NODE_DISTANCE, y),
        (x + NODE_DISTANCE, y + NODE_DISTANCE),
        (x + NODE_DISTANCE, y - NODE_DISTANCE),
      ]
      print(f"intents: {intents}")

      for position in intents:
        if position not in self.occupied_positions:
          return position
      
      while True:
        x += NODE_DISTANCE
        if (x, y) not in self.occupied_positions:
          return (x, y) 
      
      
    

if __name__ == "__main__":
  Window()
