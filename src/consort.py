from diagram import Diagram

class ConsortDiagram(Diagram):
    def __init__(self, data):
        super().__init__(data)
        self.build_graph()

    def build_graph(self):
        self.dot.node('A', f"Assessed for eligibility (n={self.data['assessed_for_eligibility']})")
        self.dot.node('B', f"Excluded (n={self.data['excluded']})")
        self.dot.node('C', f"Randomized (n={self.data['randomized']})")
        self.dot.node('D', f"Allocated to intervention (n={self.data['allocated_to_intervention']})")
        self.dot.node('E', f"Received allocated intervention (n={self.data['received_allocated_intervention']})")
        self.dot.node('F', f"Did not receive allocated intervention (n={self.data['did_not_receive_allocated_intervention']})")
        self.dot.node('G', f"Lost to follow-up (n={self.data['lost_to_follow_up']})")
        self.dot.node('H', f"Discontinued intervention (n={self.data['discontinued_intervention']})")
        self.dot.node('I', f"Analysed (n={self.data['analysed']})")
        self.dot.node('J', f"Excluded from analysis (n={self.data['excluded_from_analysis']})")

        self.dot.edge('A', 'B')
        self.dot.edge('A', 'C')
        self.dot.edge('C', 'D')
        self.dot.edge('D', 'E')
        self.dot.edge('D', 'F')
        self.dot.edge('E', 'G')
        self.dot.edge('E', 'H')
        self.dot.edge('E', 'I')
        self.dot.edge('I', 'J')

    def to_dot(self, output_path):
        self.dot.render(output_path, format='dot', cleanup=True)

    def to_png(self, output_path):
        self.dot.render(output_path, format='png', cleanup=True)
