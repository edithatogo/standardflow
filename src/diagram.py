from graphviz import Digraph

class Diagram:
    def __init__(self, data):
        self.data = data
        self.dot = Digraph()

    def to_dot(self, output_path):
        self.dot.render(output_path, format='dot', cleanup=True)

    def to_png(self, output_path):
        self.dot.render(output_path, format='png', cleanup=True)

    def to_markdown(self, output_path):
        # This is a placeholder implementation.
        # A real implementation would convert the diagram to markdown.
        with open(output_path, 'w') as f:
            f.write("# Diagram\n")
            f.write("```dot\n")
            f.write(self.dot.source)
            f.write("\n```\n")

class Checklist(Diagram):
    def __init__(self, data):
        super().__init__(data)

    def to_dot(self, output_path):
        # Checklists don't have a dot representation
        pass

    def to_png(self, output_path):
        # Checklists don't have a png representation
        pass

    def to_markdown(self, output_path):
        # This is a placeholder implementation.
        # A real implementation would convert the checklist to markdown.
        with open(output_path, 'w') as f:
            f.write(f"# {self.data['title']}\n\n")
            for item in self.data['items']:
                f.write(f"## {item['section']}\n\n")
                f.write(f"**{item['id']}** - {item['description']}\n\n")
