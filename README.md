# Antenna_generator
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

To generate a microstrop patch antenna, run:
```shell
ant_gen generate --ant msp
```
```
                           +---------------------+
                           |                     |
                           |                     |
Input YAML    ------------>|   Antenna Generator +----------->  Generated .py
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
                                    
                    
