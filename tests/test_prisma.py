import unittest
import os
import json
from src.prisma import PrismaDiagram

class TestPrisma(unittest.TestCase):
    def setUp(self):
        """Set up test data and output file paths."""
        with open('data/prisma_data.json', 'r') as f:
            self.data = json.load(f)
            print(self.data)
        self.output_png = "test_prisma.png"
        self.output_svg = "test_prisma.svg"
        self.output_pdf = "test_prisma.pdf"
        self.prisma = PrismaDiagram(self.data)

    def tearDown(self):
        """Tear down test files."""
        if os.path.exists(self.output_png):
            os.remove(self.output_png)
        if os.path.exists(self.output_svg):
            os.remove(self.output_svg)
        if os.path.exists(self.output_pdf):
            os.remove(self.output_pdf)

    def test_generate_prisma_diagram_png(self):
        """Test that the PRISMA diagram is generated as a PNG file."""
        self.prisma.save(self.output_png)
        self.assertTrue(os.path.exists(self.output_png))

    def test_generate_prisma_diagram_svg(self):
        """Test that the PRISMA diagram is generated as an SVG file."""
        self.prisma.save(self.output_svg)
        self.assertTrue(os.path.exists(self.output_svg))

    def test_generate_prisma_diagram_pdf(self):
        """Test that the PRISMA diagram is generated as a PDF file."""
        self.prisma.save(self.output_pdf)
        self.assertTrue(os.path.exists(self.output_pdf))

    def test_snapshot(self):
        """Test that the generated dot source matches the snapshot."""
        self.snapshot_file = "tests/snapshots/prisma.dot"
        self.prisma.build_graph()
        generated_dot = self.prisma.dot.source
        with open(self.snapshot_file, 'r') as f:
            snapshot_dot = f.read()
        self.assertEqual(generated_dot.strip(), snapshot_dot.strip())

if __name__ == '__main__':
    unittest.main()
