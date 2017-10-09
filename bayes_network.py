

class BayesNode:
    """Class that represents a node in the Bayes Network
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def read_nodes():
    """Parser for reading node names
    RETURNS:
    - list of BayesNodes created
    """
    while True:
        current_input = input()
        if current_input == '[Nodes]':
            break
    return [BayesNode(x) for x in input().replace(' ', '').split(',')]    

def main():
    """Main program
    """
    nodes = read_nodes()
    print(nodes)


if __name__ == '__main__':
    main()