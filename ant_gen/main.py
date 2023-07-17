import generator as gen
import os
import utils


build_dir = 'build'
utils.clean_dir(build_dir)
os.system(f"mkdir {build_dir}")
gen.generator(build_dir)