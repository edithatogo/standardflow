import unittest
import os
import json
from src.strobe import StrobeDiagram

class TestStrobeCohort(unittest.TestCase):
    def setUp(self):
        """Set up test data and output file paths."""
        with open('data/strobe_cohort_data.json', 'r') as f:
            self.data = json.load(f)
        self.output_png = "test_strobe_cohort.png"
        self.snapshot_file = "tests/snapshots/strobe_cohort.dot"
        self.strobe = StrobeDiagram(self.data)

    def tearDown(self):
        """Tear down test files."""
        if os.path.exists(self.output_png):
            os.remove(self.output_png)

    def test_generate_strobe_cohort_diagram_png(self):
        """Test that the STROBE cohort diagram is generated as a PNG file."""
        self.strobe.save(self.output_png)
        self.assertTrue(os.path.exists(self.output_png))

    def test_snapshot(self):
        """Test that the generated dot source matches the snapshot."""
        self.strobe.build_graph()
        generated_dot = self.strobe.dot.source
        with open(self.snapshot_file, 'r') as f:
            snapshot_dot = f.read()
        self.assertEqual(generated_dot.strip(), snapshot_dot.strip())

if __name__ == '__main__':
    unittest.main()
