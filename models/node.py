


class Node:
    def __init__(self):
        self.routes = {} # Espera algo como 'valor': set(lista_de_rutas). Si no te gusta el enfoque me dices
    
    def add_route(self, destination_node, transition_value):
        pass

    def exists_transition_value(self, transition_value):
        return transition_value in self.routes