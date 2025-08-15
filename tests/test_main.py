import unittest
import os
from src.main import generate_artifact

class TestMain(unittest.TestCase):
    def test_generate_artifact(self):
        output_file = os.path.abspath("test_generate_artifact.png")
        generate_artifact("data/prisma_data.json", output_file, schema_dir='schemas')
        import time
        time.sleep(1)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_generate_artifact_with_style(self):
        output_file = os.path.abspath("test_generate_artifact_with_style.png")
        generate_artifact("data/prisma_data.json", output_file, style_path="data/test_style.json", schema_dir='schemas')
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_generate_artifact_with_set(self):
        output_file = os.path.abspath("test_generate_artifact_with_set.png")
        generate_artifact("data/prisma_data.json", output_file, set_values=["studies_included=123"], schema_dir='schemas')
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_missing_diagram_type(self):
        output_file = os.path.abspath("test_missing_diagram_type.png")
        with self.assertRaises(ValueError):
            generate_artifact("data/missing_diagram_type.json", output_file, schema_dir='schemas')

    def test_generate_artifact_with_set_float_and_string(self):
        output_file = os.path.abspath("test_generate_artifact_with_set_float_and_string.png")
        generate_artifact("data/prisma_data.json", output_file, set_values=["studies_included=123.4", "diagram_type=PRISMA"], schema_dir='schemas')
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_generate_strobe_diagram(self):
        output_file = os.path.abspath("test_strobe_diagram.png")
        generate_artifact("data/strobe_data.json", output_file, schema_dir='schemas')
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_unknown_diagram_type(self):
        output_file = os.path.abspath("test_unknown_diagram_type.png")
        with self.assertRaises(ValueError):
            generate_artifact("data/unknown_diagram_type.json", output_file, schema_dir='schemas')

if __name__ == '__main__':
    unittest.main()
