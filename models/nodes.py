class Nodes:
    def __init__(self, regular_expression):
        self.regular_expression = regular_expression
        self.routes = {}
        self.special_characters = (ord('+'), ord('*'), ord(','), ord('('), ord(')'), ord('|'), ord('?'), ord('•'))

    def detect_nodes(self):
        i = 0
        parenthesis_locations = []
        while i < len(self.regular_expression):
            if ord(self.regular_expression[i]) == ord('('):
                parenthesis_locations.append({'init': i, 'finish': None})
            if ord(self.regular_expression[i]) == ord(')'):
                pivot_stack = []
                while parenthesis_locations:
                    if parenthesis_locations[-1].finish == None:
                        parenthesis_locations[-1].finish = i
                        break
                    pivot_stack.append(parenthesis_locations.pop())
                while pivot_stack:
                    parenthesis_locations.append(pivot_stack.pop())
                        

                    


                
