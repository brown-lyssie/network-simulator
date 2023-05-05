import sys
from parse_cla import parse_cla
from classes.Network import Network
from classes.Packet import Packet
from Simulator import Simulator
def main(clean_argc, clean_argv):
    print(clean_argc)
    print(clean_argv)
    with open("LOG.txt", "a") as f:
        sim = Simulator()


if __name__ == "__main__":
    cla = parse_cla(sys.argv)
    main(len(cla), cla)
