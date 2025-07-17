import graphviz
import json
import argparse
import os
import subprocess
from jsonschema import validate

class PrismaDiagram:
    """
    A class to generate PRISMA 2020 flow diagrams.
    """
    def __init__(self, data):
        """
        Initializes the PrismaDiagram object.

        Args:
            data (dict): A dictionary containing the PRISMA data.
        """
        self.data = data
        self.dot = graphviz.Digraph(comment='PRISMA 2020 Flow Diagram')
        self.dot.attr('node', shape='box')

    def _build_graph(self):
        """Builds the graph structure."""
        self.dot.node('A', f'Records identified through database searching\n(n = {self.data["records_identified"]})')
        self.dot.node('B', f'Records after duplicates removed\n(n = {self.data["records_after_duplicates_removed"]})')
        self.dot.node('C', f'Records screened\n(n = {self.data["records_screened"]})')
        self.dot.node('D', f'Records excluded\n(n = {self.data["records_excluded"]})')
        self.dot.node('E', f'Full-text articles assessed for eligibility\n(n = {self.data["full_text_articles_assessed"]})')
        self.dot.node('F', f'Full-text articles excluded, with reasons\n(n = {self.data["full_text_articles_excluded"]})')
        self.dot.node('G', f'Studies included in qualitative synthesis\n(n = {self.data["studies_included"]})')
        self.dot.node('H', f'Studies included in quantitative synthesis (meta-analysis)\n(n = {self.data["studies_included"]})')

        self.dot.edge('A', 'B')
        self.dot.edge('B', 'C')
        self.dot.edge('C', 'D')
        self.dot.edge('C', 'E')
        self.dot.edge('E', 'F')
        self.dot.edge('E', 'G')
        self.dot.edge('G', 'H')

    def generate(self, output_filename="prisma.png"):
        """
        Generates the PRISMA diagram and saves it to a file.

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

        print(f"PRISMA diagram saved as {output_filename}")

# No main function needed here anymore.
