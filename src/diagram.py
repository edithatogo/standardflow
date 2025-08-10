from graphviz import Digraph
import os

class Diagram:
    def __init__(self, data):
        self.data = data
        self.dot = Digraph()

    def build_graph(self):
        raise NotImplementedError

    def save(self, path):
        output_path_without_ext, ext = os.path.splitext(path)
        format = ext.lstrip('.')

        if format == 'typ':
            # For typst, we first render to svg
            svg_path = output_path_without_ext + '.svg'
            self.dot.render(output_path_without_ext, format='svg', view=False, cleanup=True)

            # Then we create a .typ file that includes the svg
            with open(path, 'w') as f:
                f.write(f'#image("{os.path.basename(svg_path)}")')
        else:
            self.dot.render(output_path_without_ext, format=format, view=False, cleanup=True)
