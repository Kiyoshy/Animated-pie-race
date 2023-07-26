# Animated pie race data visualization

The code in this repository allows you to visualize data in an animated pie race, using the sjvisualizer python library.

sjvisualizer is a data visualization and animation library for Python.
Library: https://github.com/SjoerdTilmans/sjvisualizer

Author of the library https://github.com/SjoerdTilmans

## Technical details

* The library only works with .png images.

* The images of the flags are added to the "assets" folder, so that the library can use them automatically.

* Colors for the chart can be defined in code or via a json file. In case the colors are not defined by any means, the library will assign them.

* Image positions and coordinates should be adapted to the size of the screen.


### Prerequisites

This is the basic information to be able to execute the code.

You first need to have Python 3 and Pip 3 installed in your computer. Check here for the proper instructions and code:
```
https://www.python.org/downloads/

$ sudo apt install python3
$ sudo apt install python3-pip
```

Working on Windows:

* Installing the python library sjvisualizer.
```
pip install sjvisualizer
```

Working on Ubuntu:

* Installing the python library sjvisualizer.
```
$ sudo pip install sjvisualizer
```

* Installing Tkinter.
```
$ sudo apt install python3-tk
```

* Installing ImageTk.
```
$ sudo apt-get install python3-pil python3-pil.imagetk
```

### Files

The code in this repository was written and tested in Python 3.

Files contained:

* The `assets` folder is used by the library to store the images of the country flags.

* The file `co2_continent.xlsx` and `co2_country.xlsx` inside the `data` folder contains all the data used for each graph.

* The `Continent.py` and `Country.py` files contain the Python code with the comments that will help you modify the graph.


## Graph's

* CO₂ emissions per Continent.

![](CO2_continent.gif)


* CO₂ emissions per Country.

![](CO2_country.gif)


## License

sjvisualizer is released under the MIT License - see the [LICENSE](LICENSE) file for details.