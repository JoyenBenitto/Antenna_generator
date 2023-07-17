import generator as gen
import os
import utils
import yaml

build_dir = 'build'
data = []
with open('test/pass/pass1.yaml') as f:
    data = yaml.load(f, Loader= yaml.SafeLoader)

utils.clean_dir(build_dir)
os.system(f"mkdir {build_dir}")
gen.generator(build_dir) 
