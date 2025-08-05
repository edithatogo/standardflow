import unittest
import os
import json
from src.consort_cluster import ConsortClusterDiagram

class TestConsortCluster(unittest.TestCase):
    def setUp(self):
        """Set up test data and output file paths."""
        with open('data/consort_cluster_data.json', 'r') as f:
            self.data = json.load(f)
        self.output_png = "test_consort_cluster.png"
        self.snapshot_file = "tests/snapshots/consort_cluster.dot"
        self.consort = ConsortClusterDiagram(self.data)

    def tearDown(self):
        """Tear down test files."""
        if os.path.exists(self.output_png):
            os.remove(self.output_png)

    def test_generate_consort_cluster_diagram_png(self):
        """Test that the CONSORT cluster diagram is generated as a PNG file."""
        self.consort.save(self.output_png)
        self.assertTrue(os.path.exists(self.output_png))

    def test_snapshot(self):
        """Test that the generated dot source matches the snapshot."""
        self.consort.build_graph()
        generated_dot = self.consort.dot.source
        with open(self.snapshot_file, 'r') as f:
            snapshot_dot = f.read()
        self.assertEqual(generated_dot.strip(), snapshot_dot.strip())

if __name__ == '__main__':
    unittest.main()
