# 311 Group Project: Connecting a City  

## City Connection System  
This project generates a Minimum Spanning Tree (MST) from files containing the intersections and roads of a given city. How this MST is generated and which city it is generated for is up to the user! Choose between four different algorithms, such as Prim's Algorithm or Kruskal's Algorithm, and five different locations, like San Francisco or North America.   

## Description  
From the client's perspective, this system provides solutions that minimize the amount of cable you need to use to fully connect the city of choice, given files continaing intersections (nodes) and roads (edges). From the stuent's perspective, this project compares the strengths and weaknesses of 4 MST generating algorithms: Boruvka's Algorithm, Prim's Algorithm, Reverse-Delete Algorithm, and Boruvka's Algorithm.

## Installation
In order to run this code, ensure that you have a recent version of Python3 downloaded onto your machine. 

## Downloading the repository
To download this repo, simply clone the project using the URL below or download the zip file on the gitlab page under "Code", found here: UPDATE ME

```
# Clone the repo
cd repo_location
git clone UPDATE ME
```

## Run the code  
Once the repo is downloaded, ensure that you are in the directory with the project files. From there, type ```python3 interface.py``` into the terminal to run the interactive interface. You will then be prompted to enter input in the terminal.   
To use the command line with Kruskal's algorithm (which we've decided is our fasted algorithm), type ```python3 cmd-line-prompt.py input_file output_file``` into the command line.

## Interact with the code  
Once ```main.py``` is running, you will be prompted to choose one of four algorithms in order to generate an MST. Entering a number 1 through 4 will use the corresponding algorithm. Then, you will be prompted to choose one of five cities to compute an MST on. The MST will be generated as a uniquely named (based on the algorithm and city) ``.cedge`` file in the ``output/`` directory.   

You will then be prompted to enter another algorithm and city pair or quit the program. Entering ```y``` will bring you back to the previous algorithm choices.  

## Usage
One example of the use of this system is as follows:
If you opt to use the system files and select option 3, Edit Distance, the expected output will return:

## Authors and acknowledgment
Authors of this project include Thao Nguyen, Katrina Wilson, Bhenzel Cadet, and Geoffrey Park  
Completed in April 2024