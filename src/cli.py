import click

@click.group()
def cli():
    """A command-line tool for generating research artifacts."""
    pass

import os
import json

@cli.command()
def list():
    """Lists the available diagram and checklist types."""
    click.echo("Available diagram types:")
    click.echo("- PRISMA")
    click.echo("- CONSORT")
    click.echo("- STROBE")

    click.echo("\nAvailable checklist types:")
    click.echo("- CONSORT")

from .main import generate_artifact

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', default='output', help='Output file name.')
def generate(input, output):
    """Generates a diagram or checklist from a JSON file."""
    generate_artifact(input, output, schema_dir='schemas')

if __name__ == '__main__':
    cli()
