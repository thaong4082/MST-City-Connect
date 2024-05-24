import os.path
import sys
import time
from kruskal_algorithm import *
from prims import prim_mst
from reverse_delete import *
from graph import *
from boruvka import *

###### MAIN ######
# Prompt the user with an interface
def do_interface():
  print("Welcome to the City Connection Project!")

  run = True
  while(run):
    # Prompt user for algorithm
    algorithm = select_alg()

    # Prompt the user for the input file
    input_file = select_input_file()

    mst = do_mst(algorithm, input_file)

    output_filename = make_file_name(algorithm, input_file)

    export_mst_to_file(mst, output_filename)
    print("Algorithm is complete. Output is exported to: " + output_filename) 

    if input("Would you like to enter another algorithm? (y/n): ") in ['y','Y']:
      continue
    else:
      print("Thank you for using the City Connection System!")
      run = False
      sys.exit()

def select_alg():
  print("Please select an algorithm to generate an MST with: ")
  print("(1) Boruvka's")
  print("(2) Prim's")
  print("(3) Kruskal's")
  print("(4) Reverse Delete")

  alg_number = input("Enter corresponding number of algorithm of choice: ")

  if alg_number == '1':
     return boruvka
  if alg_number == '2':
    return prim_mst
  elif alg_number == '3':
    return kruskal
  elif alg_number == '4':
    return reverse_delete
  else:
    print("Invalid algorithm. Try again!")
    do_interface()

def select_input_file():
  print("Choose a file to apply the algorithm to:")
  print("(1) California")
  print("(2) North America")
  print("(3) Oldenburg")
  print("(4) San Francisco")
  print("(5) City of San Joaquin County")
  print("(6) TESTING FILE")

  filename = input("Enter corresponding number of file of choice: ")

  if filename == '1':
    return 'data/cal.cedge'
  elif filename == '2':
    return 'data/NA.cedge'
  elif filename == '3':
    return 'data/OL.cedge'
  elif filename == '4':
    return 'data/SF.cedge'
  elif filename == '5':
    return 'data/TG.cedge'
  elif filename == '6':
    return 'data/test.cedge'
  else:
    print("Invalid file name. Try again!")
    do_interface()

def export_mst_to_file(mst_edges, filename):
    with open(filename, 'w') as file:
        # for i, (u, v, weight) in enumerate(mst_edges):
        #     file.write(f"Edge ID: {i}\n")
        #     file.write(f"2. Start Node ID: {u}\n")
        #     file.write(f"3. End Node ID: {v}\n")
        #     file.write(f"4. Length: {weight}\n\n")
        i = 0
        for u, v, weight in mst_edges:
          file.write(f"{i} {u} {v} {weight}\n")
          i = i + 1

def do_mst(algorithm, filename):

  # Generate a Graph representation of the input file
  graph = Graph(filename)
  
  ## START TIME
  start_time = time.time()
  
  # Run the algorithm on the Graph
  mst = algorithm(graph)

  ##END TIME
  end_time = time.time()

  elapsed_time = end_time - start_time
  milliseconds = elapsed_time * 1000
  print("EXECUTION TIME: ", milliseconds, "ms")
  return mst

def make_file_name(algorithm, city_file):

  # Output MST to a file, named nicely
  str_filename = str(city_file)
  filename_parts = str_filename.split('/')
  city_name = filename_parts[-1].split('.')[0]
  alg_name = ''

  # Get name of the algorithm
  if algorithm == boruvka:
     alg_name = 'boruvka'
  if algorithm == prim_mst:
    alg_name = 'prim_mst'
  elif algorithm == kruskal:
    alg_name = 'kruskal'
  elif algorithm == reverse_delete:
    alg_name = 'reverse_delete'

  output_filename = "output/" + alg_name + "_" + city_name + ".cedge"
  return output_filename

# Run the program!
# do_interface()

if __name__ == "__main__":
    do_interface()