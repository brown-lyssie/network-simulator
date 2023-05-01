# Takes in argv and returns dictionary with command line arguments in dictionary, all as strings
# Use:
#in terminal: python3 main.py --percent 80 --hello World
#parse_cla will return {"percent": "80", "hello": "World"}
def parse_cla(argv: list) -> dict:
    #argv doesn't have the python3 arg
    # clean_cla is argv without the filename
    clean_cla = argv[1:]
    args = {}
    for i in range(len(clean_cla)):
        try:
            if (clean_cla[i][0:2] == "--" and clean_cla[i+1][0:2] != "--"):
                args[clean_cla[i][2:]] = clean_cla[i+1]
        except:
            pass
    return args