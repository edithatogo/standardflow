from src.diagram import Diagram

class StrobeDiagram(Diagram):
    def __init__(self, data):
        super().__init__(data)

    def build_graph(self):
        self.dot.node('A', f"Potentially eligible (n={self.data['potentially_eligible']})")
        self.dot.node('B', f"Assessed for eligibility (n={self.data['assessed_for_eligibility']})")
        self.dot.node('C', f"Excluded before study (n={self.data['excluded_before_study']})")
        self.dot.node('D', f"Included in study (n={self.data['included_in_study']})")
        self.dot.node('E', f"Lost to follow-up (n={self.data['lost_to_follow_up']})")
        self.dot.node('F', f"Incomplete data (n={self.data['incomplete_data']})")
        self.dot.node('G', f"Analysed (n={self.data['analysed']})")

        self.dot.edge('A', 'B')
        self.dot.edge('B', 'C')
        self.dot.edge('B', 'D')
        self.dot.edge('D', 'E')
        self.dot.edge('D', 'F')
        self.dot.edge('D', 'G')

    def save(self, path):
        self.dot.render(path, view=False)
