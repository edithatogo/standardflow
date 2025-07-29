import unittest
from jsonschema import validate, ValidationError

class TestValidation(unittest.TestCase):

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
