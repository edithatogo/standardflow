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

if __name__ == '__main__':
    unittest.main()
