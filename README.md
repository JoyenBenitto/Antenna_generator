# Antenna Generator
Antenna_generator is a tool developed with researchers in the field of antenna design in mind. In a nutshell antenna_generator is a python package that allows you to generate microstrip patch antenna in the HFSS software, we have added support for optimizations like cut-out, slots and L slot. 


## Installation

```shell
git clone https://github.com/JoyenBenitto/Antenna_generator.git
cd Antenna_generator
pip install -e .
```

## Usage

To display the help message, run:
```shell
ant_gen --help
ant_gen generate --help
```

To generate an antenna, run:
```shell
ant_gen generate --src [SOURCE]
```
To generate an antenna into a build directory:
```shell
ant_gen generate --build_dir [dir] 
```

# Resources & Thoughts
- Find the pyPatch ppt in `resources\pyPatch.pptx`
