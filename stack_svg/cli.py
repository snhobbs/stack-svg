"""Console script for stack_svg."""
import sys
import click
import svgutils
from . import __version__


def make_layer_stack_image(fnames, fout=None):
    """
    Take a set of layers as a dataframe
    """
    files_ = []
    for f in fnames:
        try:
            files_.append(svgutils.compose.SVG(f))
        except FileNotFoundError:
            pass
    return svgutils.compose.Figure(0, 0, *files_)


@click.command()
@click.option("-o", default="svg-stack.svg")
@click.option("-f", multiple=True, required=True, help="Files to stack, layer is done by order")
def main(o, f):
    """Console script for stack_svg."""
    fig = make_layer_stack_image(f, fout=o)
    fig.save(o)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
