import click

@click.group(help="A command-line tool for generating research artifacts like flow diagrams and checklists for scientific reporting.")
def cli():
    pass

import os
import json

@cli.command(help="Lists the available diagram and checklist types that can be generated.")
def list():
    click.echo("Available diagram types:")
    click.echo("- PRISMA")
    click.echo("- CONSORT")
    click.echo("- STROBE")

    click.echo("\nAvailable checklist types:")
    click.echo("- CONSORT")
    click.echo("- CARE")

from .main import generate_artifact

@cli.command(help="""
Generates a diagram or checklist from a JSON file.

Example:
    python -m src.cli generate examples/data/consort_data.json -o consort.png
""")
@click.argument('input', type=click.Path(exists=True), required=False)
@click.option('--output', '-o', default='output', help='Output file name.')
@click.option('--style', '-s', type=click.Path(exists=True), help='Path to a JSON file with styling information.')
@click.option('--set', multiple=True, help='Set a key-value pair in the data, e.g., --set title="My Diagram".')
@click.option('--interactive', is_flag=True, help='Run in interactive mode.')
def generate(input, output, style, set, interactive):
    if interactive:
        diagram_type = click.prompt("Select a diagram or checklist type", type=click.Choice(['CONSORT', 'PRISMA', 'STROBE', 'CARE_CHECKLIST'], case_sensitive=False))
        data = {'diagram_type': diagram_type}

        schema_path = f"schemas/{diagram_type.lower()}_schema.json"
        with open(schema_path, 'r') as f:
            schema = json.load(f)

        for prop, prop_schema in schema['properties'].items():
            if prop in ['diagram_type', 'style']:
                continue

            prompt_text = prop_schema.get('description', prop)
            data[prop] = click.prompt(prompt_text, type=str)

        temp_file = "interactive_input.json"
        with open(temp_file, 'w') as f:
            json.dump(data, f)

        generate_artifact(temp_file, output, style_path=style, set_values=set, schema_dir='schemas')
        os.remove(temp_file)
        return
    elif not input:
        raise click.UsageError("Missing argument 'INPUT'. Provide a path to a JSON file or use --interactive.")

    generate_artifact(input, output, style_path=style, set_values=set, schema_dir='schemas')

from .main import validate_data
from jsonschema.exceptions import ValidationError

@cli.command(help="Validates a JSON data file against the appropriate schema.")
@click.argument('input', type=click.Path(exists=True))
def validate(input):
    """Validates a JSON data file against the appropriate schema."""
    with open(input, 'r') as f:
        data = json.load(f)
    try:
        validate_data(data, schema_dir='schemas')
        click.echo("Validation successful!")
    except ValidationError as e:
        click.echo("Validation failed:")
        click.echo(f"  - {e.message}")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")

@cli.command(help="Lists available schemas or prints a specific schema.")
@click.argument('name', required=False)
def schemas(name):
    """Lists available schemas or prints a specific schema."""
    schema_dir = 'schemas'
    if name:
        schema_path = os.path.join(schema_dir, f"{name.lower()}_schema.json")
        if os.path.exists(schema_path):
            with open(schema_path, 'r') as f:
                click.echo(f.read())
        else:
            click.echo(f"Schema '{name}' not found.")
    else:
        click.echo("Available schemas:")
        for filename in os.listdir(schema_dir):
            if filename.endswith("_schema.json"):
                click.echo(f"- {filename.replace('_schema.json', '').upper()}")

if __name__ == '__main__':
    cli()
