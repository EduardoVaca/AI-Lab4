

class BayesNode(object):
    """Class that represents a node in the Bayes Network
    """

    def __init__(self, name):
        self.name = name
        self.parents = set()
        self.probabilities = []

    def __str__(self):
        return self.name + '\nParents: ' + ''.join([x.name for x in self.parents]) + '\n' + str(self.probabilities)

    def __hash__(self):
        return hash(self.name)

    def add_probability(self, parents_cond, parents, prob):
        """Adds probability value to probability table"""
        self.parents.update(parents)
        self.probabilities.append((parents_cond, prob))        
        
class BayesNetwork(object):
    """Class that represents a Bayes Network
    """

    def __init__(self, node_names):
        self.nodes = [BayesNode(name) for name in node_names]
        self.nodes_index = {node.name: i for i, node in enumerate(self.nodes)}

    def add_probability_to_node(self, node_name, parents_cond, prob):
        """Adds probability values to one of its nodes
        """
        self.nodes[self.nodes_index[node_name]].add_probability(parents_cond, [self.nodes[self.nodes_index[x[1:]]] for x in parents_cond], prob)

def read_nodes():
    """Parser for reading node names
    RETURNS:
    - a new BayesNetwork
    """
    return BayesNetwork(input().replace(' ', '').split(','))

def read_probability_tables(bayes_net):
    """Parser for prob tables, it adds tables to the nodes
    PARAMS:
    - bayer_net : bayes network on which probabilities will be added
    """
    prob_count = int(input())
    for _ in range(prob_count):          
        values = input().replace(' ', '').split('=')
        var_assignments = values[0].split('|')
        parents_cond = [] if len(var_assignments) <= 1 else var_assignments[1].split(',')
        bayes_net.add_probability_to_node(var_assignments[0][1:], parents_cond, values[1])

def read_execute_queries(bayes_net):
    """Read and execute queries to a given bayes net
    PARAMS:
    - bayes_net : bayes network on which queries will be made
    """
    queries_count = int(input())
    for _ in range(queries_count):
        # QUERY HERE.
       break  


def main():
    """Main program
    """
    bayes_net = read_nodes()
    read_probability_tables(bayes_net)
    print(bayes_net.nodes[0])



if __name__ == '__main__':
    main()