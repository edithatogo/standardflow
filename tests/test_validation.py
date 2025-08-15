import unittest
from jsonschema import validate, ValidationError
from src.main import validate_data

class TestValidation(unittest.TestCase):

    def test_missing_diagram_type(self):
        data = {"foo": "bar"}
        with self.assertRaises(ValueError):
            validate_data(data, schema_dir='schemas')

    def test_validation(self):
        schema = {
            "type": "object",
            "properties": {
                "foo": {"type": "number"}
            }
        }
        data = {"foo": "bar"}
        with self.assertRaises(ValidationError):
            validate(instance=data, schema=schema)

if __name__ == '__main__':
    unittest.main()
