

class BayesNode:
    """Class that represents a node in the Bayes Network
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class BayesNetwork:
    """Class that represents a Bayes Network
    """

    def __init__(self, node_names):
        self.nodes = [BayesNode(name) for name in node_names]
        self.nodes_index = {node.name: i for i, node in enumerate(self.nodes)}

def read_nodes():
    """Parser for reading node names
    RETURNS:
    - a new BayesNetwork
    """
    while True:
        current_input = input()
        if current_input == '[Nodes]':
            break
    return BayesNetwork(input().replace(' ', '').split(','))

def read_probability_tables():
    """Parser for prob tables, it adds tables to the nodes
    """
    while True:
        current_input = input()
        if current_input == '[Probabilities]':
            break
    while True:
        probability = input()
        if probability == '':
            break


def main():
    """Main program
    """
    bayes_net = read_nodes()
    print(bayes_net.nodes_index)


if __name__ == '__main__':
    main()