import ant_gen.generator as gen
from __init__ import __version__
import os
import utils
import click

# Top level group named 'cli'
@click.group()
@click.version_option(version=__version__)
def cli():
	'''Command Line Interface for riscv_application_profiler'''

@click.version_option(version=__version__)
# CLI option 'log'.
# Expects an ISA string.
@click.option(
	'-l',
	'--log',
	help=
	'This option expects the path to an execution log.',
	required=True)
# CLI option 'ISA'
# Expects a ISA.
# CLI option 'output.
# Expects a directory.
@click.option(
	'-o',
	'--output',
	help="Path to the output file.",
	default='./build',
	show_default=True,
	required=False,
    )
# CLI function 'generate'
@cli.command()
def generate():
    utils.clean_dir(build_dir)
    os.system(f"mkdir {build_dir}")
    gen.generator(build_dir) 
