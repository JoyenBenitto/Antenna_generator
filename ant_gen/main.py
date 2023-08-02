import ant_gen.generator as gen
import ant_gen.utils as utils
from ant_gen.__init__ import __version__
from ant_gen.__init__ import __name__
import ant_gen.logger as log
import os
import click

# Top level group named 'cli'
@click.group()
@click.version_option(version=__version__)
def cli():
	f'''Command Line Interface for antenna generator'''

@click.version_option(version=__version__)
# CLI option 'log'.

@click.option(
    '--src',
    default="test/pass/pass1.yaml",
    help='provide the input with the parametersin standard format',
    required=False
)

# CLI option 'output.
# Expects a directory.
@click.option(
	'--build_dir',
	help="Path to the output file.",
	default='build',
	show_default=True,
	required=False,
    )
# CLI function 'generate'
@cli.command(help = "Generates ansys compatible .py file")
def generate(build_dir, src):
    log.info('Building the directory')
    utils.clean_dir(build_dir)
    os.system(f"mkdir {build_dir}")
    gen.generator(build_dir, src) 