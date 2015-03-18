import click

from barcode.util import get_barcodes


@click.command()
@click.argument('input', type=click.File('U'), required=True)
@click.argument('output', type=click.File('w'), required=False)
def cli(input, output):
    """This scripts generates a pdf of barcodes"""
    print input
    get_barcodes(input, output)

if __name__ == '__main__':
    cli()
