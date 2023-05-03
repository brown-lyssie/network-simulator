import sys
from parse_cla import parse_cla
from classes.Network import Network
from classes.Packet import Packet
def main(clean_argc, clean_argv):
    print(clean_argc)
    print(clean_argv)
    with open("LOG.txt", "a") as f:
        network = Network(chance_of_host_failure=.02, log=True, log_file_obj = f)
        network.add_host_to_network("1:1:1:1:1:1:1:1")
        network.add_host_to_network("2:2:2:2:2:2:2:2")
        network.insert_incoming_packet("1:1:1:1:1:1:1:1", Packet("hello world"), log=True, log_file_obj=f)
        network.transfer_messages_from_hosts("1:1:1:1:1:1:1:1", "2:2:2:2:2:2:2:2", log=True, immediate=True)


if __name__ == "__main__":
    cla = parse_cla(sys.argv)
    main(len(cla), cla)
