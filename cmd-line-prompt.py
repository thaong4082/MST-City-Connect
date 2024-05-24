from sys import argv
from interface import do_mst, export_mst_to_file
from kruskal_algorithm import kruskal
from graph import *
from reverse_delete import *

def cmd_line(input_file, output_file):
  # Use Kruskal's algorithm
  mst = do_mst(kruskal, input_file)
  export_mst_to_file(mst, output_file)

# if __name__ == "__main__":
if len(argv) != 3:
  print("Usage: python3 cmd-line-prompt.py input_file output_file")
else:
  input_file = argv[1]
  output_file = argv[2]
  print("test")
  cmd_line(input_file, output_file)
