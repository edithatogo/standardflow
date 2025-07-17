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
        if self.data['diagram_type'] == 'STROBE':
            self._build_strobe_graph()
        elif self.data['diagram_type'] == 'STROBE_COHORT':
            self._build_cohort_graph()

    def _build_strobe_graph(self):
        """Builds the graph for the standard STROBE flow diagram."""
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

    def _build_cohort_graph(self):
        """Builds the graph for the STROBE flow diagram for cohort studies."""
        with self.dot.subgraph(name='cluster_exposed') as c:
            c.attr(label='Exposed Group')
            c.node('A', f'Potentially eligible (n={self.data["exposed_group_potentially_eligible"]})')
            c.node('B', f'Assessed for eligibility (n={self.data["exposed_group_assessed_for_eligibility"]})')
            c.node('C', f'Excluded (n={self.data["exposed_group_excluded"]})\n' +
                       '\n'.join(self.data.get("reasons_for_exposed_group_exclusion", [])))
            c.node('D', f'Included in study (n={self.data["exposed_group_included"]})')
            c.node('E', f'Lost to follow-up (n={self.data["exposed_group_lost_to_follow_up"]})\n' +
                       '\n'.join(self.data.get("reasons_for_exposed_group_loss_to_follow_up", [])))
            c.node('F', f'Analysed (n={self.data["exposed_group_analysed"]})')
            c.edge('A', 'B')
            c.edge('B', 'C')
            c.edge('B', 'D')
            c.edge('D', 'E')
            c.edge('D', 'F')

        with self.dot.subgraph(name='cluster_unexposed') as c:
            c.attr(label='Unexposed Group')
            c.node('G', f'Potentially eligible (n={self.data["unexposed_group_potentially_eligible"]})')
            c.node('H', f'Assessed for eligibility (n={self.data["unexposed_group_assessed_for_eligibility"]})')
            c.node('I', f'Excluded (n={self.data["unexposed_group_excluded"]})\n' +
                       '\n'.join(self.data.get("reasons_for_unexposed_group_exclusion", [])))
            c.node('J', f'Included in study (n={self.data["unexposed_group_included"]})')
            c.node('K', f'Lost to follow-up (n={self.data["unexposed_group_lost_to_follow_up"]})\n' +
                       '\n'.join(self.data.get("reasons_for_unexposed_group_loss_to_follow_up", [])))
            c.node('L', f'Analysed (n={self.data["unexposed_group_analysed"]})')
            c.edge('G', 'H')
            c.edge('H', 'I')
            c.edge('H', 'J')
            c.edge('J', 'K')
            c.edge('J', 'L')

    def generate(self, output_filename="strobe.png"):
        """
        Generates the STROBE diagram and saves it to a file.

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

        print(f"STROBE diagram saved as {output_filename}")
