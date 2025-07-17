import unittest
import os
import json
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from prisma import PrismaDiagram

class TestPrisma(unittest.TestCase):

    def setUp(self):
        """Set up test data and output file paths."""
        self.data = {
            "records_identified": 1000,
            "records_after_duplicates_removed": 800,
            "records_screened": 800,
            "records_excluded": 200,
            "full_text_articles_assessed": 600,
            "full_text_articles_excluded": 300,
            "studies_included": 300
        }
        self.output_png = "test_prisma.png"
        self.output_svg = "test_prisma.svg"
        self.output_pdf = "test_prisma.pdf"
        self.output_tiff = "test_prisma.tiff"
        self.output_eps = "test_prisma.eps"
        self.prisma = PrismaDiagram(self.data)

    def tearDown(self):
        """Remove generated files after each test."""
        for f in [self.output_png, self.output_svg, self.output_pdf, self.output_tiff, self.output_eps]:
            if os.path.exists(f):
                # We need to also remove the source file for some formats
                if os.path.splitext(f)[1] in ['.eps', '.pdf', '.svg', '.png']:
                    if os.path.exists(os.path.splitext(f)[0]):
                        os.remove(os.path.splitext(f)[0])
                os.remove(f)


    def test_generate_prisma_diagram_png(self):
        """Test that the PRISMA diagram is generated as a PNG file."""
        self.prisma.generate(self.output_png)
        self.assertTrue(os.path.exists(self.output_png))

    def test_generate_prisma_diagram_svg(self):
        """Test that the PRISMA diagram is generated as an SVG file."""
        self.prisma.generate(self.output_svg)
        self.assertTrue(os.path.exists(self.output_svg))

    def test_generate_prisma_diagram_pdf(self):
        """Test that the PRISMA diagram is generated as a PDF file."""
        self.prisma.generate(self.output_pdf)
        self.assertTrue(os.path.exists(self.output_pdf))

    def test_generate_prisma_diagram_tiff(self):
        """Test that the PRISMA diagram is generated as a TIFF file."""
        self.prisma.generate(self.output_tiff)
        self.assertTrue(os.path.exists(self.output_tiff))

    def test_generate_prisma_diagram_eps(self):
        """Test that the PRISMA diagram is generated as an EPS file."""
        self.prisma.generate(self.output_eps)
        self.assertTrue(os.path.exists(self.output_eps))

if __name__ == '__main__':
    unittest.main()
