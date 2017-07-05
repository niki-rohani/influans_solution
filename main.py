import click
import pandas as pd

@click.command()
@click.option('--entity_file', help='csv', required=True)
@click.option('--model', help='w2v', required=True)
@click.option('--words', help='csv', required=True)
@click.option('--out', help='csv', required=False)