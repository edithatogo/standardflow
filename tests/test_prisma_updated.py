import unittest
import os
import json
from src.prisma import PrismaDiagram

class TestPrismaUpdated:
    def setup_method(self):
        """Set up test data and output file paths."""
        with open('data/prisma_2020_updated_data.json', 'r') as f:
            self.data = json.load(f)
        self.output_png = "test_prisma_updated.png"
        self.snapshot_file = "tests/snapshots/prisma_updated.dot"
        self.prisma = PrismaDiagram(self.data)

    def teardown_method(self):
        """Tear down test files."""
        if os.path.exists(self.output_png):
            os.remove(self.output_png)

    def test_generate_prisma_updated_diagram_png(self):
        """Test that the updated PRISMA diagram is generated as a PNG file."""
        self.prisma.save(self.output_png)
        assert os.path.exists(self.output_png)

    def test_snapshot(self, snapshot):
        """Test that the generated dot source matches the snapshot."""
        self.prisma.build_graph()
        generated_dot = self.prisma.dot.source
        snapshot.assert_match(generated_dot, 'prisma_updated.dot')
