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
        self.dot.node('A', f'Potentially eligible participants (n={self.data["potentially_eligible"]})')
        self.dot.node('B', f'Assessed for eligibility (n={self.data["assessed_for_eligibility"]})')
        self.dot.node('C', f'Excluded before study (n={self.data["excluded_before_study"]})\n' +
                           '\n'.join(self.data.get("reasons_for_exclusion_before_study", [])))
        self.dot.node('D', f'Included in study (n={self.data["included_in_study"]})')
        self.dot.node('E', f'Lost to follow-up (n={self.data["lost_to_follow_up"]})\n' +
                           '\n'.join(self.data.get("reasons_for_loss_to_follow_up", [])))
        self.dot.node('F', f'Incomplete data (n={self.data["incomplete_data"]})\n' +
                           '\n'.join(self.data.get("reasons_for_incomplete_data", [])))
        self.dot.node('G', f'Analysed (n={self.data["analysed"]})')

        self.dot.edge('A', 'B')
        self.dot.edge('B', 'C')
        self.dot.edge('B', 'D')
        self.dot.edge('D', 'E')
        self.dot.edge('D', 'F')
        self.dot.edge('D', 'G')

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
