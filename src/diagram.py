from graphviz import Digraph
import os

class Diagram:
    def __init__(self, data):
        self.data = data
        self.dot = Digraph()

    def build_graph(self):
        raise NotImplementedError

    def save(self, path):
        output_path = os.path.abspath(path)
        self.dot.render(output_path, format='png', view=False, cleanup=False)
        print(f"File exists: {os.path.exists(f'{output_path}.png')}")
