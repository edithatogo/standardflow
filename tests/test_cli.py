import unittest
import os
import json
from click.testing import CliRunner
from src.cli import cli

class TestCli(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.valid_data_path = 'examples/data/consort_data.json'
        self.invalid_data_path = 'invalid_data.json'
        with open(self.invalid_data_path, 'w') as f:
            json.dump({"diagram_type": "CONSORT"}, f)

        self.style_path = 'style.json'
        with open(self.style_path, 'w') as f:
            json.dump({"box_color": "red"}, f)

    def tearDown(self):
        if os.path.exists(self.invalid_data_path):
            os.remove(self.invalid_data_path)
        if os.path.exists(self.style_path):
            os.remove(self.style_path)
        # Clean up any generated files
        for f in ['test.png', 'test.svg', 'test.pdf', 'test.typ', 'test.svg']:
            if os.path.exists(f):
                os.remove(f)

    def test_list_command(self):
        result = self.runner.invoke(cli, ['list'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Available diagram types:", result.output)

    def test_generate_command(self):
        result = self.runner.invoke(cli, ['generate', self.valid_data_path, '-o', 'test.png'])
        self.assertEqual(result.exit_code, 0)

    def test_generate_command_with_format(self):
        result = self.runner.invoke(cli, ['generate', self.valid_data_path, '-o', 'test.svg'])
        self.assertEqual(result.exit_code, 0)

    def test_validate_command_valid(self):
        result = self.runner.invoke(cli, ['validate', self.valid_data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Validation successful!", result.output)

    def test_validate_command_invalid(self):
        result = self.runner.invoke(cli, ['validate', self.invalid_data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Validation failed:", result.output)

    def test_schemas_command_list(self):
        result = self.runner.invoke(cli, ['schemas'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Available schemas:", result.output)

    def test_schemas_command_print(self):
        result = self.runner.invoke(cli, ['schemas', 'CONSORT'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("CONSORT 2010 flow diagram schema", result.output)

    def test_generate_with_style(self):
        result = self.runner.invoke(cli, ['generate', self.valid_data_path, '-o', 'test.png', '--style', self.style_path])
        self.assertEqual(result.exit_code, 0)

    def test_generate_with_set(self):
        result = self.runner.invoke(cli, ['generate', self.valid_data_path, '-o', 'test.png', '--set', 'randomized=999'])
        self.assertEqual(result.exit_code, 0)

    def test_generate_interactive(self):
        input_data = 'TEST\nvalue1\nvalue2\n'
        result = self.runner.invoke(cli, ['generate', '-o', 'test.png', '--interactive', '--schema', 'tests/test_schema.json'], input=input_data)
        self.assertNotEqual(result.exit_code, 0)
        self.assertIsInstance(result.exception, ValueError)
        self.assertIn("Unknown diagram_type", str(result.exception))

    def test_generate_no_input(self):
        result = self.runner.invoke(cli, ['generate'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Missing argument 'INPUT'", result.output)

if __name__ == '__main__':
    unittest.main()
