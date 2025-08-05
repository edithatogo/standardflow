import argparse
import json
from jsonschema import validate
from diagram import Diagram
from consort import ConsortDiagram
from strobe import StrobeDiagram
from prisma import PrismaDiagram
from checklist import Checklist

def generate_artifact(input_path, output_path, schema_dir='schemas'):
    with open(input_path, 'r') as f:
        data = json.load(f)

    diagram_type = data.get("diagram_type")
    if not diagram_type:
        raise ValueError("The 'diagram_type' key is missing from the JSON file.")

    schema_path = f"{schema_dir}/{diagram_type.lower()}_schema.json"
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)

    if diagram_type == "CONSORT":
        diagram = ConsortDiagram(data)
    elif diagram_type == "STROBE":
        diagram = StrobeDiagram(data)
    elif diagram_type == "PRISMA":
        diagram = PrismaDiagram(data)
    elif diagram_type.endswith("_CHECKLIST"):
        diagram = Checklist(data)
    else:
        raise ValueError(f"Unknown diagram type: {diagram_type}")

    if output_path.endswith(".md"):
        diagram.to_markdown(output_path)
    else:
        diagram.to_png(output_path)

    print(f"{diagram_type} diagram saved as {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate a diagram or checklist from a JSON file.")
    parser.add_argument("input", help="Path to the input JSON file.")
    parser.add_argument("-o", "--output", help="Output file name. The format is determined by the file extension (e.g., .png, .svg, .pdf, .tiff, .eps, .md).")
    parser.add_argument("--schema-dir", help="Directory where the schema files are located.", default="schemas")
    args = parser.parse_args()
    generate_artifact(args.input, args.output, args.schema_dir)

if __name__ == "__main__":
    main()
