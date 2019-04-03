# Article_views_analysis

A python script that can be launched from the command line or in any python shell (e.g. IDLE: https://docs.python.org/3/library/idle.html). The program outputs answers to the questions:
1. The percentage of people visiting the page via a mobile phone or a tablet device.
2. The times where the number of page views via mobile phone is higher than the mean (throughout the day) number of page views    via mobile phone.

## Getting started
Download a copy of the program (Views_analysis.py) and store it in the same location as the dataset (article-Devices.csv). The location filepath of the csv file on the local machine must be specified inside the read_csv method at line 12.
If the csv file is located in the same folder as the program file, the program downloaded from the repository does not need to be modified.

The output file names are Result_mobile_percentage.txt, which answers question 1 above, and Result_times_above_mean.txt, which answers question 2.
The names of the files can be changed along with a location at lines 27 and 37 respectively. 
Leaving them unchanged will create the files in the same location folder as the program.

## Prerequisites

Python 3.6 or later: https://www.python.org/downloads/.

Python packages: NumPy (http://www.numpy.org/), Pandas (https://pandas.pydata.org/).

## Installing

Install python3 and the above packages as described for your local environment at the above links.

Example for MacOS terminal/linux command line (using PIP, a python package manager that is included by default in releases greater than Python 3.4):

```
$ pip install pandas
```

```
$ pip install numpy
```

## Running the program

The program can be executed from the command line by navigating to the folder containing the program file (using cd command) and then executing the below command:

```
$ python Views_analysis.py
```

Ensure the above is calling python3 by checking:

```
$ python --version
```

If your default is not set to python3, execute the program with the python3 command instead of python in the example line for running the program above.

## Results

The program will output the answer to question 1 to the terminal/shell when executed, and create the two text files as outlined above.

The text files containing the results of the program are included in the repository as Result_mobile_percentage.txt, which answers question 1 above, and Result_times_above_mean.txt which answers question 2.

## Author
Conor Molumby

## License
Copyright 2019 Conor Molumby. This repository is provided under the MIT license (https://opensource.org/licenses/MIT).
