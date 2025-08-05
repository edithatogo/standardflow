from src.diagram import Diagram

class ConsortClusterDiagram(Diagram):
    def __init__(self, data):
        super().__init__(data)

    def build_graph(self):
        self.dot.node('A', f"Assessed for eligibility (n={self.data['assessed_for_eligibility']})")
        self.dot.node('B', f"Excluded (n={self.data['excluded']})")
        self.dot.node('C', f"Randomized (n={self.data['randomized']})")
        self.dot.node('D', f"Allocated to intervention (n={self.data['intervention_group_allocated']})")
        self.dot.node('E', f"Received intervention (n={self.data['intervention_group_received']})")
        self.dot.node('F', f"Lost to follow-up (n={self.data['intervention_group_lost_to_follow_up']})")
        self.dot.node('G', f"Discontinued intervention (n={self.data['intervention_group_discontinued']})")
        self.dot.node('H', f"Analysed (n={self.data['intervention_group_analysed']})")
        self.dot.node('I', f"Allocated to control (n={self.data['control_group_allocated']})")
        self.dot.node('J', f"Received control (n={self.data['control_group_received']})")
        self.dot.node('K', f"Lost to follow-up (n={self.data['control_group_lost_to_follow_up']})")
        self.dot.node('L', f"Discontinued control (n={self.data['control_group_discontinued']})")
        self.dot.node('M', f"Analysed (n={self.data['control_group_analysed']})")

        self.dot.edge('A', 'C')
        self.dot.edge('A', 'B')
        self.dot.edge('C', 'D')
        self.dot.edge('C', 'I')
        self.dot.edge('D', 'E')
        self.dot.edge('E', 'F')
        self.dot.edge('E', 'G')
        self.dot.edge('E', 'H')
        self.dot.edge('I', 'J')
        self.dot.edge('J', 'K')
        self.dot.edge('J', 'L')
        self.dot.edge('J', 'M')

    def save(self, path):
        self.dot.render(path, format='png', view=False)
