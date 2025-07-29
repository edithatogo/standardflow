import unittest
import os
from click.testing import CliRunner
from src.cli import cli

class TestCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_list_command(self):
        result = self.runner.invoke(cli, ['list'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Available diagram types:", result.output)
        self.assertIn("- PRISMA", result.output)
        self.assertIn("- CONSORT", result.output)
        self.assertIn("- STROBE", result.output)
        self.assertIn("Available checklist types:", result.output)
        self.assertIn("- CONSORT", result.output)

    def test_generate_command(self):
        output_file = "test_generate_command.png"
        result = self.runner.invoke(cli, ['generate', 'data/prisma_data.json', '-o', output_file])
        self.assertEqual(result.exit_code, 0)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
