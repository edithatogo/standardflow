from diagram import Diagram

class PrismaDiagram(Diagram):
    def __init__(self, data):
        super().__init__(data)
        self.build_graph()

    def build_graph(self):
        self.dot.node('A', f"Records identified (n={self.data['records_identified']})")
        self.dot.node('B', f"Records after duplicates removed (n={self.data['records_after_duplicates_removed']})")
        self.dot.node('C', f"Records screened (n={self.data['records_screened']})")
        self.dot.node('D', f"Records excluded (n={self.data['records_excluded']})")
        self.dot.node('E', f"Full-text articles assessed for eligibility (n={self.data['full_text_articles_assessed']})")
        self.dot.node('F', f"Full-text articles excluded (n={self.data['full_text_articles_excluded']})")
        self.dot.node('G', f"Studies included in qualitative synthesis (n={self.data['studies_included']})")

        self.dot.edge('A', 'B')
        self.dot.edge('B', 'C')
        self.dot.edge('C', 'D')
        self.dot.edge('C', 'E')
        self.dot.edge('E', 'F')
        self.dot.edge('E', 'G')

    def to_dot(self, output_path):
        self.dot.render(output_path, format='dot', cleanup=True)

    def to_png(self, output_path):
        self.dot.render(output_path, format='png', cleanup=True)
