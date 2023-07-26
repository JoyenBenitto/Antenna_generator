# Antenna Generator
A python library that allows you to generate microstrip patch antenna in the HFSS  software


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
```
                           +---------------------+
                           |                     |
                           |                     |
Input YAML    ------------>|  Antenna Generator  +----------->  Generated .py
                           |                     |
                           |                     |                    |
                           +---------------------+                    |
                                                                      |
                                                                      |
                                                                      |
                                                                      |
                                                                      v
                                                         +---------------------------+
                                                         |                           |
                                                         |       Ansys HFSS          |
                                                         |                           |
                                                         +---------------------------+
```
                                    
                    
