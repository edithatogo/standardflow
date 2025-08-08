import unittest
import os
from graphviz import Digraph

class TestRendering(unittest.TestCase):
    def test_render(self):
        dot = Digraph()
        dot.node('A', 'Hello')
        dot.node('B', 'World')
        dot.edge('A', 'B')
        output_path = "test_render.png"
        dot.render(output_path, format='png', view=False, cleanup=True)
        self.assertTrue(os.path.exists(f"{output_path}.png"))
        os.remove(f"{output_path}.png")

if __name__ == '__main__':
    unittest.main()
