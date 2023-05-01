import sys
from parse_cla import parse_cla
from classes.Graph import Graph
from classes.Network import Network

def main(clean_argc, clean_argv):
    print(clean_argc)
    print(clean_argv)



if __name__ == "__main__":
    cla = parse_cla(sys.argv)
    main(len(cla), cla)