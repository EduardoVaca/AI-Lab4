

class BayesNode:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def read_nodes():
    while True:
        current_input = input()
        if current_input == '[Nodes]':
            break
    return [BayesNode(x) for x in input().replace(' ', '').split(',')]    

nodes = read_nodes()
print(nodes)