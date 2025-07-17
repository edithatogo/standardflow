import unittest
import os
import json
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from checklist import Checklist

class TestChecklist(unittest.TestCase):

    def setUp(self):
        """Set up test data and output file paths."""
        with open('data/consort_checklist.json', 'r') as f:
            self.data = json.load(f)
        self.output_md = "test_checklist.md"
        self.checklist = Checklist(self.data)

    def tearDown(self):
        """Remove generated files after each test."""
        if os.path.exists(self.output_md):
            os.remove(self.output_md)

    def test_generate_checklist_md(self):
        """Test that the checklist is generated as a Markdown file."""
        self.checklist.generate(self.output_md)
        self.assertTrue(os.path.exists(self.output_md))

if __name__ == '__main__':
    unittest.main()
