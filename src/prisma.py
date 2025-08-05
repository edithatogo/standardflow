from src.diagram import Diagram

class PrismaDiagram(Diagram):
    def __init__(self, data):
        super().__init__(data)

    def build_graph(self):
        self.dot.node('A', f"Records identified (n={self.data['databases'] + self.data['registers']})")
        self.dot.node('B', f"Records after duplicates removed (n={self.data['duplicates']})")
        self.dot.node('C', f"Records screened (n={self.data['duplicates']})")
        self.dot.node('D', f"Records excluded (n={self.data['excluded_records']})")
        self.dot.node('E', f"Full-text articles assessed for eligibility (n={self.data['retrieved_reports']})")
        self.dot.node('F', f"Full-text articles excluded (n={self.data['excluded_reports']})")
        self.dot.node('G', f"Studies included in qualitative synthesis (n={self.data['studies_included']})")
        self.dot.node('H', f"Studies included in quantitative synthesis (n={self.data['included_in_synthesis']})")

        self.dot.edge('A', 'B')
        self.dot.edge('B', 'C')
        self.dot.edge('C', 'D')
        self.dot.edge('C', 'E')
        self.dot.edge('E', 'F')
        self.dot.edge('E', 'G')
        self.dot.edge('G', 'H')

    def save(self, path):
        self.dot.render(path, view=False)
