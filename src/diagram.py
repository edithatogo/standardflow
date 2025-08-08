from graphviz import Digraph
import os

class Diagram:
    def __init__(self, data):
        self.data = data
        self.dot = Digraph()

    def build_graph(self):
        raise NotImplementedError

    def save(self, path):
        output_path_without_ext = os.path.splitext(path)[0]
        self.dot.render(output_path_without_ext, format='png', view=False, cleanup=True)
