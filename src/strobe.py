import graphviz
import os
import subprocess

class StrobeDiagram:
    """
    A class to generate STROBE 2007 flow diagrams.
    """
    def __init__(self, data):
        """
        Initializes the StrobeDiagram object.

        Args:
            data (dict): A dictionary containing the STROBE data.
        """
        self.data = data
        self.dot = graphviz.Digraph(comment='STROBE 2007 Flow Diagram')
        self.dot.attr('node', shape='box')

    def _build_graph(self):
        """Builds the graph structure."""
        # TODO: Implement the graph building logic for the STROBE diagram
        pass

    def generate(self, output_filename="strobe.png"):
        """
        Generates the STROBE diagram and saves it to a file.

        Args:
            output_filename (str): The name of the output file.
        """
        self._build_graph()

        file_format = os.path.splitext(output_filename)[1][1:]

        if file_format == 'tiff':
            # Generate a temporary PNG file and then convert it to TIFF
            temp_png_base = os.path.splitext(output_filename)[0]
            self.dot.render(temp_png_base, format='png', view=False, cleanup=True)
            temp_png_filename = temp_png_base + '.png'
            subprocess.run(['convert', temp_png_filename, output_filename])
            os.remove(temp_png_filename)
        else:
            base = os.path.splitext(output_filename)[0]
            self.dot.render(base, format=file_format, view=False, cleanup=True)

        print(f"STROBE diagram saved as {output_filename}")
