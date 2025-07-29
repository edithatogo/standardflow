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

    def _apply_styles(self):
        """Applies the styles from the data to the graph."""
        if 'style' in self.data:
            style = self.data['style']
            if 'box_color' in style:
                self.dot.attr('node', style='filled', fillcolor=style['box_color'])
            if 'font_color' in style:
                self.dot.attr('node', fontcolor=style['font_color'])
                self.dot.attr('edge', fontcolor=style['font_color'])
            if 'font_name' in style:
                self.dot.attr('node', fontname=style['font_name'])
                self.dot.attr('edge', fontname=style['font_name'])
            if 'font_size' in style:
                self.dot.attr('node', fontsize=style['font_size'])
                self.dot.attr('edge', fontsize=style['font_size'])
            if 'arrow_color' in style:
                self.dot.attr('edge', color=style['arrow_color'])

    def _build_graph(self):
        """Builds the graph structure."""
        if self.data['diagram_type'] == 'PRISMA':
            self._build_prisma_graph()
        elif self.data['diagram_type'] == 'PRISMA_2020_UPDATED':
            self._build_updated_prisma_graph()

    def _build_prisma_graph(self):
        """Builds the graph for the standard PRISMA 2020 flow diagram."""
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

    def _build_updated_prisma_graph(self):
        """Builds the graph for the updated PRISMA 2020 flow diagram."""
        self.dot.node('A', f'Studies included in previous version of review\n(n = {self.data["previous_studies"]})')
        self.dot.node('B', f'New records identified\n(n = {self.data["new_records_identified"]})')
        self.dot.node('C', f'New records after duplicates removed\n(n = {self.data["new_records_after_duplicates_removed"]})')
        self.dot.node('D', f'New records screened\n(n = {self.data["new_records_screened"]})')
        self.dot.node('E', f'New records excluded\n(n = {self.data["new_records_excluded"]})')
        self.dot.node('F', f'New full-text articles assessed for eligibility\n(n = {self.data["new_full_text_articles_assessed"]})')
        self.dot.node('G', f'New full-text articles excluded, with reasons\n(n = {self.data["new_full_text_articles_excluded"]})')
        self.dot.node('H', f'New studies included in qualitative synthesis\n(n = {self.data["new_studies_included"]})')
        self.dot.node('I', f'Total studies included in qualitative synthesis\n(n = {self.data["total_studies_included"]})')
        self.dot.node('J', f'Total studies included in quantitative synthesis (meta-analysis)\n(n = {self.data["total_studies_included"]})')

        self.dot.edge('A', 'I')
        self.dot.edge('B', 'C')
        self.dot.edge('C', 'D')
        self.dot.edge('D', 'E')
        self.dot.edge('D', 'F')
        self.dot.edge('F', 'G')
        self.dot.edge('F', 'H')
        self.dot.edge('H', 'I')
        self.dot.edge('I', 'J')

    def generate(self, output_filename="prisma.png"):
        """
        Generates the PRISMA diagram and saves it to a file.

        Args:
            output_filename (str): The name of the output file.
        """
        self._apply_styles()
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
