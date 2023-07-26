```
  /$$$$$$            /$$                                                /$$$$$$                                               /$$                      
 /$$__  $$          | $$                                               /$$__  $$                                             | $$                      
| $$  \ $$/$$$$$$$ /$$$$$$   /$$$$$$ /$$$$$$$ /$$$$$$$  /$$$$$$       | $$  \__/ /$$$$$$ /$$$$$$$  /$$$$$$  /$$$$$$ /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$ 
| $$$$$$$| $$__  $|_  $$_/  /$$__  $| $$__  $| $$__  $$|____  $$      | $$ /$$$$/$$__  $| $$__  $$/$$__  $$/$$__  $|____  $|_  $$_/  /$$__  $$/$$__  $$
| $$__  $| $$  \ $$ | $$   | $$$$$$$| $$  \ $| $$  \ $$ /$$$$$$$      | $$|_  $| $$$$$$$| $$  \ $| $$$$$$$| $$  \__//$$$$$$$ | $$   | $$  \ $| $$  \__/
| $$  | $| $$  | $$ | $$ /$| $$_____| $$  | $| $$  | $$/$$__  $$      | $$  \ $| $$_____| $$  | $| $$_____| $$     /$$__  $$ | $$ /$| $$  | $| $$      
| $$  | $| $$  | $$ |  $$$$|  $$$$$$| $$  | $| $$  | $|  $$$$$$$      |  $$$$$$|  $$$$$$| $$  | $|  $$$$$$| $$    |  $$$$$$$ |  $$$$|  $$$$$$| $$      
|__/  |__|__/  |__/  \___/  \_______|__/  |__|__/  |__/\_______/       \______/ \_______|__/  |__/\_______|__/     \_______/  \___/  \______/|__/  
```
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
