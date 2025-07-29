import graphviz
import os
import subprocess

class ConsortDiagram:
    """
    A class to generate CONSORT 2010 flow diagrams.
    """
    def __init__(self, data):
        """
        Initializes the ConsortDiagram object.

        Args:
            data (dict): A dictionary containing the CONSORT data.
        """
        self.data = data
        self.dot = graphviz.Digraph(comment='CONSORT 2010 Flow Diagram')
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
        if self.data['diagram_type'] == 'CONSORT':
            self._build_consort_graph()
        elif self.data['diagram_type'] == 'CONSORT_CLUSTER':
            self._build_cluster_graph()

    def _build_consort_graph(self):
        """Builds the graph for the standard CONSORT 2010 flow diagram."""
        self.dot.node('A', f'Assessed for eligibility (n={self.data["assessed_for_eligibility"]})')
        self.dot.node('B', f'Excluded (n={self.data["excluded"]})\n' +
                           '\n'.join(self.data.get("reasons_for_exclusion", [])))
        self.dot.node('C', f'Randomized (n={self.data["randomized"]})')
        self.dot.node('D', f'Allocated to intervention (n={self.data["allocated_to_intervention"]})')
        self.dot.node('E', f'Received allocated intervention (n={self.data["received_allocated_intervention"]})')
        self.dot.node('F', f'Did not receive allocated intervention (n={self.data["did_not_receive_allocated_intervention"]})\n' +
                           '\n'.join(self.data.get("reasons_for_not_receiving_intervention", [])))
        self.dot.node('G', f'Lost to follow-up (n={self.data["lost_to_follow_up"]})\n' +
                           '\n'.join(self.data.get("reasons_for_loss_to_follow_up", [])))
        self.dot.node('H', f'Discontinued intervention (n={self.data["discontinued_intervention"]})\n' +
                           '\n'.join(self.data.get("reasons_for_discontinuing_intervention", [])))
        self.dot.node('I', f'Analysed (n={self.data["analysed"]})')
        self.dot.node('J', f'Excluded from analysis (n={self.data["excluded_from_analysis"]})\n' +
                           '\n'.join(self.data.get("reasons_for_exclusion_from_analysis", [])))

        self.dot.edge('A', 'C')
        self.dot.edge('A', 'B')
        self.dot.edge('C', 'D')
        self.dot.edge('D', 'E')
        self.dot.edge('D', 'F')
        self.dot.edge('E', 'G')
        self.dot.edge('E', 'H')
        self.dot.edge('E', 'I')
        self.dot.edge('I', 'J')

    def _build_cluster_graph(self):
        """Builds the graph for the CONSORT 2010 flow diagram for cluster-randomised trials."""
        self.dot.node('A', f'Assessed for eligibility (n={self.data["clusters_assessed_for_eligibility"]} clusters)')
        self.dot.node('B', f'Excluded (n={self.data["clusters_excluded"]} clusters)\n' +
                           '\n'.join(self.data.get("reasons_for_cluster_exclusion", [])))
        self.dot.node('C', f'Randomized (n={self.data["clusters_randomized"]} clusters)')
        self.dot.node('D', f'Allocated to intervention (n={self.data["clusters_allocated_to_intervention"]} clusters, n={self.data["individuals_in_clusters_allocated_to_intervention"]} individuals)')
        self.dot.node('E', f'Lost to follow-up (n={self.data["clusters_lost_to_follow_up"]} clusters, n={self.data["individuals_lost_to_follow_up"]} individuals)\n' +
                           '\n'.join(self.data.get("reasons_for_cluster_loss_to_follow_up", [])))
        self.dot.node('F', f'Discontinued intervention (n={self.data["clusters_discontinued_intervention"]} clusters, n={self.data["individuals_discontinued_intervention"]} individuals)\n' +
                           '\n'.join(self.data.get("reasons_for_cluster_discontinuation", [])))
        self.dot.node('G', f'Analysed (n={self.data["clusters_analysed"]} clusters, n={self.data["individuals_analysed"]} individuals)')
        self.dot.node('H', f'Excluded from analysis (n={self.data["clusters_excluded_from_analysis"]} clusters, n={self.data["individuals_excluded_from_analysis"]} individuals)\n' +
                           '\n'.join(self.data.get("reasons_for_cluster_exclusion_from_analysis", [])))

        self.dot.edge('A', 'C')
        self.dot.edge('A', 'B')
        self.dot.edge('C', 'D')
        self.dot.edge('D', 'E')
        self.dot.edge('D', 'F')
        self.dot.edge('D', 'G')
        self.dot.edge('G', 'H')

    def generate(self, output_filename="consort.png"):
        """
        Generates the CONSORT diagram and saves it to a file.

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

        print(f"CONSORT diagram saved as {output_filename}")
